from PyQt5 import QtCore, QtGui, QtWidgets
import _parser_


channel_categories_listed = False 
series_categories_listed = False 
movies_categories_listed = False 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 691)
        MainWindow.setMinimumSize(QtCore.QSize(890, 691))
        MainWindow.setMaximumSize(QtCore.QSize(890, 691))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 890, 691))
        self.frame.setMinimumSize(QtCore.QSize(686, 691))
        self.frame.setMaximumSize(QtCore.QSize(890, 691))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:  rgb(0, 0, 30)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 60, 311, 571))
        self.stackedWidget.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.listWidget_channels = QtWidgets.QListWidget(self.page)
        self.listWidget_channels.setGeometry(QtCore.QRect(0, 50, 191, 511))
        self.listWidget_channels.setObjectName("listWidget_channels")
        self.listWidget_channels.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("MV Boli")
        self.listWidget_channels.setFont(font)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:  rgb(0, 0, 30);\n"
"color: white;\n"
" border-radius:10px;")
        self.label.setObjectName("label")
        self.btn_select_channel_category = QtWidgets.QPushButton(self.page)
        self.btn_select_channel_category.setGeometry(QtCore.QRect(200, 210, 101, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_select_channel_category.setFont(font)
        self.btn_select_channel_category.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_select_channel_category.setObjectName("btn_select_channel_category")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:  rgb(0, 0, 30);\n"
"color: white;\n"
" border-radius:10px;")
        self.label_6.setObjectName("label_6")
        self.btn_select_movies_category = QtWidgets.QPushButton(self.page_3)
        self.btn_select_movies_category.setGeometry(QtCore.QRect(200, 210, 101, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_select_movies_category.setFont(font)
        self.btn_select_movies_category.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_select_movies_category.setObjectName("btn_select_movies_category")
        self.listWidget_movies = QtWidgets.QListWidget(self.page_3)
        self.listWidget_movies.setGeometry(QtCore.QRect(0, 50, 191, 511))
        self.listWidget_movies.setObjectName("listWidget_movies")

        self.listWidget_movies.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("MV Boli")
        self.listWidget_movies.setFont(font)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:  rgb(0, 0, 30);\n"
"color: white;\n"
" border-radius:10px;")
        self.label_7.setObjectName("label_7")
        self.btn_select_series_category = QtWidgets.QPushButton(self.page_2)
        self.btn_select_series_category.setGeometry(QtCore.QRect(200, 210, 101, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.btn_select_series_category.setFont(font)
        self.btn_select_series_category.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_select_series_category.setObjectName("btn_select_series_category")
        self.listWidget_series = QtWidgets.QListWidget(self.page_2)
        self.listWidget_series.setGeometry(QtCore.QRect(0, 50, 191, 511))
        self.listWidget_series.setObjectName("listWidget_series")

        self.listWidget_series.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("MV Boli")
        self.listWidget_series.setFont(font)

        self.stackedWidget.addWidget(self.page_2)
        self.btn_channels = QtWidgets.QPushButton(self.frame)
        self.btn_channels.setGeometry(QtCore.QRect(10, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.btn_channels.setFont(font)
        self.btn_channels.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_channels.setObjectName("btn_channels")
        self.btn_movies = QtWidgets.QPushButton(self.frame)
        self.btn_movies.setGeometry(QtCore.QRect(130, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.btn_movies.setFont(font)
        self.btn_movies.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_movies.setObjectName("btn_movies")
        self.btn_series = QtWidgets.QPushButton(self.frame)
        self.btn_series.setGeometry(QtCore.QRect(250, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.btn_series.setFont(font)
        self.btn_series.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_series.setObjectName("btn_series")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(360, 60, 311, 571))
        self.frame_2.setStyleSheet("background-color: rgb(24, 24, 24);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:  rgb(0, 0, 30);\n"
"color: white;\n"
" border-radius:10px;")
        self.label_2.setObjectName("label_2")
        self.btn_stream = QtWidgets.QPushButton(self.frame_2)
        self.btn_stream.setGeometry(QtCore.QRect(230, 200, 81, 101))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(13)
        self.btn_stream.setFont(font)
        self.btn_stream.setStyleSheet("QPushButton{\n"
"    background-color: rgb(253, 255, 88);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(244, 100, 71);\n"
"    color: rgb(232, 255, 78);\n"
"}\n"
"")
        self.btn_stream.setObjectName("btn_select_channel_category_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 50, 211, 511))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("MV Boli")
        self.listWidget_2.setFont(font)

        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 630, 871, 41))
        self.groupBox_4.setStyleSheet("color: rgb(253, 255, 88);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 20, 850, 5))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(370, 670, 221, 20))
        self.label_4.setStyleSheet("color: rgb(232, 255, 78);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(780, 670, 111, 20))
        self.label_5.setStyleSheet("color: rgb(232, 255, 78);")
        self.label_5.setObjectName("label_5")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(700, 10, 171, 621))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(253, 255, 88);")
        self.groupBox.setObjectName("groupBox")
        self.volume_control = QtWidgets.QSlider(self.groupBox)
        self.volume_control.setGeometry(QtCore.QRect(10, 60, 141, 31))
        self.volume_control.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volume_control.setStyleSheet("background-color: rgb(244, 100, 71);\n"
"color: rgb(232, 255, 78);")
        self.volume_control.setOrientation(QtCore.Qt.Horizontal)
        self.volume_control.setObjectName("volume_control")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:  rgb(0, 0, 30);\n"
"color: rgb(253, 255, 88);\n"
" border-radius:10px;")
        self.label_3.setObjectName("label_3")
        self.btn_stop = QtWidgets.QPushButton(self.groupBox)
        self.btn_stop.setGeometry(QtCore.QRect(100, 110, 51, 51))
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stop.setAutoFillBackground(False)
        self.btn_stop.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.btn_stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon)
        self.btn_stop.setIconSize(QtCore.QSize(46, 50))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_play = QtWidgets.QPushButton(self.groupBox)
        self.btn_play.setGeometry(QtCore.QRect(20, 110, 51, 51))
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_play.setAutoFillBackground(False)
        self.btn_play.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.btn_play.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/play.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon1)
        self.btn_play.setIconSize(QtCore.QSize(45, 45))
        self.btn_play.setObjectName("btn_play")
        self.btn_before = QtWidgets.QPushButton(self.groupBox)
        self.btn_before.setGeometry(QtCore.QRect(20, 180, 51, 51))
        self.btn_before.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_before.setAutoFillBackground(False)
        self.btn_before.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.btn_before.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_before.setIcon(icon2)
        self.btn_before.setIconSize(QtCore.QSize(45, 49))
        self.btn_before.setObjectName("btn_before")
        self.btn_next = QtWidgets.QPushButton(self.groupBox)
        self.btn_next.setGeometry(QtCore.QRect(100, 180, 51, 51))
        self.btn_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_next.setAutoFillBackground(False)
        self.btn_next.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.btn_next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/next.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QtCore.QSize(45, 49))
        self.btn_next.setObjectName("btn_next")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 500, 121, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.bth_subtitle_submit = QtWidgets.QPushButton(self.groupBox_2)
        self.bth_subtitle_submit.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.bth_subtitle_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bth_subtitle_submit.setAutoFillBackground(False)
        self.bth_subtitle_submit.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.bth_subtitle_submit.setObjectName("bth_subtitle_submit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 380, 121, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.bth_audio_submit = QtWidgets.QPushButton(self.groupBox_3)
        self.bth_audio_submit.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.bth_audio_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bth_audio_submit.setAutoFillBackground(False)
        self.bth_audio_submit.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(244, 100, 71);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(253, 255, 88);\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.bth_audio_submit.setObjectName("bth_audio_submit")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 30, 101, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_channels.clicked.connect(self.show_channels_category)
        self.btn_series.clicked.connect(self.show_series_category)
        self.btn_movies.clicked.connect(self.show_movies_category)
        x = _parser_.read_tvFile_contents("../data/test.bi")
        _parser_.parse_file_contents(x)
        self.channels_categories = _parser_.get_channels()
        self.movies_categories = _parser_.get_movies()
        self.series_categories = _parser_.get_series()
        self.show_series_category()
        self.show_movies_category()
        self.show_channels_category()

        self.btn_select_channel_category.clicked.connect(self.load_channels)
        self.btn_select_movies_category.clicked.connect(self.load_movies)
        self.btn_select_series_category.clicked.connect(self.load_series)

    def load_channels(self):
        category = self.listWidget_channels.currentItem().text()
        self.listWidget_2.clear()
        for i in self.channels_categories:
            if i[0] == category:
                for channel in i[1]:
                    self.listWidget_2.addItem(channel.name)

    def load_movies(self):
        category = self.listWidget_movies.currentItem().text()
        self.listWidget_2.clear()
        for i in self.movies_categories:
            if i[0] == category:
                for movie in i[1]:
                    self.listWidget_2.addItem(movie.name)

    def load_series(self):
        category = self.listWidget_series.currentItem().text()
        self.listWidget_2.clear()
        for i in self.series_categories:
            if i[0] == category:
                for series in i[1]:
                    self.listWidget_2.addItem(series.name)



    
    def show_channels_category(self):
        #self.listWidget.addItem("Hi")
        global channel_categories_listed
        self.stackedWidget.setCurrentIndex(0)
        if channel_categories_listed : # then we have already listed categories
            return
        for i in self.channels_categories:
            self.listWidget_channels.addItem(i[0])
        
        channel_categories_listed = True

    def show_series_category(self):
        global series_categories_listed
        self.stackedWidget.setCurrentIndex(2)
        if series_categories_listed: # then we have already listed categories
             return
        for i in self.series_categories:
            self.listWidget_series.addItem(i[0])
        series_categories_listed = True

    def show_movies_category(self):
        global movies_categories_listed
        self.stackedWidget.setCurrentIndex(1)
        if movies_categories_listed: # then we have already listed it
             return
        for i in self.movies_categories:
            self.listWidget_movies.addItem(i[0])
        movies_categories_listed = True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Categories"))
        self.btn_select_channel_category.setText(_translate("MainWindow", "Select"))
        self.label_6.setText(_translate("MainWindow", "Categories"))
        self.btn_select_movies_category.setText(_translate("MainWindow", "Select"))
        self.label_7.setText(_translate("MainWindow", "Categories"))
        self.btn_select_series_category.setText(_translate("MainWindow", "Select"))
        self.btn_channels.setText(_translate("MainWindow", "Channels"))
        self.btn_movies.setText(_translate("MainWindow", "Movies"))
        self.btn_series.setText(_translate("MainWindow", "Series"))
        self.label_2.setText(_translate("MainWindow", "Items"))
        self.btn_stream.setText(_translate("MainWindow", "Stream"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Time"))
        self.label_4.setText(_translate("MainWindow", "©® Rodriguez"))
        self.label_5.setText(_translate("MainWindow", "v0.0.1"))
        self.groupBox.setTitle(_translate("MainWindow", "Video Control Buttons"))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Subtitles"))
        self.bth_subtitle_submit.setText(_translate("MainWindow", "Submit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Audio"))
        self.bth_audio_submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
