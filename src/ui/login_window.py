"""Login window.

Layout is done with Qt layouts and styling lives in ``styles.LOGIN_QSS``,
so there are no hard-coded geometries or per-widget stylesheets here.

Usage:
    app = QApplication(sys.argv)
    tv = launch_login_menu(app)      # Tv instance, or None if the user quit
"""
from contextlib import contextmanager
from pathlib import Path

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMessageBox, QPushButton, QRadioButton,
    QStackedWidget, QVBoxLayout, QWidget,
)

import src.Account as Account
import src.request_service as request_service
import src.Tv as Tv
from src.ui.styles import LOGIN_QSS

SRC_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = SRC_DIR / "img"


# --------------------------------------------------------------------------
# Pages: pure UI, they only emit a signal when the user presses "Enter".
# --------------------------------------------------------------------------
class NewAccountPage(QWidget):
    submitted = pyqtSignal(str, str, str, str)  # name, username, password, server

    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.server = QLineEdit()
        self.server.setPlaceholderText("http://example.com:8080")
        self._fields = (self.name, self.username, self.password, self.server)

        form = QFormLayout()
        form.setVerticalSpacing(12)
        form.addRow("Name", self.name)
        form.addRow("Username", self.username)
        form.addRow("Password", self.password)
        form.addRow("Server link", self.server)

        self.submit_btn = QPushButton("Enter")
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.submit_btn.clicked.connect(self._emit_values)

        layout = QVBoxLayout(self)
        layout.addLayout(form)
        layout.addWidget(self.submit_btn)
        layout.addStretch()

    def clear(self):
        for field in self._fields:
            field.clear()

    def _emit_values(self):
        self.submitted.emit(*(f.text().strip() for f in self._fields))


class ExistingAccountPage(QWidget):
    submitted = pyqtSignal(str, bool)  # account name, refresh_from_server

    def __init__(self, parent=None):
        super().__init__(parent)
        self.accounts = QComboBox()
        self.accounts.setCursor(Qt.PointingHandCursor)

        self.use_cache = QRadioButton("Read from cache (Fast)")
        self.refresh = QRadioButton("Get new version (Slow)")
        self.use_cache.setChecked(True)  # sensible default, no "choose one" popup

        box = QGroupBox("Activity")
        box_layout = QVBoxLayout(box)
        box_layout.addWidget(self.use_cache)
        box_layout.addWidget(self.refresh)

        self.submit_btn = QPushButton("Enter")
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.submit_btn.clicked.connect(self._emit_values)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Account"))
        layout.addWidget(self.accounts)
        layout.addWidget(box)
        layout.addWidget(self.submit_btn)
        layout.addStretch()

    def set_accounts(self, names):
        self.accounts.clear()
        self.accounts.addItems(names)

    def _emit_values(self):
        self.submitted.emit(self.accounts.currentText(), self.refresh.isChecked())


