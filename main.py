import os
import sys
from pathlib import Path

from PyQt5 import QtWidgets

SRC_DIR = Path(__file__).resolve().parent / "src"

# Temporary: Account, request_service and main_menu still use "./data" and
# "./img" relative to the working directory. Remove once they use pathlib.
os.chdir(SRC_DIR)
(SRC_DIR / "data").mkdir(exist_ok=True)

from src.main_menu import Ui_MainWindow
from src.ui.login_window import launch_login_menu


def main():
    app = QtWidgets.QApplication(sys.argv)
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