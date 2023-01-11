

from PyQt5 import QtCore, QtGui, QtWidgets
from Account import *
import modirator
from PyQt5.QtWidgets import QMessageBox
import _parser_
import Tv


comBox_is_readed = False
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 780)
        MainWindow.setMinimumSize(QtCore.QSize(792, 597))
        MainWindow.setMaximumSize(QtCore.QSize(792, 597))
        font = QtGui.QFont()
        font.setPointSize(1)
        MainWindow.setFont(font)
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
        self.logo.setPixmap(QtGui.QPixmap("img/logo.jpg"))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.widget_1.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_existing_account.clicked.connect(self.existing_account_clicked)
        self.btn_new_account.clicked.connect(self.new_account_menu_clicked)
        self.btn_enter_new.clicked.connect(self.submit_new_account_clicked)
        self.btn_enter_existing.clicked.connect(self.submit_existing_account_clicked)
        self.account = None
    
    def existing_account_clicked(self):
        global comBox_is_readed
        print("show existing accounts menu")
        self.txtBox_username.setText("")
        self.txtBox_name.setText("")
        self.txtBox_password.setText("")
        self.txtBox_server.setText("")
        self.widget_1.setCurrentIndex(1)
        if comBox_is_readed:
            return
        self.account = Account()  # account = list of lines, each line = "name, username, password, server"
        lines = self.account.read_accounts_from_database()
        if lines is not None and lines is not False and len(lines) > 0:
            for line in lines:
                x = line.split(", ")
                self.comboBox_existing_account.addItem(x[0])
        comBox_is_readed = True
        

    def new_account_menu_clicked(self):
        print("show new accounts menu")
        self.txtBox_username.setText("")
        self.txtBox_name.setText("")
        self.txtBox_password.setText("")
        self.txtBox_server.setText("")
        self.widget_1.setCurrentIndex(0)

    def submit_new_account_clicked(self):
        print("submit new account")
        name = self.txtBox_name.text()
        username = self.txtBox_username.text()
        password = self.txtBox_password.text()
        server_link = self.txtBox_server.text()
        account =  Account(name, username, password, server_link)
        if account == False:
            print("Can not create account instance. ")
            ##                                              ## display msg box error 
        #### Need to read the channels file of the choosen tv . name of the file = (tv_name + extention)

    def submit_existing_account_clicked(self):
        print("submit existing account ")
        read_from_cache = self.radioButton_read_from_file.isChecked()
        make_new_request = self.radioButton_update_file.isChecked()
        if read_from_cache == make_new_request == False:
            self.show_msg("Choose: read from cache OR update file, Please! ")
            return
        
        tv_name = self.comboBox_existing_account.currentText()
        x = self.account.confirm_existing_account(tv_name)
        if x == False:
            self.show_msg("Can not confirm the choosen tv")
            return
        #### Need to read the channels file of the choosen tv . name of the file = (tv_name + extention)
        path = "../data/"   ######################################################## Make it dynamic
        tv_name = path +  tv_name + ".bi"
        self.tv = Tv.Tv(tv_name)


        

    def show_msg(self, msg):
        box = QMessageBox()
        box.setWhatsThis("OBS")
        msg += '\t'*4
        box.setText(msg)
        box.setIcon(QMessageBox.Information)
        x = box.exec_()


        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Free IPTV"))
        self.btn_new_account.setText(_translate("MainWindow", "New Account"))
        self.btn_existing_account.setText(_translate("MainWindow", "Exising Accunt"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Server link"))
        self.btn_enter_new.setText(_translate("MainWindow", "Enter"))
        self.label_6.setText(_translate("MainWindow", "Account"))
        self.groupBox.setTitle(_translate("MainWindow", "Activity"))
        self.radioButton_read_from_file.setText(_translate("MainWindow", "Read from cache (Fast)"))
        self.radioButton_update_file.setText(_translate("MainWindow", "Get new version (Slow)"))
        self.btn_enter_existing.setText(_translate("MainWindow", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
