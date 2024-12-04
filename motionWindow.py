from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup
from PySide6.QtSerialPort import QSerialPort
import serial.tools.list_ports


from ui_MotionClient import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status = QLabel()
        self.serial_connection = None
        self.initialize_program()
#~~~~~~~~~~~~~~~ALL BUTTONS~~~~~~~~~~~~~~~~~~~
        #Move Box
        self.ui.PushButton_Move.clicked.connect(lambda: self.move_data()) #move function
       #self.ui.PushButton_Abort.clicked.connect(lambda: self.moveAbort()) #abort move function

        #USB to Serial Box
        self.ui.PushButton_PortRefresh.clicked.connect(lambda: self.populate_com_ports())
        self.ui.PushButton_PortConnect.clicked.connect(lambda: self.connect_to_port())

    def initialize_program(self):
        self.populate_com_ports()
        self.update_connection_status(False)

    def move_data(self):
        #Setters
        distance = self.ui.LineEdit_Distance.text()
        accel = self.ui.LineEdit_Accel.text()
        decel = self.ui.LineEdit_Decel.text()
        velocity = self.ui.LineEdit_Velocity.text()
        print(f"Distance: {distance}\nVelocity: {velocity}\nAcceleration: {accel}\nDeceleration: {decel}")

    def populate_com_ports(self):
      print(f"Running populate_com_ports...")
      """Populates the list of available COM Ports"""
      self.ui.ListWidget_ComPort.clear() #clear current list
      ports = serial.tools.list_ports.comports()
      if not ports:
        self.ui.ListWidget_ComPort.addItem("No COM ports available")
      for port in ports:
          print(f"{port.device} - {port.description}")
          self.ui.ListWidget_ComPort.addItem(port.device)
      print(f"populate_com_ports successful")

    def connect_to_port(self):
        print(f"Running connect_to_port...")
        """Connects to selected COM Port"""
        selected_items = self.ui.ListWidget_ComPort.selectedItems()
        if not selected_items:
            print(f"No COM port selected.")
            return
        selected_port = selected_items[0].text()
        try:
            self.serial_connection = serial.Serial(selected_port, baudrate=9600, timeout=1)
            self.update_connection_status(True)
            print(f"Connected to {selected_port}")
        except Exception as e:
            self.update_connection_status(False)
            print(f"Failed to connect to {selected_port}: {e}")
        print(f"connect_to_port successful")

    def update_connection_status(self, connected):
        if connected==True:
            self.ui.Label_ConnectionStatus.setText("Status: Connected")
        else:
            self.ui.Label_ConnectionStatus.setText("Status: Not Connected")