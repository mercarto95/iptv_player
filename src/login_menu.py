from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QVBoxLayout
from src.Account import *
from PyQt5.QtWidgets import QMessageBox
import src.Tv as Tv, src.login_modirator as login_modirator




is_loading_now = False
comBox_is_readed = False
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app):
        self.app = app
        self.login_successed = False
        self.main_window = MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 780)
        MainWindow.setMinimumSize(QtCore.QSize(792, 597))
        MainWindow.setMaximumSize(QtCore.QSize(792, 597))
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border:0px;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 621))
        self.frame.setMinimumSize(QtCore.QSize(791, 621))
        self.frame.setMaximumSize(QtCore.QSize(791, 621))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:rgb(0, 0, 57);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setGeometry(QtCore.QRect(550, 380, 231, 181))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("./img/logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(550, 280, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(233, 247, 255);")
        self.label_2.setObjectName("label_2")
        self.btn_new_account = QtWidgets.QPushButton(self.frame)
        self.btn_new_account.setGeometry(QtCore.QRect(30, 30, 251, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_new_account.setFont(font)
        self.btn_new_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_new_account.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 64, 166);\n"
"color: rgb(255, 255, 255);\n"
"border: 1;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_new_account.setObjectName("btn_new_account")
        self.btn_existing_account = QtWidgets.QPushButton(self.frame)
        self.btn_existing_account.setGeometry(QtCore.QRect(300, 30, 251, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_existing_account.setFont(font)
        self.btn_existing_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_existing_account.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 64, 166);\n"
"color: rgb(255, 255, 255);\n"
"border: 1;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_existing_account.setObjectName("btn_existing_account")
        self.widget_1 = QtWidgets.QStackedWidget(self.frame)
        self.widget_1.setGeometry(QtCore.QRect(40, 130, 501, 431))
        self.widget_1.setStyleSheet("background-color:rgb(0, 0, 57);\n" 
"")
        self.widget_1.setObjectName("widget_1")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.txtBox_name = QtWidgets.QLineEdit(self.page)
        self.txtBox_name.setGeometry(QtCore.QRect(0, 60, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtBox_name.setFont(font)
        self.txtBox_name.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0.5;\n"
"border-radius: 8px;")
        self.txtBox_name.setObjectName("txtBox_name")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 110, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.txtBox_username = QtWidgets.QLineEdit(self.page)
        self.txtBox_username.setGeometry(QtCore.QRect(0, 160, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtBox_username.setFont(font)
        self.txtBox_username.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0;\n"
"border-radius: 8px;")
        self.txtBox_username.setObjectName("txtBox_username")
        self.txtBox_password = QtWidgets.QLineEdit(self.page)
        self.txtBox_password.setGeometry(QtCore.QRect(0, 260, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtBox_password.setFont(font)
        self.txtBox_password.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0;\n"
"border-radius: 8px;")
        self.txtBox_password.setObjectName("txtBox_password")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(0, 210, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(0, 310, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.txtBox_server = QtWidgets.QLineEdit(self.page)
        self.txtBox_server.setGeometry(QtCore.QRect(0, 350, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtBox_server.setFont(font)
        self.txtBox_server.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0;\n"
"border-radius: 8px;")
        self.txtBox_server.setObjectName("txtBox_server")
        self.btn_enter_new = QtWidgets.QPushButton(self.page)
        self.btn_enter_new.setGeometry(QtCore.QRect(390, 40, 101, 191))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_enter_new.setFont(font)
        self.btn_enter_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter_new.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 64, 166);\n"
"color: rgb(255, 255, 255);\n"
"border: 0;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_enter_new.setObjectName("btn_enter_new")
        self.widget_1.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.comboBox_existing_account = QtWidgets.QComboBox(self.page_2)
        self.comboBox_existing_account.setGeometry(QtCore.QRect(170, 70, 311, 41))
        self.comboBox_existing_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_existing_account.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0;\n"
"border-radius: 8px;")
        self.comboBox_existing_account.setObjectName("comboBox_existing_account")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(280, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        self.groupBox.setGeometry(QtCore.QRect(170, 130, 311, 101))
        self.groupBox.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(0, 0, 97);\n"
"border:0;\n"
"border-radius: 8px;")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_read_from_file = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_read_from_file.setGeometry(QtCore.QRect(10, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_read_from_file.setFont(font)
        self.radioButton_read_from_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_read_from_file.setObjectName("radioButton_read_from_file")
        self.radioButton_update_file = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_update_file.setGeometry(QtCore.QRect(10, 60, 291, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_update_file.setFont(font)
        self.radioButton_update_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_update_file.setObjectName("radioButton_update_file")
        self.btn_enter_existing = QtWidgets.QPushButton(self.page_2)
        self.btn_enter_existing.setGeometry(QtCore.QRect(10, 280, 201, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_enter_existing.setFont(font)
        self.btn_enter_existing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter_existing.setStyleSheet("QPushButton{\n"
"background-color: rgb(64, 64, 166);\n"
"color: rgb(255, 255, 255);\n"
"border: 0.5;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_enter_existing.setObjectName("btn_enter_existing")
        self.widget_1.addWidget(self.page_2)

        ################################################################33
        self.label_gif = QtWidgets.QLabel(self.widget_1)
        self.label_gif.setGeometry(QtCore.QRect(190, 120, 211, 181))
        self.label_gif.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.label_gif.setScaledContents(True)
        self.movie = QMovie("./img/loader.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()

        self.label_gif.setObjectName("label_gif")
        self.label_gif.hide()


        ##################
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(180, 160, 481, 271))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 31);\n"
"border: 1px solid rgb(255, 255, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 441, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(231, 255, 248)")
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.btn_submit_exist = QtWidgets.QPushButton(self.frame_2)
        self.btn_submit_exist.setGeometry(QtCore.QRect(170, 200, 151, 61))
        self.btn_submit_exist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_enter_existing.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.btn_submit_exist.setFont(font)
        self.btn_submit_exist.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 174, 44);\n"
"color:rgb(255, 110, 37);"
"}\n"
"")
        self.btn_submit_exist.setObjectName("btn_submit_exist")
        self.label_waiting_icon = QtWidgets.QLabel(self.frame_2)
        self.label_waiting_icon.setGeometry(QtCore.QRect(360, 130, 101, 81))
        self.label_waiting_icon.setObjectName("label_waiting_icon")

        self.label_waiting_icon.setStyleSheet("background-color: rgb(53, 53, 53);")
        self.label_waiting_icon.setScaledContents(True)
        self.movie = QMovie("./img/loader.gif")
        self.label_waiting_icon.setMovie(self.movie)
        self.movie.start()

        #################
        ######################################################################333
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_window = MainWindow
        
        self.retranslateUi(self.main_window)
        self.widget_1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_existing_account.clicked.connect(self.existing_account_clicked)
        self.btn_new_account.clicked.connect(self.new_account_menu_clicked)
        self.btn_enter_new.clicked.connect(self.submit_new_account_clicked) #submit_new_account_clicked
        self.btn_enter_existing.clicked.connect(self.show_waiting_menu)
        self.btn_submit_exist.clicked.connect(self.submit_existing_account_clicked)
        self.account = None
    
    def existing_account_clicked(self):
        login_modirator.login_existing_account_clicked(self)
        return

    
    def new_account_menu_clicked(self):
        login_modirator.login_new_account_menu_clicked(self)
        return



    def submit_new_account_clicked(self):
        login_modirator.login_submit_new_account_clicked(self)
        return


    def submit_existing_account_clicked(self):
        login_modirator.login_submit_existing_account_clicked(self)
        return

    def show_msg(self, msg):
        box = QMessageBox()
        box.setWhatsThis("OBS")
        msg += '\t'*4
        box.setText(msg)
        box.setIcon(QMessageBox.Information)
        x = box.exec_()


    def show_waiting_menu(self):
        login_modirator.login_show_waiting_menu(self)
        return
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login to Rodri IPTV"))
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Free IPTV"))
        self.btn_new_account.setText(_translate("MainWindow", "New Account"))
        self.btn_existing_account.setText(_translate("MainWindow", "Exising Accunt"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Server link"))
        self.btn_enter_new.setText(_translate("MainWindow", "Enter"))
        self.label_7.setText(_translate("MainWindow", "Its going to take some time to prepare \n"
"things... plz press \"Go Ahead\" to start.."))
        self.frame_2.hide()
        self.btn_submit_exist.setText(_translate("MainWindow", "Go Ahead"))
        self.label_6.setText(_translate("MainWindow", "Account"))
        self.groupBox.setTitle(_translate("MainWindow", "Activity"))
        self.radioButton_read_from_file.setText(_translate("MainWindow", "Read from cache (Fast)"))
        self.radioButton_update_file.setText(_translate("MainWindow", "Get new version (Slow)"))
        self.btn_enter_existing.setText(_translate("MainWindow", "Enter"))


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, app)
    MainWindow.show()
    sys.exit(app.exec_())

print("I defenetly good")
"""





def launch_login_menu():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, app)
    MainWindow.show()
    app.exec_()
    print(f"Login = {ui.login_successed}")
    return ui.login_successed