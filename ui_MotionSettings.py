# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MotionSettingsLMbVQF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(413, 253)
        self.flowControlBox = QComboBox(Dialog)
        self.flowControlBox.setObjectName(u"flowControlBox")
        self.flowControlBox.setGeometry(QRect(310, 180, 79, 22))
        self.parityBox = QComboBox(Dialog)
        self.parityBox.setObjectName(u"parityBox")
        self.parityBox.setGeometry(QRect(310, 122, 79, 22))
        self.stopBitsBox = QComboBox(Dialog)
        self.stopBitsBox.setObjectName(u"stopBitsBox")
        self.stopBitsBox.setGeometry(QRect(310, 151, 79, 22))
        self.dataBitsBox = QComboBox(Dialog)
        self.dataBitsBox.setObjectName(u"dataBitsBox")
        self.dataBitsBox.setGeometry(QRect(310, 93, 79, 22))
        self.baudRateBox = QComboBox(Dialog)
        self.baudRateBox.setObjectName(u"baudRateBox")
        self.baudRateBox.setGeometry(QRect(310, 64, 79, 22))
        self.dataBitsLabel = QLabel(Dialog)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")
        self.dataBitsLabel.setGeometry(QRect(220, 93, 80, 22))
        self.baudRateLabel = QLabel(Dialog)
        self.baudRateLabel.setObjectName(u"baudRateLabel")
        self.baudRateLabel.setGeometry(QRect(220, 64, 80, 22))
        self.parityLabel = QLabel(Dialog)
        self.parityLabel.setObjectName(u"parityLabel")
        self.parityLabel.setGeometry(QRect(220, 122, 80, 22))
        self.stopBitsLabel = QLabel(Dialog)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")
        self.stopBitsLabel.setGeometry(QRect(220, 151, 80, 22))
        self.flowControlLabel = QLabel(Dialog)
        self.flowControlLabel.setObjectName(u"flowControlLabel")
        self.flowControlLabel.setGeometry(QRect(220, 180, 80, 30))
        self.applyButton = QPushButton(Dialog)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setGeometry(QRect(70, 220, 80, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 70, 14))
        self.pidLabel = QLabel(Dialog)
        self.pidLabel.setObjectName(u"pidLabel")
        self.pidLabel.setGeometry(QRect(10, 190, 158, 14))
        self.descriptionLabel = QLabel(Dialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(10, 40, 158, 14))
        self.vidLabel = QLabel(Dialog)
        self.vidLabel.setObjectName(u"vidLabel")
        self.vidLabel.setGeometry(QRect(10, 160, 158, 14))
        self.manufacturerLabel = QLabel(Dialog)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        self.manufacturerLabel.setGeometry(QRect(10, 70, 158, 14))
        self.serialNumberLabel = QLabel(Dialog)
        self.serialNumberLabel.setObjectName(u"serialNumberLabel")
        self.serialNumberLabel.setGeometry(QRect(10, 100, 158, 14))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 80, 14))
        self.locationLabel = QLabel(Dialog)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setGeometry(QRect(10, 130, 158, 14))
        self.ComboBox_SerialPort = QComboBox(Dialog)
        self.ComboBox_SerialPort.setObjectName(u"ComboBox_SerialPort")
        self.ComboBox_SerialPort.setGeometry(QRect(220, 30, 170, 30))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.dataBitsLabel.setText(QCoreApplication.translate("Dialog", u"Data bits:", None))
        self.baudRateLabel.setText(QCoreApplication.translate("Dialog", u"BaudRate:", None))
        self.parityLabel.setText(QCoreApplication.translate("Dialog", u"Parity:", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("Dialog", u"Stop bits:", None))
        self.flowControlLabel.setText(QCoreApplication.translate("Dialog", u"Flow control:", None))
        self.applyButton.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.pidLabel.setText(QCoreApplication.translate("Dialog", u"Product ID:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"Description:", None))
        self.vidLabel.setText(QCoreApplication.translate("Dialog", u"Vendor ID:", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("Dialog", u"Manufacturer:", None))
        self.serialNumberLabel.setText(QCoreApplication.translate("Dialog", u"Serial number:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Information", None))
        self.locationLabel.setText(QCoreApplication.translate("Dialog", u"Location:", None))
    # retranslateUi

