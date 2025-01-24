# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MotionSettingspMrDLD.ui'
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

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(413, 253)
        self.flowControlBox = QComboBox(SettingsWindow)
        self.flowControlBox.setObjectName(u"flowControlBox")
        self.flowControlBox.setGeometry(QRect(310, 180, 79, 22))
        self.parityBox = QComboBox(SettingsWindow)
        self.parityBox.setObjectName(u"parityBox")
        self.parityBox.setGeometry(QRect(310, 122, 79, 22))
        self.stopBitsBox = QComboBox(SettingsWindow)
        self.stopBitsBox.setObjectName(u"stopBitsBox")
        self.stopBitsBox.setGeometry(QRect(310, 151, 79, 22))
        self.dataBitsBox = QComboBox(SettingsWindow)
        self.dataBitsBox.setObjectName(u"dataBitsBox")
        self.dataBitsBox.setGeometry(QRect(310, 93, 79, 22))
        self.baudRateBox = QComboBox(SettingsWindow)
        self.baudRateBox.setObjectName(u"baudRateBox")
        self.baudRateBox.setGeometry(QRect(310, 64, 79, 22))
        self.dataBitsLabel = QLabel(SettingsWindow)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")
        self.dataBitsLabel.setGeometry(QRect(220, 93, 80, 22))
        self.baudRateLabel = QLabel(SettingsWindow)
        self.baudRateLabel.setObjectName(u"baudRateLabel")
        self.baudRateLabel.setGeometry(QRect(220, 64, 80, 22))
        self.parityLabel = QLabel(SettingsWindow)
        self.parityLabel.setObjectName(u"parityLabel")
        self.parityLabel.setGeometry(QRect(220, 122, 80, 22))
        self.stopBitsLabel = QLabel(SettingsWindow)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")
        self.stopBitsLabel.setGeometry(QRect(220, 151, 80, 22))
        self.flowControlLabel = QLabel(SettingsWindow)
        self.flowControlLabel.setObjectName(u"flowControlLabel")
        self.flowControlLabel.setGeometry(QRect(220, 180, 80, 30))
        self.PushButton_Apply = QPushButton(SettingsWindow)
        self.PushButton_Apply.setObjectName(u"PushButton_Apply")
        self.PushButton_Apply.setGeometry(QRect(70, 220, 80, 22))
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 10, 70, 14))
        self.pidLabel = QLabel(SettingsWindow)
        self.pidLabel.setObjectName(u"pidLabel")
        self.pidLabel.setGeometry(QRect(10, 190, 158, 14))
        self.descriptionLabel = QLabel(SettingsWindow)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(10, 40, 158, 14))
        self.vidLabel = QLabel(SettingsWindow)
        self.vidLabel.setObjectName(u"vidLabel")
        self.vidLabel.setGeometry(QRect(10, 160, 158, 14))
        self.manufacturerLabel = QLabel(SettingsWindow)
        self.manufacturerLabel.setObjectName(u"manufacturerLabel")
        self.manufacturerLabel.setGeometry(QRect(10, 70, 158, 14))
        self.serialNumberLabel = QLabel(SettingsWindow)
        self.serialNumberLabel.setObjectName(u"serialNumberLabel")
        self.serialNumberLabel.setGeometry(QRect(10, 100, 158, 14))
        self.label_2 = QLabel(SettingsWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 80, 14))
        self.locationLabel = QLabel(SettingsWindow)
        self.locationLabel.setObjectName(u"locationLabel")
        self.locationLabel.setGeometry(QRect(10, 130, 158, 14))
        self.ComboBox_SerialPort = QComboBox(SettingsWindow)
        self.ComboBox_SerialPort.setObjectName(u"ComboBox_SerialPort")
        self.ComboBox_SerialPort.setGeometry(QRect(220, 30, 170, 30))

        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Dialog", None))
        self.dataBitsLabel.setText(QCoreApplication.translate("SettingsWindow", u"Data bits:", None))
        self.baudRateLabel.setText(QCoreApplication.translate("SettingsWindow", u"BaudRate:", None))
        self.parityLabel.setText(QCoreApplication.translate("SettingsWindow", u"Parity:", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("SettingsWindow", u"Stop bits:", None))
        self.flowControlLabel.setText(QCoreApplication.translate("SettingsWindow", u"Flow control:", None))
        self.PushButton_Apply.setText(QCoreApplication.translate("SettingsWindow", u"Apply", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Parameters", None))
        self.pidLabel.setText(QCoreApplication.translate("SettingsWindow", u"Product ID:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("SettingsWindow", u"Description:", None))
        self.vidLabel.setText(QCoreApplication.translate("SettingsWindow", u"Vendor ID:", None))
        self.manufacturerLabel.setText(QCoreApplication.translate("SettingsWindow", u"Manufacturer:", None))
        self.serialNumberLabel.setText(QCoreApplication.translate("SettingsWindow", u"Serial number:", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWindow", u"Information", None))
        self.locationLabel.setText(QCoreApplication.translate("SettingsWindow", u"Location:", None))
    # retranslateUi

