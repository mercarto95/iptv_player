"""Download an IPTV playlist (M3U) from an Xtream-codes style server.

No Qt in here: it can be tested and used from any thread. Errors are raised
as ``RequestError`` with a message that is safe to show to the user.
"""
import os
import re
from pathlib import Path
from urllib.parse import urlencode, urlsplit

import requests

DATA_DIR = Path(__file__).resolve().parent / "data"

CONNECT_TIMEOUT = 10   # seconds to establish the connection
READ_TIMEOUT = 30      # max seconds of silence between chunks (not total time)
CHUNK_SIZE = 64 * 1024
# Some providers block the default "python-requests" agent.
HEADERS = {"User-Agent": "VLC/3.0.20 LibVLC/3.0.20"}


class RequestError(Exception):
    """Something went wrong; ``str(error)`` is a user-friendly message."""


def cache_path(name: str) -> Path:
    """Where the playlist for account `name` is cached."""
    safe = re.sub(r"[^\w.\- ]", "_", name).strip() or "playlist"
    return DATA_DIR / f"{safe}.bi"


def build_url(server: str, username: str, password: str) -> str:
    """Build the get.php URL. Tolerates a missing scheme, a trailing slash,
    and a pasted full URL that already contains /get.php?..."""
    server = server.strip()
    if "://" not in server:
        server = "http://" + server
    parts = urlsplit(server)
    if not parts.netloc:
        raise RequestError("Invalid server address.")

    path = parts.path.split("get.php")[0].rstrip("/")
    query = urlencode({
        "username": username,
        "password": password,
        "type": "m3u_plus",
        "output": "ts",
    })  # urlencode escapes special characters in passwords
    return f"{parts.scheme}://{parts.netloc}{path}/get.php?{query}"


def _looks_like_m3u(chunk: bytes) -> bool:
    return chunk.lstrip(b"\xef\xbb\xbf \t\r\n").startswith(b"#EXTM3U")


def download_playlist(server, username, password, name,
                      should_cancel=lambda: False, on_progress=None) -> bytes:
    """Download the playlist, save it to the cache and return its bytes.

    should_cancel: called between chunks; return True to abort.
    on_progress:   called with the number of bytes downloaded so far.
    The cache file is only replaced when the download fully succeeded.
    """
    url = build_url(server, username, password)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    target = cache_path(name)
    tmp = target.with_suffix(".part")
    buffer = bytearray()

    try:
        with requests.get(url, stream=True, headers=HEADERS,
                          timeout=(CONNECT_TIMEOUT, READ_TIMEOUT)) as response:
            
            print("HTTP status:", response.status_code)
            print("Response headers:", dict(response.headers))
            if response.status_code in (401, 403):
                raise RequestError("The server rejected the username or password.")
            if response.status_code == 404:
                raise RequestError("Server found, but it has no playlist at this address.")
            if response.status_code != 200:
                raise RequestError(f"Server answered with error {response.status_code}.")

            with open(tmp, "wb") as f:
                for chunk in response.iter_content(CHUNK_SIZE):
                    if should_cancel():
                        raise RequestError("Cancelled.")
                    if not buffer and not _looks_like_m3u(chunk):
                        # Many servers answer 200 with empty/JSON on bad login.
                        raise RequestError(
                            "The server did not return a playlist. "
                            "Check username, password and that the account is active.")
                    f.write(chunk)
                    buffer.extend(chunk)
                    if on_progress:
                        on_progress(len(buffer))

        if not buffer:
            raise RequestError("The server returned an empty playlist.")
        os.replace(tmp, target)  # atomic: never leaves a half-written cache
        return bytes(buffer)

    except RequestError:
        raise
    except requests.exceptions.ConnectTimeout:
        raise RequestError("Timed out connecting to the server. Check address and port.")
    except requests.exceptions.ReadTimeout:
        raise RequestError("The server stopped responding.")
    except requests.exceptions.SSLError:
        raise RequestError("Secure connection failed (SSL). Try http:// instead of https://.")
    except requests.exceptions.ConnectionError:
        raise RequestError("Could not connect to the server. Check the address and your internet.")
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema):
        raise RequestError("Invalid server address.")
    except requests.exceptions.RequestException as e:
        raise RequestError(f"Request failed: {e}")
    except OSError as e:
        raise RequestError(f"Could not save the playlist: {e}")
    finally:
        tmp.unlink(missing_ok=True)
        