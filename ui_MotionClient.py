# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MotionClientfPBMyI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 800)
        MainWindow.setAutoFillBackground(False)
        self.Ethernet = QGroupBox(MainWindow)
        self.Ethernet.setObjectName(u"Ethernet")
        self.Ethernet.setEnabled(True)
        self.Ethernet.setGeometry(QRect(10, 20, 250, 120))
        self.lineEdit = QLineEdit(self.Ethernet)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 30, 120, 22))
        self.PortLabel = QLabel(self.Ethernet)
        self.PortLabel.setObjectName(u"PortLabel")
        self.PortLabel.setGeometry(QRect(20, 30, 57, 22))
        self.PortLabel.setLineWidth(1)
        self.lineEdit_2 = QLineEdit(self.Ethernet)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 60, 120, 22))
        self.IPLabel = QLabel(self.Ethernet)
        self.IPLabel.setObjectName(u"IPLabel")
        self.IPLabel.setGeometry(QRect(20, 60, 61, 22))
        self.EthernetButton = QPushButton(self.Ethernet)
        self.EthernetButton.setObjectName(u"EthernetButton")
        self.EthernetButton.setEnabled(True)
        self.EthernetButton.setGeometry(QRect(150, 90, 80, 22))
        self.USBtoSerialBox = QGroupBox(MainWindow)
        self.USBtoSerialBox.setObjectName(u"USBtoSerialBox")
        self.USBtoSerialBox.setEnabled(True)
        self.USBtoSerialBox.setGeometry(QRect(270, 20, 250, 120))
        self.PushButton_PortRefresh = QPushButton(self.USBtoSerialBox)
        self.PushButton_PortRefresh.setObjectName(u"PushButton_PortRefresh")
        self.PushButton_PortRefresh.setGeometry(QRect(20, 90, 80, 22))
        self.PushButton_PortConnect = QPushButton(self.USBtoSerialBox)
        self.PushButton_PortConnect.setObjectName(u"PushButton_PortConnect")
        self.PushButton_PortConnect.setGeometry(QRect(150, 90, 80, 22))
        self.ListWidget_ComPort = QListWidget(self.USBtoSerialBox)
        self.ListWidget_ComPort.setObjectName(u"ListWidget_ComPort")
        self.ListWidget_ComPort.setGeometry(QRect(20, 30, 210, 50))
        self.checkBox = QCheckBox(MainWindow)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 150, 111, 20))
        self.comboBox = QComboBox(MainWindow)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(235, 150, 79, 22))
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 150, 80, 22))
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(395, 150, 30, 22))
        self.comboBox_2 = QComboBox(MainWindow)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(430, 150, 79, 22))
        self.Move = QGroupBox(MainWindow)
        self.Move.setObjectName(u"Move")
        self.Move.setGeometry(QRect(10, 180, 251, 251))
        self.LineEdit_Distance = QLineEdit(self.Move)
        self.LineEdit_Distance.setObjectName(u"LineEdit_Distance")
        self.LineEdit_Distance.setGeometry(QRect(20, 40, 113, 22))
        self.LineEdit_Velocity = QLineEdit(self.Move)
        self.LineEdit_Velocity.setObjectName(u"LineEdit_Velocity")
        self.LineEdit_Velocity.setGeometry(QRect(20, 90, 113, 22))
        self.LineEdit_Accel = QLineEdit(self.Move)
        self.LineEdit_Accel.setObjectName(u"LineEdit_Accel")
        self.LineEdit_Accel.setGeometry(QRect(20, 140, 113, 22))
        self.LineEdit_Decel = QLineEdit(self.Move)
        self.LineEdit_Decel.setObjectName(u"LineEdit_Decel")
        self.LineEdit_Decel.setGeometry(QRect(20, 190, 113, 22))
        self.PushButton_Move = QPushButton(self.Move)
        self.PushButton_Move.setObjectName(u"PushButton_Move")
        self.PushButton_Move.setGeometry(QRect(20, 220, 80, 22))
        self.PushButton_Abort = QPushButton(self.Move)
        self.PushButton_Abort.setObjectName(u"PushButton_Abort")
        self.PushButton_Abort.setGeometry(QRect(150, 220, 80, 22))
        self.IPLabel_2 = QLabel(self.Move)
        self.IPLabel_2.setObjectName(u"IPLabel_2")
        self.IPLabel_2.setGeometry(QRect(20, 20, 61, 22))
        self.IPLabel_3 = QLabel(self.Move)
        self.IPLabel_3.setObjectName(u"IPLabel_3")
        self.IPLabel_3.setGeometry(QRect(20, 70, 61, 22))
        self.IPLabel_4 = QLabel(self.Move)
        self.IPLabel_4.setObjectName(u"IPLabel_4")
        self.IPLabel_4.setGeometry(QRect(20, 120, 61, 22))
        self.IPLabel_5 = QLabel(self.Move)
        self.IPLabel_5.setObjectName(u"IPLabel_5")
        self.IPLabel_5.setGeometry(QRect(20, 170, 61, 22))
        self.groupBox_2 = QGroupBox(MainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(270, 180, 251, 141))
        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 80, 113, 22))
        self.IPLabel_6 = QLabel(self.groupBox_2)
        self.IPLabel_6.setObjectName(u"IPLabel_6")
        self.IPLabel_6.setGeometry(QRect(20, 60, 71, 22))
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 110, 80, 22))
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(150, 110, 80, 22))
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 30, 91, 20))
        self.groupBox_3 = QGroupBox(MainWindow)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(270, 370, 251, 61))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 30, 80, 22))
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 30, 80, 22))
        self.IPLabel_7 = QLabel(MainWindow)
        self.IPLabel_7.setObjectName(u"IPLabel_7")
        self.IPLabel_7.setGeometry(QRect(300, 340, 61, 22))
        self.lineEdit_8 = QLineEdit(MainWindow)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(370, 340, 120, 22))
        self.groupBox_4 = QGroupBox(MainWindow)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 440, 511, 101))
        self.IPLabel_8 = QLabel(self.groupBox_4)
        self.IPLabel_8.setObjectName(u"IPLabel_8")
        self.IPLabel_8.setGeometry(QRect(40, 30, 71, 22))
        self.IPLabel_9 = QLabel(self.groupBox_4)
        self.IPLabel_9.setObjectName(u"IPLabel_9")
        self.IPLabel_9.setGeometry(QRect(40, 60, 91, 22))
        self.IPLabel_10 = QLabel(self.groupBox_4)
        self.IPLabel_10.setObjectName(u"IPLabel_10")
        self.IPLabel_10.setGeometry(QRect(390, 60, 91, 22))
        self.IPLabel_10.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.IPLabel_11 = QLabel(self.groupBox_4)
        self.IPLabel_11.setObjectName(u"IPLabel_11")
        self.IPLabel_11.setGeometry(QRect(410, 30, 71, 22))
        self.IPLabel_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.groupBox_5 = QGroupBox(MainWindow)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 550, 511, 101))
        self.IPLabel_12 = QLabel(self.groupBox_5)
        self.IPLabel_12.setObjectName(u"IPLabel_12")
        self.IPLabel_12.setGeometry(QRect(30, 30, 91, 22))
        self.IPLabel_13 = QLabel(self.groupBox_5)
        self.IPLabel_13.setObjectName(u"IPLabel_13")
        self.IPLabel_13.setGeometry(QRect(30, 60, 91, 22))
        self.lineEdit_9 = QLineEdit(self.groupBox_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(100, 30, 391, 22))
        self.lineEdit_10 = QLineEdit(self.groupBox_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(100, 60, 391, 22))
        self.groupBox_6 = QGroupBox(MainWindow)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 660, 511, 81))
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(25, 40, 80, 22))
        self.comboBox_3 = QComboBox(self.groupBox_6)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(100, 40, 79, 22))
        self.pushButton_7 = QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(280, 40, 80, 22))
        self.pushButton_8 = QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(410, 40, 80, 22))
        self.Label_ConnectionStatus = QLabel(MainWindow)
        self.Label_ConnectionStatus.setObjectName(u"Label_ConnectionStatus")
        self.Label_ConnectionStatus.setGeometry(QRect(20, 750, 200, 22))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.Ethernet.setTitle(QCoreApplication.translate("MainWindow", u"Ethernet", None))
        self.PortLabel.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.IPLabel.setText(QCoreApplication.translate("MainWindow", u"IP address", None))
        self.EthernetButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.USBtoSerialBox.setTitle(QCoreApplication.translate("MainWindow", u"USB-to-Serial", None))
        self.PushButton_PortRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.PushButton_PortConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Enable Motor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Motor Type:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Axis: ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.Move.setTitle(QCoreApplication.translate("MainWindow", u"Move", None))
        self.PushButton_Move.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.PushButton_Abort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.IPLabel_2.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.IPLabel_3.setText(QCoreApplication.translate("MainWindow", u"Velocity", None))
        self.IPLabel_4.setText(QCoreApplication.translate("MainWindow", u"Accel", None))
        self.IPLabel_5.setText(QCoreApplication.translate("MainWindow", u"Decel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.IPLabel_6.setText(QCoreApplication.translate("MainWindow", u"Jog Velocity", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Positive", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Negative", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Activate Jog", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.IPLabel_7.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.lineEdit_8.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Limit Sensors", None))
        self.IPLabel_8.setText(QCoreApplication.translate("MainWindow", u"Neg. Limit", None))
        self.IPLabel_9.setText(QCoreApplication.translate("MainWindow", u"Neg. SW Limit", None))
        self.IPLabel_10.setText(QCoreApplication.translate("MainWindow", u"Pos. SW Limit", None))
        self.IPLabel_11.setText(QCoreApplication.translate("MainWindow", u"Pos. Limit", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"ASCII Command Interface", None))
        self.IPLabel_12.setText(QCoreApplication.translate("MainWindow", u"Command", None))
        self.IPLabel_13.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.Label_ConnectionStatus.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
    # retranslateUi

