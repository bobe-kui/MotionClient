from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup
from PySide6.QtSerialPort import QSerialPort
import serial.tools.list_ports


from ui_MotionClient import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        '''Constructors'''
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.status = QLabel()
        self.serial_connection = None
        self.initialize_program()

        '''All Signals'''
        #Move Box
        self.ui.PushButton_Move.clicked.connect(self.relative_move) #move function
        #self.ui.PushButton_Abort.clicked.connect(lambda: self.moveAbort()) #abort move function

        #USB to Serial Box
        self.ui.PushButton_PortRefresh.clicked.connect(self.populate_com_ports)
        self.ui.PushButton_PortConnect.clicked.connect(self.connect_to_port)

    '''All Functions'''
    def initialize_program(self):
        print(f"Running initialize_program...")
        self.populate_com_ports()
        self.update_connection_status(False)

#Com Port Box
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
        print(f"Running update_connection_status...")
        if connected:
            self.ui.Label_ConnectionStatus.setText("Status: Connected")
        else:
            self.ui.Label_ConnectionStatus.setText("Status: Not Connected")
        print(f"update_connection_status successful")

    def relative_move(self):
        print(f"Running relative_move...")
        #Setters
        move_distance = self.ui.LineEdit_Distance.text()
        move_accel = self.ui.LineEdit_Accel.text()
        move_decel = self.ui.LineEdit_Decel.text()
        move_velocity = self.ui.LineEdit_Velocity.text()

        # Validation
        if not move_distance or not move_accel or not move_decel or not move_velocity:
            QMessageBox.warning(self, "Input Error", "All fields must be filled out.")
            return

        try:
            distance = int(move_distance)
            accel = int(move_accel)
            decel = int(move_decel)
            velocity = int(move_velocity)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "All fields must contain valid numbers.")
            return
        
        print(f"Distance: {move_distance} counts\nVelocity: {move_velocity} counts/sec\nAcceleration: {move_accel} counts/sec^2\nDeceleration: {move_decel} counts/sec^2")
        commands = self.generate_relative_move_command(distance, accel, decel, velocity)
        self.send_commands(commands)
        print(f"relative_move successful")

    def generate_relative_move_command(self, move_distance, move_accel, move_decel, move_velocity):
        print(f"Running generate_relative_move_command...")
        """Generates an ASCII command for the motion controller"""
        commands = [
        f"s r0xc8 0\n", #Set the trajectory genearator to aboslute move, trapezoidal profile,
        f"s r0xca {move_distance}\n", #set distance,
        f"s r0xcb {move_velocity}\n", #set max velocity,
        f"s r0xcc {move_accel}\n", #set max acceleration,
        f"s r0xcd {move_decel}\n", #set max deceleration,
        f"g r0x32\n", #Read actual position,
        f"t 1\n", #Execute the move,
        f"g r0xa0\n", #Determine if move has been completed,
        f"g r0xc9\n" #Controller checks trajectory status to see if move was aborted,
        ]
        print(f"generate_relative_move_command successful")
        return commands
    
    def send_commands(self, commands):
            print(f"Running send_commands...")
            if not hasattr(self, 'serial_connection') or not self.serial_connection.is_open:
                print(f"No open serial connection.")
                return

            for command in commands:
                try:
                    self.serial_connection.write(command.encode('ascii'))
                    response = self.serial_connection.readline().decode('ascii').strip()
                    self.ui.responseTextEdit.append(f"Sent: {command.strip()}")
                    self.ui.responseTextEdit.append(f"Received: {response}")
                    print(f"Command sent: {command.strip()}")
                    print(f"Response received: {response}")
                except serial.SerialException as e:
                    print(f"Failed to send command: {e}")
                    break
            print(f"send_commands successful")