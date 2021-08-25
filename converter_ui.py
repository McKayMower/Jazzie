# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter_uiITWDlG.ui'
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


class Ui_Jazzie(object):
    def setupUi(self, Jazzie):
        if Jazzie.objectName():
            Jazzie.setObjectName(u"Jazzie")
        Jazzie.resize(679, 471)
        self.howToUse = QAction(Jazzie)
        self.howToUse.setObjectName(u"howToUse")
        self.centralwidget = QWidget(Jazzie)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headingLabel = QLabel(self.centralwidget)
        self.headingLabel.setObjectName(u"headingLabel")
        font = QFont()
        font.setFamily(u"PMingLiU-ExtB")
        font.setPointSize(20)
        self.headingLabel.setFont(font)
        self.headingLabel.setStyleSheet(u"")
        self.headingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.headingLabel)

        self.subheadingLabel = QLabel(self.centralwidget)
        self.subheadingLabel.setObjectName(u"subheadingLabel")
        self.subheadingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.subheadingLabel)

        self.urlLabel = QLabel(self.centralwidget)
        self.urlLabel.setObjectName(u"urlLabel")

        self.verticalLayout.addWidget(self.urlLabel)

        self.urlEntry = QLineEdit(self.centralwidget)
        self.urlEntry.setObjectName(u"urlEntry")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlEntry.sizePolicy().hasHeightForWidth())
        self.urlEntry.setSizePolicy(sizePolicy)
        self.urlEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.urlEntry)

        self.startLabel = QLabel(self.centralwidget)
        self.startLabel.setObjectName(u"startLabel")

        self.verticalLayout.addWidget(self.startLabel)

        self.startEntry = QLineEdit(self.centralwidget)
        self.startEntry.setObjectName(u"startEntry")
        self.startEntry.setEnabled(False)
        self.startEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.startEntry)

        self.stopLabel = QLabel(self.centralwidget)
        self.stopLabel.setObjectName(u"stopLabel")

        self.verticalLayout.addWidget(self.stopLabel)

        self.stopEntry = QLineEdit(self.centralwidget)
        self.stopEntry.setObjectName(u"stopEntry")
        self.stopEntry.setEnabled(False)
        self.stopEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.stopEntry)

        self.authorLabel = QLabel(self.centralwidget)
        self.authorLabel.setObjectName(u"authorLabel")

        self.verticalLayout.addWidget(self.authorLabel)

        self.authorEntry = QLineEdit(self.centralwidget)
        self.authorEntry.setObjectName(u"authorEntry")
        self.authorEntry.setEnabled(False)
        self.authorEntry.setAutoFillBackground(False)
        self.authorEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")
        self.authorEntry.setReadOnly(False)

        self.verticalLayout.addWidget(self.authorEntry)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.titleEntry = QLineEdit(self.centralwidget)
        self.titleEntry.setObjectName(u"titleEntry")
        self.titleEntry.setEnabled(False)
        self.titleEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")
        self.titleEntry.setReadOnly(False)

        self.verticalLayout.addWidget(self.titleEntry)

        self.albumLabel = QLabel(self.centralwidget)
        self.albumLabel.setObjectName(u"albumLabel")

        self.verticalLayout.addWidget(self.albumLabel)

        self.albumEntry = QLineEdit(self.centralwidget)
        self.albumEntry.setObjectName(u"albumEntry")
        self.albumEntry.setEnabled(False)
        self.albumEntry.setStyleSheet(u"border: 0.5px solid grey;\n"
"border-radius: 5px;")
        self.albumEntry.setReadOnly(False)

        self.verticalLayout.addWidget(self.albumEntry)

        self.genreLabel = QLabel(self.centralwidget)
        self.genreLabel.setObjectName(u"genreLabel")

        self.verticalLayout.addWidget(self.genreLabel)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.comboBox)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setStyleSheet(u"")
        self.convertButton.setAutoDefault(False)
        self.convertButton.setFlat(False)

        self.verticalLayout.addWidget(self.convertButton)

        Jazzie.setCentralWidget(self.centralwidget)

        self.retranslateUi(Jazzie)

        self.convertButton.setDefault(False)


        QMetaObject.connectSlotsByName(Jazzie)
    # setupUi

    def retranslateUi(self, Jazzie):
        Jazzie.setWindowTitle(QCoreApplication.translate("Jazzie", u"MainWindow", None))
        self.howToUse.setText(QCoreApplication.translate("Jazzie", u"How To Use", None))
        self.headingLabel.setText(QCoreApplication.translate("Jazzie", u"Jazzie MP3 Converter", None))
        self.subheadingLabel.setText(QCoreApplication.translate("Jazzie", u"Enter a URL, change the autofilled entries if wanted, and hit convert!", None))
        self.urlLabel.setText(QCoreApplication.translate("Jazzie", u"YouTube URL:", None))
        self.urlEntry.setText("")
        self.urlEntry.setPlaceholderText(QCoreApplication.translate("Jazzie", u"e.g. www.youtube.com/xyz", None))
        self.startLabel.setText(QCoreApplication.translate("Jazzie", u"Start Time (format: hh:mm:ss.ms, accessible after entering a valid URL):", None))
#if QT_CONFIG(whatsthis)
        self.startEntry.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.startEntry.setText("")
        self.startEntry.setPlaceholderText("")
        self.stopLabel.setText(QCoreApplication.translate("Jazzie", u"Stop Time (format: hh:mm:ss.ms, accessible after entering a valid URL):", None))
        self.stopEntry.setText("")
        self.stopEntry.setPlaceholderText("")
        self.authorLabel.setText(QCoreApplication.translate("Jazzie", u"Artist:", None))
        self.authorEntry.setText("")
        self.titleLabel.setText(QCoreApplication.translate("Jazzie", u"Title:", None))
        self.titleEntry.setText("")
        self.albumLabel.setText(QCoreApplication.translate("Jazzie", u"Album:", None))
        self.albumEntry.setText("")
        self.genreLabel.setText(QCoreApplication.translate("Jazzie", u"Genre:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Jazzie", u"--Select--", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Jazzie", u"Hip-Hop/Rap", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Jazzie", u"Pop", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Jazzie", u"Alternative", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Jazzie", u"Metal", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Jazzie", u"Phonk", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Jazzie", u"Classic Rock", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Jazzie", u"R&B/Soul", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Jazzie", u"House", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Jazzie", u"Other", None))
        self.comboBox.setItemText(10, "")

        self.convertButton.setText(QCoreApplication.translate("Jazzie", u"Convert!", None))
    # retranslateUi

