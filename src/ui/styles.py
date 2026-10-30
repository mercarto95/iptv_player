"""Styling for the login window. Change colours here, nowhere else."""

BG = "rgb(0, 0, 57)"
ACCENT = "rgb(64, 64, 166)"
ACCENT_HOVER = "rgb(244, 100, 71)"
ACCENT_HOVER_TEXT = "rgb(232, 255, 78)"
FIELD_BG = "rgb(218, 218, 218)"
FIELD_TEXT = "rgb(0, 0, 97)"

LOGIN_QSS = f"""
QMainWindow, #root {{
    background-color: {BG};
}}

QLabel {{
    color: white;
    font-family: "MV Boli";
    font-size: 16px;
}}

#title {{
    font-family: "Algerian";
    font-size: 32px;
    font-weight: bold;
    color: rgb(233, 247, 255);
}}

#status {{
    color: rgb(255, 255, 127);
    font-size: 13px;
}}

QLineEdit, QComboBox {{
    background-color: {FIELD_BG};
    color: {FIELD_TEXT};
    border: 0;
    border-radius: 8px;
    padding: 8px;
    font-size: 14px;
}}

QPushButton {{
    background-color: {ACCENT};
    color: white;
    border: 0;
    padding: 12px 20px;
    font-family: "MV Boli";
    font-size: 16px;
}}
QPushButton:hover {{
    background-color: {ACCENT_HOVER};
    color: {ACCENT_HOVER_TEXT};
}}
QPushButton:disabled {{
    background-color: rgb(50, 50, 90);
    color: rgb(150, 150, 150);
}}

QGroupBox {{
    color: white;
    border: 1px solid {ACCENT};
    border-radius: 8px;
    margin-top: 14px;
    padding: 10px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 10px;
}}

QRadioButton {{
    color: white;
    font-family: "MV Boli";
    font-size: 14px;
}}
"""