# --------------------------------------------------------------------------
# Window: wires the pages to the services (Account / request_service / Tv).
# --------------------------------------------------------------------------
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tv = None  # set on successful login
        self.setWindowTitle("Login to Rodri IPTV")
        self.setWindowIcon(QIcon(str(IMG_DIR / "logo.jpg")))
        self.setMinimumSize(720, 520)
        self.setStyleSheet(LOGIN_QSS)
        self._build_ui()
        self._connect_signals()

    # ---- construction ----------------------------------------------------
    def _build_ui(self):
        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)

        self.btn_new = QPushButton("New Account")
        self.btn_existing = QPushButton("Existing Account")
        for btn in (self.btn_new, self.btn_existing):
            btn.setCursor(Qt.PointingHandCursor)

        tabs = QHBoxLayout()
        tabs.addWidget(self.btn_new)
        tabs.addWidget(self.btn_existing)

        self.new_page = NewAccountPage()
        self.existing_page = ExistingAccountPage()
        self.pages = QStackedWidget()
        self.pages.addWidget(self.new_page)
        self.pages.addWidget(self.existing_page)

        self.status = QLabel("")
        self.status.setObjectName("status")

        left = QVBoxLayout()
        left.addLayout(tabs)
        left.addWidget(self.pages, 1)
        left.addWidget(self.status)

        title = QLabel("Free IPTV")
        title.setObjectName("title")
        logo = QLabel()
        logo.setPixmap(
            QPixmap(str(IMG_DIR / "logo.jpg")).scaled(
                220, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        right = QVBoxLayout()
        right.addStretch()
        right.addWidget(title)
        right.addWidget(logo)

        layout = QHBoxLayout(root)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(24)
        layout.addLayout(left, 1)
        layout.addLayout(right)

        self._interactive = (self.btn_new, self.btn_existing, self.pages)

    def _connect_signals(self):
        self.btn_new.clicked.connect(self._show_new_page)
        self.btn_existing.clicked.connect(self._show_existing_page)
        self.new_page.submitted.connect(self._on_new_account)
        self.existing_page.submitted.connect(self._on_existing_account)

    # ---- navigation ------------------------------------------------------
    def _show_new_page(self):
        self.new_page.clear()
        self.pages.setCurrentWidget(self.new_page)

    def _show_existing_page(self):
        # Re-read every time, so freshly created accounts show up.
        self.existing_page.set_accounts(self._read_account_names())
        self.pages.setCurrentWidget(self.existing_page)

    # ---- actions ---------------------------------------------------------
    def _on_new_account(self, name, username, password, server):
        if not all((name, username, password, server)):
            self._info("Fill all fields, please!")
            return

        try:
            with self._busy("Requesting channel list from the server..."):
                Account.Account(name, username, password, server)
                content = request_service.download_playlist(
                    server, username, password, name
                )
        except request_service.RequestError as error:
            self._info(str(error))
            return

        self._load_tv(Tv.Tv(content, new_tv=True))

    def _on_existing_account(self, name, refresh):
        if not name:
            self._info("No account selected.")
            return

        if refresh:
            credentials = self._read_account_credentials(name)
            if credentials is None:
                self._info("Could not find the saved credentials for this account.")
                return
            username, password, server = credentials
            try:
                with self._busy("Requesting an updated channel list from the server..."):
                    content = request_service.download_playlist(
                        server, username, password, name
                    )
            except request_service.RequestError as error:
                self._info(str(error))
                return
            tv = Tv.Tv(content, new_tv=True)
        else:
            with self._busy("Reading cached channel list..."):
                tv = Tv.Tv(str(request_service.cache_path(name)))

        if not tv.is_loaded:
            self._info("Can not find the cached file. Try 'Get new version' / new account.")
            return
        self._load_tv(tv)

    def _load_tv(self, tv):
        if not tv.is_loaded:
            self._info("Error while parsing the TV list.")
            return
        self.tv = tv
        self.close()  # ends app.exec_() in launch_login_menu

    # ---- helpers ---------------------------------------------------------
    @staticmethod
    def _read_account_names():
        lines = Account.Account().read_accounts_from_database() or []
        return [line.split(", ")[0] for line in lines if line.strip()]

    @staticmethod
    def _read_account_credentials(name):
        lines = Account.Account().read_accounts_from_database() or []
        for line in lines:
            fields = line.rstrip("\r\n").split(", ", 3)
            if len(fields) == 4 and fields[0] == name:
                return fields[1], fields[2], fields[3]
        return None

    def _info(self, text):
        QMessageBox.information(self, "Rodri IPTV", text)

    @contextmanager
    def _busy(self, message):
        """Disable the UI while working. Always re-enabled, even on errors."""
        self.status.setText(message)
        for widget in self._interactive:
            widget.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        QApplication.processEvents()
        try:
            yield
        finally:
            QApplication.restoreOverrideCursor()
            for widget in self._interactive:
                widget.setEnabled(True)
            self.status.setText("")


def launch_login_menu(app):
    """Show the login window and return the loaded Tv (or None)."""
    window = LoginWindow()
    window.show()
    app.exec_()
    return window.tv