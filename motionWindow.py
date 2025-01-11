from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup, QComboBox, QDialog
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo


from ui_MotionClient import Ui_MainWindow

BLANK_STRING = "N/A"

CUSTOM_BAUDRATE_INDEX = 4

class Settings():
    def __init__(self):
    #Serial Port Stuff
        self.name = ""
        self.baud_rate = 0
        self.string_baud_rate = ""
        self.data_bits = QSerialPort.Data8
        self.string_data_bits = ""
        self.parity = QSerialPort.NoParity
        self.string_parity = ""
        self.stop_bits = QSerialPort.OneStop
        self.string_stop_bits = ""
        self.flow_control = QSerialPort.SoftwareControl
        self.string_flow_control = ""
        self.local_echo_enabled = False

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        #Serial Port Stuff
        super().__init__(parent)
        self.m_ui = Ui_MainWindow()
        self._custom_port_inex = -1
        self.m_ui.setupUi(self)
        self.m_currentSettigns = Settings()
        self.m_intValidator = QIntValidator(0, 4000000, self)

        '''All Signals'''
        #Move Box
        self.m_ui.PushButton_Move.clicked.connect(self.relative_move) #move function
        #self.ui.PushButton_Abort.clicked.connect(lambda: self.moveAbort()) #abort move function

        #USB to Serial Box
        self.m_ui.PushButton_PortRefresh.clicked.connect(self.populate_com_ports)
      #  self.m_ui.PushButton_PortConnect.clicked.connect(self.connect_to_port)
        #Enable Motor Checkbox

    '''All Functions'''
    def initialize_program(self):
        print(f"Running initialize_program...")
        self.populate_com_ports()
        self.update_connection_status(False)

#Com Port Box
    
    #Populates the list of available COM Ports
    def populate_com_ports(self, idx):
        print(f"Running populate_com_ports...")
        if idx == -1:
            return
        
        list = self.m_ui.serialPortInfoListBox.itemData(idx)
        count = len(list) if list else 0
        description = list[1] if count > 1 else BLANK_STRING

        print(f"populate_com_ports successful")

#    def connect_to_port(self):
#        print(f"Running connect_to_port...")
# 
#        selected_items = self.m_ui.ListWidget_ComPort.selectedItems()
#        if not selected_items:
#            print(f"No COM port selected.")
#            return
#        selected_port = selected_items[0].text()
#        try:
#            self.serial_connection = serial.Serial(selected_port, baudrate=9600, timeout=1)
#            self.update_connection_status(True)
#            print(f"Connected to {selected_port}")
#        except Exception as e:
#            self.update_connection_status(False)
#            print(f"Failed to connect to {selected_port}: {e}")
#        print(f"connect_to_port successful")


    def update_connection_status(self, connected):
        print(f"Running update_connection_status...")
        if connected:
            self.m_ui.Label_ConnectionStatus.setText("Status: Connected")
        else:
            self.m_ui.Label_ConnectionStatus.setText("Status: Not Connected")
        print(f"update_connection_status successful")

    def relative_move(self):
        print(f"Running relative_move...")

        #Setters
        move_distance = self.m_ui.LineEdit_Distance.text()
        move_accel = self.m_ui.LineEdit_Accel.text()
        move_decel = self.m_ui.LineEdit_Decel.text()
        move_velocity = self.m_ui.LineEdit_Velocity.text()

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
        """Getting axis data"""
        move_axis = self.m_ui.ComboBox_AxisSelect.currentIndex()
        if move_axis == 0:
            axis = "a"
        elif move_axis == 1:
            axis = "b"
        elif move_axis == 2:
            axis = "c"

        """Generates an ASCII command for the motion controller"""
        commands = [
        f".{axis} s r0xc8 0\n", #Set the trajectory genearator to aboslute move, trapezoidal profile,
        f".{axis} s r0xca {move_distance}\n", #set distance,
        f".{axis} s r0xcb {move_velocity}\n", #set max velocity,
        f".{axis} s r0xcc {move_accel}\n", #set max acceleration,
        f".{axis} s r0xcd {move_decel}\n", #set max deceleration,
        f".{axis} g r0x32\n", #Read actual position,
        f".{axis} t 1\n", #Execute the move,
        f".{axis} g r0xa0\n", #Determine if move has been completed,
        f".{axis} g r0xc9\n", #Controller checks trajectory status to see if move was aborted,
        f".{axis} t 0\n" #Motion stops and th drive is left enabled
        ]
        print(f"generate_relative_move_command successful")
        return commands
    
    def send_commands(self, commands):
        print(f"Running send_commands...")
        # Commenting out the actual serial communication code
        # if not hasattr(self, 'serial_connection') or not self.serial_connection.is_open:
        #     print(f"No open serial connection.")
        #     return

        for command in commands:
            try:
                # self.serial_connection.write(command.encode('ascii'))
                # response = self.serial_connection.readline().decode('ascii').strip()
                #self.ui.responseTextEdit.append(f"Sent: {command.strip()}")
                # self.ui.responseTextEdit.append(f"Received: {response}")
                print(f"Command sent: {command.strip()}")
                # print(f"Response received: {response}")
            except Exception as e:
                print(f"Failed to send command: {e}")
                break
        print(f"send_commands successful")
