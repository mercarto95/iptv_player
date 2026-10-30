import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets
import vlc

SRC_DIR = Path(__file__).resolve().parent / "src"

# Temporary: Account, request_service and main_menu still use "./data" and
# "./img" relative to the working directory. Remove once they use pathlib.
os.chdir(SRC_DIR)
(SRC_DIR / "data").mkdir(exist_ok=True)

from src.main_menu import Ui_MainWindow
from src.ui.login_window import launch_login_menu


def main():
    app = QtWidgets.QApplication(sys.argv)
    try:
        vlc.get_default_instance()
    except (NameError, OSError) as error:
        QtWidgets.QMessageBox.critical(
            None,
            "VLC is unavailable",
            "The VLC runtime library (libvlc) could not be loaded.\n\n"
            "On Ubuntu or Debian, install it with:\n"
            "sudo apt update && sudo apt install vlc\n\n"
            f"Details: {error}",
        )
        return

    tv = launch_login_menu(app)
    if tv is None:
        return
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()