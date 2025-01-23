# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MotionClientNYDoye.ui'
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
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 701)
        MainWindow.setAutoFillBackground(False)
        self.USBtoSerialBox = QGroupBox(MainWindow)
        self.USBtoSerialBox.setObjectName(u"USBtoSerialBox")
        self.USBtoSerialBox.setEnabled(True)
        self.USBtoSerialBox.setGeometry(QRect(270, 50, 250, 300))
        self.PushButton_PortConnect = QPushButton(self.USBtoSerialBox)
        self.PushButton_PortConnect.setObjectName(u"PushButton_PortConnect")
        self.PushButton_PortConnect.setGeometry(QRect(40, 240, 80, 22))
        self.PushButton_PortDisconnect = QPushButton(self.USBtoSerialBox)
        self.PushButton_PortDisconnect.setObjectName(u"PushButton_PortDisconnect")
        self.PushButton_PortDisconnect.setGeometry(QRect(140, 240, 80, 22))
        self.flowControlLabel = QLabel(self.USBtoSerialBox)
        self.flowControlLabel.setObjectName(u"flowControlLabel")
        self.flowControlLabel.setGeometry(QRect(40, 210, 180, 30))
        self.dataBitsLabel = QLabel(self.USBtoSerialBox)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")
        self.dataBitsLabel.setGeometry(QRect(40, 123, 180, 22))
        self.stopBitsLabel = QLabel(self.USBtoSerialBox)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")
        self.stopBitsLabel.setGeometry(QRect(40, 181, 180, 22))
        self.parityLabel = QLabel(self.USBtoSerialBox)
        self.parityLabel.setObjectName(u"parityLabel")
        self.parityLabel.setGeometry(QRect(40, 152, 180, 22))
        self.baudRateLabel = QLabel(self.USBtoSerialBox)
        self.baudRateLabel.setObjectName(u"baudRateLabel")
        self.baudRateLabel.setGeometry(QRect(40, 94, 180, 22))
        self.statusLabel = QLabel(self.USBtoSerialBox)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(40, 70, 180, 22))
        self.settingsButton = QPushButton(self.USBtoSerialBox)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(90, 270, 80, 22))
        self.statusLabel_2 = QLabel(self.USBtoSerialBox)
        self.statusLabel_2.setObjectName(u"statusLabel_2")
        self.statusLabel_2.setGeometry(QRect(40, 40, 180, 22))
        self.CheckBox_EnableMotor = QCheckBox(MainWindow)
        self.CheckBox_EnableMotor.setObjectName(u"CheckBox_EnableMotor")
        self.CheckBox_EnableMotor.setGeometry(QRect(20, 18, 111, 20))
        self.comboBox = QComboBox(MainWindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(245, 18, 79, 22))
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 18, 80, 22))
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(375, 18, 30, 22))
        self.ComboBox_AxisSelect = QComboBox(MainWindow)
        self.ComboBox_AxisSelect.addItem("")
        self.ComboBox_AxisSelect.addItem("")
        self.ComboBox_AxisSelect.addItem("")
        self.ComboBox_AxisSelect.setObjectName(u"ComboBox_AxisSelect")
        self.ComboBox_AxisSelect.setGeometry(QRect(410, 18, 79, 22))
        self.Move = QGroupBox(MainWindow)
        self.Move.setObjectName(u"Move")
        self.Move.setGeometry(QRect(10, 198, 251, 251))
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
        self.IPLabel_2.setGeometry(QRect(20, 20, 140, 22))
        self.IPLabel_3 = QLabel(self.Move)
        self.IPLabel_3.setObjectName(u"IPLabel_3")
        self.IPLabel_3.setGeometry(QRect(20, 70, 130, 22))
        self.IPLabel_4 = QLabel(self.Move)
        self.IPLabel_4.setObjectName(u"IPLabel_4")
        self.IPLabel_4.setGeometry(QRect(20, 120, 130, 22))
        self.IPLabel_5 = QLabel(self.Move)
        self.IPLabel_5.setObjectName(u"IPLabel_5")
        self.IPLabel_5.setGeometry(QRect(20, 170, 140, 22))
        self.groupBox_2 = QGroupBox(MainWindow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 50, 251, 141))
        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 80, 113, 22))
        self.IPLabel_6 = QLabel(self.groupBox_2)
        self.IPLabel_6.setObjectName(u"IPLabel_6")
        self.IPLabel_6.setGeometry(QRect(20, 60, 150, 22))
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
        self.groupBox_3.setGeometry(QRect(270, 388, 251, 61))
        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(150, 30, 80, 22))
        self.pushButton_6 = QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 30, 80, 22))
        self.IPLabel_7 = QLabel(MainWindow)
        self.IPLabel_7.setObjectName(u"IPLabel_7")
        self.IPLabel_7.setGeometry(QRect(300, 360, 61, 22))
        self.lineEdit_8 = QLineEdit(MainWindow)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(370, 360, 120, 22))
        self.groupBox_4 = QGroupBox(MainWindow)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 458, 511, 101))
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
        self.groupBox_6 = QGroupBox(MainWindow)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 570, 511, 81))
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
        self.checkButton = QPushButton(MainWindow)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(10, 660, 80, 22))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dialog", None))
        self.USBtoSerialBox.setTitle(QCoreApplication.translate("MainWindow", u"USB-to-Serial", None))
        self.PushButton_PortConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.PushButton_PortDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.flowControlLabel.setText(QCoreApplication.translate("MainWindow", u"Flow control:", None))
        self.dataBitsLabel.setText(QCoreApplication.translate("MainWindow", u"Data bits:", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("MainWindow", u"Stop bits:", None))
        self.parityLabel.setText(QCoreApplication.translate("MainWindow", u"Parity:", None))
        self.baudRateLabel.setText(QCoreApplication.translate("MainWindow", u"BaudRate:", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.statusLabel_2.setText(QCoreApplication.translate("MainWindow", u"Port Name:", None))
        self.CheckBox_EnableMotor.setText(QCoreApplication.translate("MainWindow", u"Enable Motor", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Stepper", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Motor Type:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Axis: ", None))
        self.ComboBox_AxisSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"X", None))
        self.ComboBox_AxisSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Y", None))
        self.ComboBox_AxisSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"Z", None))

        self.Move.setTitle(QCoreApplication.translate("MainWindow", u"Move", None))
        self.PushButton_Move.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.PushButton_Abort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.IPLabel_2.setText(QCoreApplication.translate("MainWindow", u"Distance (counts)", None))
        self.IPLabel_3.setText(QCoreApplication.translate("MainWindow", u"Velocity (counts/sec)", None))
        self.IPLabel_4.setText(QCoreApplication.translate("MainWindow", u"Accel (counts/sec^2)", None))
        self.IPLabel_5.setText(QCoreApplication.translate("MainWindow", u"Decel (counts/sec^2)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Jog", None))
        self.IPLabel_6.setText(QCoreApplication.translate("MainWindow", u"Jog Velocity (counts/sec)", None))
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
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Sequences", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"Check", None))
    # retranslateUi

