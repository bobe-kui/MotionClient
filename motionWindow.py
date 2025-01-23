from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup, QComboBox, QDialog, QListWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo


from ui_MotionClient import Ui_MainWindow
from motionSettings import SettingsDialog


BLANK_STRING = "N/A"

CUSTOM_BAUDRATE_INDEX = 4

def description(s):
    return (f"Connected to {s.name} : {s.string_baud_rate}, "
            f"{s.string_data_bits}, {s.string_parity}, {s.string_stop_bits}, "
            f"{s.string_flow_control}")

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        #Serial Port Stuff
        super().__init__(parent)
        #Class definition
        self._custom_port_index = -1
        self.m_ui = Ui_MainWindow() #UI Class
        self.m_ui.setupUi(self) #Set up UI
        self.m_serial = QSerialPort(self) #Serial Port Class
        self.m_settings = SettingsDialog(self) #Settings Class

        self.m_status = QLabel() #Status Label

        self.m_intValidator = QIntValidator(0, 4000000, self) #Int Validator sets min and maximum int input
        self.m_available_ports = QSerialPortInfo.availablePorts()
        self.m_ui.statusLabel.setText("Status: Not Connected")
        '''All Signals'''
        #Move Box
        self.m_ui.PushButton_Move.clicked.connect(self.relative_move) #move function
        #self.ui.PushButton_Abort.clicked.connect(lambda: self.moveAbort()) #abort move function

        #USB to Serial Box
        #self.populate_ports()
        self.m_ui.PushButton_PortConnect.clicked.connect(self.open_serial_port)
        self.m_ui.PushButton_PortDisconnect.clicked.connect(self.close_serial_port)
        self.m_ui.PushButton_PortDisconnect.setEnabled(False)
        self.m_ui.PushButton_PortConnect.setEnabled(True)
        self.m_ui.checkButton.clicked.connect(self.check_port_open)
        self.m_ui.settingsButton.clicked.connect(self.show_settings_dialog())

        #Enable Motor Checkbox
        #self.m_ui.ComboBox_SerialPort.currentIndexChanged.connect(self.show_port_info)
        #self.m_ui.ComboBox_SerialPort.currentIndexChanged.connect(self.m_settings.check_custom_device_path_policy) 

        #self.m_settings.fill_ports_parameters()
    

        self.m_serial.errorOccurred.connect(self.handle_error)
        self.m_serial.readyRead.connect(self.read_data)

    def show_settings_dialog(self):
        self.m_settings.exec()

    @Slot()
    def open_serial_port(self):
        print(f"Running open_serial_port...")
        s = self.m_settings.settings()
        self.m_serial.setPortName(s.name)
        self.m_serial.setBaudRate(s.baud_rate)
        self.m_serial.setDataBits(s.data_bits)
        self.m_serial.setParity(s.parity)
        self.m_serial.setStopBits(s.stop_bits)
        self.m_serial.setFlowControl(s.flow_control)
        print(f"Port Name: {s.name}\nBaud Rate: {s.baud_rate}\nData Bits: {s.data_bits}\nParity: {s.parity}\nStop Bits: {s.stop_bits}\nFlow Control: {s.flow_control}")
        if self.m_serial.open(QIODeviceBase.ReadWrite):
            self.m_ui.PushButton_PortConnect.setEnabled(False) # Disable Connect Button
            self.m_ui.PushButton_PortDisconnect.setEnabled(True) # Enable Disconnect Button
            self.m_ui.ComboBox_SerialPort.setEnabled(False) # Disable Port Selection
            self.m_ui.statusLabel.setText("Status: Connected") # Update Connection Status
            self.show_port_info()
            self.show_status_message(description(s))
            print(f"Connected to {s.name}")
            self.show_status_message(description(s))
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")
            print(f"Connection Failed")
                
    @Slot()
    def close_serial_port(self):
        print(f"Running close_serial_port...")
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_ui.PushButton_PortConnect.setEnabled(True)
        self.m_ui.PushButton_PortDisconnect.setEnabled(False)
        #self.m_ui.ComboBox_SerialPort.setEnabled(True)
        self.m_ui.statusLabel.setText("Status: Not Connected")
        self.show_status_message("Disconnected")
        print(f"close_serial_port successful")

    def show_port_info(self):
        print(f"Running show_port_info...")
        self.m_ui.baudRateLabel.setText(f"Baud Rate: {self.m_settings.settings().baud_rate}")
        self.m_ui.dataBitsLabel.setText(f"Data Bits: {self.m_settings.settings().data_bits}")
        self.m_ui.parityLabel.setText(f"Parity: {self.m_settings.settings().parity}")
        self.m_ui.stopBitsLabel.setText(f"Stop Bits: {self.m_settings.settings().stop_bits}")
        self.m_ui.flowControlLabel.setText(f"Flow Control: {self.m_settings.settings().flow_control}")
        print(f"show_port_info successful")


    def update_connection_status(self, connected):
        print(f"Running update_connection_status...")
        if connected:
            self.m_ui.statusLabel.setText("Status: Connected")
        else:
            self.m_ui.statusLabel.setText("Status: Not Connected")
        print(f"update_connection_status successful")

    def check_port_open(self):
        print(f"Running check_port_open...")
        if self.m_serial.isOpen():
            print(f"Port is open")
        else:
            print(f"Port is closed")
        print(f"check_port_open successful")

    @Slot(str)
    def show_status_message(self,message):
        self.m_status.setText(message)

    @Slot(bytearray)
    def write_data(self, data):
        self.m_serial.write(data)
        print(f"Writing data: {data}")

    @Slot()
    def read_data(self):
        data = self.m_serial.readAll()


    @Slot(QSerialPort.SerialPortError)
    def handle_error(self,error):
        if error == QSerialPort.ResourceError:
            QMessageBox.critical(self, "Critical Error", self.m_serial.errorString())
            self.close_serial_port()

#Move Commands
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
            axis = "0"
        elif move_axis == 1:
            axis = "1"
        elif move_axis == 2:
            axis = "2"


        """Check if entries are valid"""


        """Generates an ASCII command for the motion controller"""
        commands = [
        f"{axis} s r0xc8 0\n", #Set the trajectory genearator to aboslute move, trapezoidal profile,
        f"{axis} s r0xca {move_distance}\n", #set distance (1000 counts = 1 mm)
        f"{axis} s r0xcb {move_velocity}\n", #set max velocity,re4
        f"{axis} s r0xcc {move_accel}\n", #set max acceleration,
        f"{axis} s r0xcd {move_decel}\n", #set max deceleration,
        f"{axis} g r0x32\n", #Read actual position,
        f"{axis} t 1\n", #Execute the move,
        f"{axis} g r0xa0\n", #Determine if move has been completed,
        f"{axis} g r0xc9\n", #Controller checks trajectory status to see if move was aborted,
        f"{axis} t 0\n" #Motion stops and th drive is left enabled
        ]
        print(f"generate_relative_move_command successful")
        return commands
    
    def send_commands(ser, cmd, verbose=True):   
        cmd += '\r'
        ser.write(cmd.encode())
        if verbose:
            print(f" Command: {cmd}")
            
            # Read the response
        response = ser.readline()
        if(len(response) > 0):
            retStr = str(response)
            # chop off the 'b at beginning and carriage return (\r) at end
            retStr = retStr[2:(len(retStr) - 3)]
            if verbose:
                print(f"Response: {retStr}\n")
            return retStr

