from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup, QComboBox, QDialog, QListWidget
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo


from ui_MotionClient import Ui_MainWindow
from motionSettings import SettingsDialog
from motionConsole import Console

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

        self.m_console = Console() #Console Class
        self.m_status = QLabel() #Status Label

        self.m_intValidator = QIntValidator(0, 4000000, self) #Int Validator sets min and maximum int input
        self.m_available_ports = QSerialPortInfo.availablePorts()
        self.m_ui.Label_ConnectionStatus.setText("Status: Not Connected")
        '''All Signals'''
        #Move Box
        self.m_ui.PushButton_Move.clicked.connect(self.relative_move) #move function
        #self.ui.PushButton_Abort.clicked.connect(lambda: self.moveAbort()) #abort move function

        #USB to Serial Box
        self.populate_ports()
        self.m_ui.PushButton_PortConnect.clicked.connect(self.open_serial_port)
        self.m_ui.PushButton_PortDisconnect.clicked.connect(self.close_serial_port)
        self.m_ui.PushButton_PortDisconnect.setEnabled(False)
        self.m_ui.PushButton_PortConnect.setEnabled(True)
        #Enable Motor Checkbox

        #self.m_ui.ComboBox_SerialPort.currentIndexChanged.connect(self.show_port_info)
        #self.m_ui.ComboBox_SerialPort.currentIndexChanged.connect(self.m_settings.check_custom_device_path_policy) 

        self.m_settings.fill_ports_parameters()
        self.m_settings.update_settings()

        self.m_serial.errorOccurred.connect(self.handle_error)
        self.m_serial.readyRead.connect(self.read_data)
        self.m_console.get_data.connect(self.write_data)


    #Show all ports when the user clicks on the dropdown
    @Slot()
    def populate_ports(self):
        print(f"Running populate_ports...")
        for port in self.m_available_ports:
            self.m_ui.ComboBox_SerialPort.addItem(port.portName())
        print(f"populate_ports successful")
    
            

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
        if self.m_serial.open(QIODeviceBase.ReadWrite):
            self.m_console.setEnabled(True)
            self.m_console.set_local_echo_enabled(s.local_echo_enabled)
            self.m_ui.PushButton_PortConnect.setEnabled(False)
            self.m_ui.PushButton_PortDisconnect.setEnabled(True)
            self.m_ui.ComboBox_SerialPort.setEnabled(False)
            self.m_ui.Label_ConnectionStatus.setText("Status: Connected")
            self.show_status_message(description(s))
            print(f"Connected to {s.name}")
            #self.m_ui.actionConfigure.setEnabled(False)
            self.show_status_message(description(s))
            self.m_console.put_data("Connected to " + s.name)
        else:
            QMessageBox.critical(self, "Error", self.m_serial.errorString())
            self.show_status_message("Open error")
            print(f"Connection Failed")
                
    @Slot()
    def close_serial_port(self):
        print(f"Running close_serial_port...")
        if self.m_serial.isOpen():
            self.m_serial.close()
        self.m_console.setEnabled(False)
        self.m_ui.PushButton_PortConnect.setEnabled(True)
        self.m_ui.PushButton_PortDisconnect.setEnabled(False)
        self.m_console.setEnabled(False)
        self.m_ui.ComboBox_SerialPort.setEnabled(True)
        self.m_ui.Label_ConnectionStatus.setText("Status: Not Connected")
        self.show_status_message("Disconnected")

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
        self.m_console.put_data(data.data())

    @Slot(QSerialPort.SerialPortError)
    def handle_error(self,error):
        if error == QSerialPort.ResourceError:
            QMessageBox.critical(self, "Critical Error", self.m_serial.errorString())
            self.close_serial_port()

#Move Commands

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
