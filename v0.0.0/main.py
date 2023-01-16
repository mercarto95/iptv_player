import requests
import os
os.add_dll_directory(os.getcwd())
import vlc
from _parser_ import *

# server information
server_url = "XXXX"
username = "XXXX"
password = "XXXXX"

def request_data(server_url, username, password):
  # Connect to the server and retrieve the list of channels
  response = requests.get(f"{server_url}", auth=(username, password))
  #channels = response.json()
  c = 0
  x = open("try3.txt", "w")
  for i in response.text:
      try:
          x.write(response.text[c])
          c += 1
      except:
          c += 1
          print("problem")

# Create a VLC player instance
player = vlc.MediaPlayer()

channels = ""
# Function to play a channel
def play_channel(stream_url):
  # Load the stream into the player
  player.set_media(vlc.Media(stream_url))
  # Play the stream
  player.video_set_scale(0.5)
  player.play()
  state = player.get_state()
  if not player.is_playing():
    print("Can not play this item")
  if state == vlc.State.Ended or state == vlc.Sate.Error:
      print("Streaming ended or an error exists!")



series = get_series()
movies = get_movies()
channels = get_channels()


# Play the first channel
play_channel(0)
player.stop()

pass