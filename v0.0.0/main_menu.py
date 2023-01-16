import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import _parser_
import vlc
import os 

channel_categories_listed = False 
series_categories_listed = False 
movies_categories_listed = False 
MAX_VOLUME = 250
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.player = vlc.MediaPlayer()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 691)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.frame_2.setObjectName("frame_2l")
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
        self.time_Slider = QtWidgets.QSlider(self.groupBox_4)
        self.time_Slider.setGeometry(QtCore.QRect(10, 20, 850, 5))
        self.time_Slider.setOrientation(QtCore.Qt.Horizontal)

        self.time_Slider.setStyleSheet("background-color: rgb(244, 100, 71);\n"
"color: rgb(232, 255, 78);")
        self.time_Slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.time_Slider.setObjectName("time_Slider")
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 500, 155, 111))
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


        #####

        self.btn_close = QtWidgets.QPushButton(self.groupBox)
        self.btn_close.setGeometry(QtCore.QRect(20, 240, 51, 51))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setAutoFillBackground(False)
        self.btn_close.setStyleSheet("QPushButton{\n"
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
        self.btn_close.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./img/close.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QtCore.QSize(45, 49))
        self.btn_close.setObjectName("btn_close")
        self.btn_resize = QtWidgets.QPushButton(self.groupBox)
        self.btn_resize.setGeometry(QtCore.QRect(100, 240, 51, 51))
        self.btn_resize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_resize.setAutoFillBackground(False)
        self.btn_resize.setStyleSheet("QPushButton{\n"
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
        self.btn_resize.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./img/resize.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_resize.setIcon(icon5)
        self.btn_resize.setIconSize(QtCore.QSize(45, 49))
        self.btn_resize.setObjectName("btn_resize")

        ####
        
        self.comboBox_subtitles = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_subtitles.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.comboBox_subtitles.setObjectName("comboBox_subtitles")
        self.comboBox_subtitles.setStyleSheet("color: black;\n"
"")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 380, 155, 111))
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
        self.comboBox_audio = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_audio.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.comboBox_audio.setObjectName("comboBox_audio")
        self.comboBox_audio.setStyleSheet("color: black;\n"
"")


        self.btn_reload_subtitles = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_reload_subtitles.setGeometry(QtCore.QRect(90, 70, 31, 31))
        self.btn_reload_subtitles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reload_subtitles.setAutoFillBackground(False)
        self.btn_reload_subtitles.setStyleSheet("QPushButton{\n"
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
        self.btn_reload_subtitles.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../iptv_player/img/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reload_subtitles.setIcon(icon4)
        self.btn_reload_subtitles.setIconSize(QtCore.QSize(27, 27))
        self.btn_reload_subtitles.setFlat(True)
        self.btn_reload_subtitles.setObjectName("btn_reload_subtitles")


        self.btn_reload_audios = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_reload_audios.setGeometry(QtCore.QRect(90, 70, 31, 31))
        self.btn_reload_audios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reload_audios.setAutoFillBackground(False)
        self.btn_reload_audios.setStyleSheet("QPushButton{\n"
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
        self.btn_reload_audios.setText("")
        self.btn_reload_audios.setIcon(icon4)
        self.btn_reload_audios.setIconSize(QtCore.QSize(27, 27))
        self.btn_reload_audios.setFlat(True)
        self.btn_reload_audios.setObjectName("btn_reload_audios")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_channels.clicked.connect(self.show_channels_category)
        self.btn_series.clicked.connect(self.show_series_category)
        self.btn_movies.clicked.connect(self.show_movies_category)
        #x = _parser_.read_tvFile_contents("../data/test.bi")
        #_parser_.parse_file_contents(x)
        self.channels_categories = _parser_.get_channels()
        self.channels_categories.sort()
        self.movies_categories = _parser_.get_movies()
        self.movies_categories.sort()
        self.series_categories = _parser_.get_series()
        self.series_categories.sort()
        self.show_series_category()
        self.show_movies_category()
        self.show_channels_category()

        ### Channels, series, movies functionality
        self.btn_select_channel_category.clicked.connect(self.load_channels)
        self.btn_select_movies_category.clicked.connect(self.load_movies)
        self.btn_select_series_category.clicked.connect(self.load_series)
        self.btn_stream.clicked.connect(self.stream)
        
        self.player.set_title(555)
        


        ## Video controll
        self.btn_stop.clicked.connect(self.stop_playing)
        self.btn_play.clicked.connect(self.resume)
        self.btn_resize.clicked.connect(self.full_screen_flipflop)
        self.btn_close.clicked.connect(self.kill_stream)
        self.volume_control.valueChanged[int].connect(self.change_volume)
        self.time_Slider.valueChanged[int].connect(self.change_time)
        self.bth_audio_submit.clicked.connect(self.set_audio_track)
        self.bth_subtitle_submit.clicked.connect(self.set_subtitle)
        self.btn_reload_audios.clicked.connect(self.reload_audio_tracks)
        self.btn_reload_subtitles.clicked.connect(self.reload_subtitles)
    
    def reload_audio_tracks(self):
        self.audio_tracks = self.get_audio_tracks()
        if self.audio_tracks == False:
            self.show_msg("No audio avilable for this video")
            return
        self.load_audio_tracks()

    def show_msg(self, msg):
        box = QMessageBox()
        box.setWhatsThis("OBS")
        msg += '\t'*4
        box.setText(msg)
        box.setIcon(QMessageBox.Information)
        x = box.exec_()

    def reload_subtitles(self):
        self.subtitles = self.get_subtitles()
        if self.subtitles == False:
            self.show_msg("No subtitles avilable for this video")
        self.load_subtitles()

    def change_time(self, value):
        print(f"Value ={value}")
        if self.cached_type == "movie" or self.cached_type == "series":
            tot_length = self.player.get_length()
        else:
            return
        netto = int( (value * tot_length) / 100 )
        if netto < self.player.get_time():
            self.time_Slider.setValue(value)
            return

        self.player.set_time(netto)
        


    def load_audio_tracks(self):
        self.comboBox_audio.clear()
        if self.audio_tracks == 0:
            print("Empty audio list")
            return
        
        current_audio = self.player.audio_get_track()
        current_audio_index = 0
        # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
        for i in self.audio_tracks:
            # index of the track 
            print(f"going to add audio {i[1].decode()}")
            self.comboBox_audio.addItem(i[1].decode())

            # set the current audio track 
            if i[0] == current_audio:
                current_audio = self.comboBox_audio.currentIndex()
        
        self.comboBox_audio.setCurrentIndex(current_audio_index)
        
        # set the current audio track
        
        #self.comboBox_audio.setCurrentText(current_audio[1].decode())
            

    def set_audio_track(self):
        # get selected item
        selected = self.comboBox_audio.currentText().encode()
        # get its index 
        if self.audio_tracks == False:
            self.audio_tracks = self.get_audio_tracks()
            if self.audio_tracks == False:
                return
        for i in self.audio_tracks:
            if selected == i[1]:
                self.player.audio_set_track(i[0])
                print(f"Set audio track to {selected}")
                return True 
        print("Faild to set audio")
        return False 
    
    def set_subtitle(self):
        # get selected item
        selected = self.comboBox_subtitles.currentText().encode()
        # get its index 
        if self.subtitles == False:
            self.subtitles = self.get_subtitles()
            if self.subtitles == False:
                return
        for i in self.subtitles:
            if selected == i[1]:
                self.player.video_set_spu(i[0])
                print(f"Set audio track to {selected}")
                return True 
        print("Faild to set audio")
        return False 




    def load_subtitles(self):
        # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
        self.comboBox_subtitles.clear()
        if self.subtitles == 0:
            print("Empty subtitle list")
            return
        current_subtitle = self.player.video_get_spu()
        current_subtitle_index = 0
        for i in self.subtitles:
            # index of the track 
            print(f"going to add sub {i[1].decode()}")
            self.comboBox_subtitles.addItem(i[1].decode())

            # set current subtitles 
            if i[0] == current_subtitle:
                current_subtitle_index = self.comboBox_subtitles.currentIndex()
        
        self.comboBox_subtitles.setCurrentIndex(current_subtitle_index)
        
        # set the current audio track
        
        

    def get_subtitles(self):
        avilable_subtitles = self.player.video_get_spu_description()
        # [(-1, b'Disable'), (257, b'Track 1 - [French]')]
        if len(avilable_subtitles) > 0:
            return avilable_subtitles
        else:
            return False

    def get_audio_tracks(self):
        avilable_tracks = self.player.audio_get_track_description()
        if len(avilable_tracks) > 0:
            return avilable_tracks
        else:
            return False


    def change_volume(self, value):
        netto = int( (value * MAX_VOLUME) / 100 )
        print(f"Value is {netto}")
        self.player.audio_set_volume(netto)
    
    def put_start_volume(self):
        current_volume = self.player.audio_get_volume()
        #netto * 100 / max
        value = int( (current_volume * 100) / MAX_VOLUME )
        self.volume_control.setValue(value)
        
    def kill_stream(self):
        self.player.stop()
    def full_screen_flipflop(self):
        if self.player.get_fullscreen():
            #self.player.video_set_scale(0.7)
            self.player.set_fullscreen(False)
            return 
        #self.player.video_set_scale(0.9)
        self.player.set_fullscreen(True)

    def stop_playing(self):
        self.player.pause()

    def resume(self):
        self.player.play()

    def stream(self):
        # need to get the url first.
        selected = self.listWidget_2.currentItem().text()
        stream_url = self.get_url(selected)
        if stream_url != None:
            x = self.stream_now(stream_url)
            if x != False:
                ##### wait 5 second to handle received frames first.
                time.sleep(4)
                ## get avilavble subtitles 
                self.subtitles = self.get_subtitles()
                self.load_subtitles()
                ## get avilable audio tracks 
                self.audio_tracks = self.get_audio_tracks()
                self.load_audio_tracks()
                self.player.set_title(555)
                self.put_start_volume()
                #####
                return
        ########################################### Show msg to say link can not found 
        print("Error, can not parse the selected item and no link found")
    
    def stream_now(self, url):
        self.player.set_media(vlc.Media(url))
        self.player.video_set_scale(0.95)
        self.player.set_title(555)
        self.player.play()
        state = self.player.get_state()
        if state == vlc.State.Ended or state == vlc.State.Error:
            ###################################### Show msg to say channel has no signal now 
            print("No signal for this selected item")
            return False 

        return True
    
    def get_url(self, selected_item):
        category = self.cached_category
        myList = None
        if self.cached_type == "movie":
            myList = self.movies_categories
        elif self.cached_type == "series":
            myList = self.series_categories
        elif self.cached_type == "channel":
                myList = self.channels_categories
        if category == None or myList == None:
            return 
        
        for i in myList:
            if i[0] == category:
                for j in i[1]:
                    if j.name == selected_item:
                        print(f"Found, {j.name} , {j.link}")
                        return j.link
        return None

    def load_channels(self):
        category = self.listWidget_channels.currentItem().text()
        self.cached_category = category
        self.cached_type = "channel"
        self.listWidget_2.clear()
        for i in self.channels_categories:
            if i[0] == category:
                for channel in i[1]:
                    self.listWidget_2.addItem(channel.name)

    def load_movies(self):
        category = self.listWidget_movies.currentItem().text()
        self.cached_category = category
        self.cached_type = "movie"
        self.listWidget_2.clear()
        for i in self.movies_categories:
            if i[0] == category:
                for movie in i[1]:
                    self.listWidget_2.addItem(movie.name)

    def load_series(self):
        category = self.listWidget_series.currentItem().text()
        self.cached_category = category
        self.cached_type = "series"
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
        try:
            self.stackedWidget.setCurrentIndex(2)
        except:
            pass
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
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Rodri IPTV"))
        self.label.setText(_translate("MainWindow", "  Channels"))
        self.btn_select_channel_category.setText(_translate("MainWindow", "Select"))
        self.label_6.setText(_translate("MainWindow", "  Movies"))
        self.btn_select_movies_category.setText(_translate("MainWindow", "Select"))
        self.label_7.setText(_translate("MainWindow", "  Series"))
        self.btn_select_series_category.setText(_translate("MainWindow", "Select"))
        self.btn_channels.setText(_translate("MainWindow", "Channels"))
        self.btn_movies.setText(_translate("MainWindow", "Movies"))
        self.btn_series.setText(_translate("MainWindow", "Series"))
        self.label_2.setText(_translate("MainWindow", "  Items"))
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
    import login_menu
    x = login_menu.lunch_login_menu()
    print(f"XXXX is {x}")
    if x:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


