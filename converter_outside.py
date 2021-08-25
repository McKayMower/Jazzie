# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter_outsidecyFBdU.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_LoadingWindow(object):
    def setupUi(self, LoadingWindow):
        if LoadingWindow.objectName():
            LoadingWindow.setObjectName(u"LoadingWindow")
        LoadingWindow.resize(1080, 720)
        self.centralwidget = QWidget(LoadingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(189, 51, 255);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.appNameLabel = QLabel(self.dropShadowFrame)
        self.appNameLabel.setObjectName(u"appNameLabel")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(35)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.appNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.appNameLabel)

        self.subtitleLabel = QLabel(self.dropShadowFrame)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.subtitleLabel.setFont(font1)
        self.subtitleLabel.setStyleSheet(u"\n"
"color: rgb(226, 151, 255);")
        self.subtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.subtitleLabel)

        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(226, 151, 255);\n"
"	color: rgb(200,200,200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.517, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(254, 121, 199, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.loadingLabel = QLabel(self.dropShadowFrame)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setFont(font1)
        self.loadingLabel.setStyleSheet(u"\n"
"color: rgb(226, 151, 255);")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.loadingLabel)

        self.createdByLabel = QLabel(self.dropShadowFrame)
        self.createdByLabel.setObjectName(u"createdByLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(6)
        self.createdByLabel.setFont(font2)
        self.createdByLabel.setStyleSheet(u"\n"
"color: rgb(226, 151, 255);")
        self.createdByLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.createdByLabel)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        LoadingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingWindow)

        QMetaObject.connectSlotsByName(LoadingWindow)
    # setupUi

    def retranslateUi(self, LoadingWindow):
        LoadingWindow.setWindowTitle(QCoreApplication.translate("LoadingWindow", u"MainWindow", None))
        self.appNameLabel.setText(QCoreApplication.translate("LoadingWindow", u"<strong>Jazzie MP3", None))
        self.subtitleLabel.setText(QCoreApplication.translate("LoadingWindow", u"Converting made <strong>easy</strong>", None))
        self.loadingLabel.setText(QCoreApplication.translate("LoadingWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">loading...</span></p></body></html>", None))
        self.createdByLabel.setText(QCoreApplication.translate("LoadingWindow", u"<html><head/><body><p><span style=\" font-size:8pt; font-weight:600;\">Created by</span><span style=\" font-size:8pt;\">: McKay Mower</span></p></body></html>", None))
    # retranslateUi

