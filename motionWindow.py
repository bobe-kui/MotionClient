from __future__ import annotations

from PySide6.QtCore import QIODeviceBase, Slot, QThread, QTimer
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QVBoxLayout, QPushButton, QButtonGroup, QComboBox, QDialog, QListWidget
#from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
import serial

from ui_MotionClient import Ui_MainWindow
from motionSettings import SettingsDialog
from motionWorker import Worker
from motionCheckWorker import checkWorker

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
        self.m_ui = Ui_MainWindow() #UI Class
        self.m_ui.setupUi(self) #Set up UI
        self.m_serial = serial.Serial() #Serial Port
        self.m_settings = SettingsDialog(self) #Settings Class
        self.abort_flag = False
        self.worker_thread = None
        self.worker = None
        self.checkWorker_thread = None
        self.checkWorker = None

        self.m_status = QLabel() #Status Label

        self.m_intValidator = QIntValidator(0, 4000000, self) #Int Validator sets min and maximum int input

        self.show_status_message("Not Connected")
        '''All Signals'''
        #Move Box
        self.m_ui.PushButton_Move.clicked.connect(self.relative_move) #move function

        
        self.show_port_info()
        self.m_ui.PushButton_PortConnect.clicked.connect(self.open_serial_port)
        self.m_ui.PushButton_PortDisconnect.clicked.connect(self.close_serial_port)
        self.m_ui.PushButton_PortDisconnect.setEnabled(False)
        self.m_ui.PushButton_PortConnect.setEnabled(True)
        self.m_ui.PushButton_Settings.setEnabled(True)
        self.m_ui.checkButton.clicked.connect(self.start_test_move)
        self.m_ui.PushButton_Settings.clicked.connect(self.show_settings)
        self.m_settings.settings_updated.connect(self.show_port_info)
        self.m_ui.PushButton_Abort.clicked.connect(self.abort_move)

        self.m_ui.GroupBox_Home.setEnabled(False) #Enable Home Checkbox
        self.m_ui.GroupBox_Jog.setEnabled(False) #Enable Jog Checkbox
        self.m_ui.GroupBox_Home.setEnabled(False) #Enable Home Checkbox
        self.m_ui.GroupBox_Limits.setEnabled(False) #Enable Limits Checkbox
        self.m_ui.GroupBox_Move.setEnabled(False) #Enable Move Checkbox
        self.m_ui.GroupBox_Sequences.setEnabled(False) #Enable Sequences Checkbox
        self.m_ui.GroupBox_Motor.setEnabled(False) #Enable Motor Checkbox
        self.m_ui.GroupBox_Serial.setEnabled(True) #Enable Serial Checkbox
        #Enable Motor Checkbox

    @Slot()
    def open_serial_port(self):
        print(f"Running open_serial_port...")
        s = self.m_settings.settings()
        self.m_serial= serial.Serial(port=s.name, baudrate=s.baud_rate, bytesize=s.data_bits, parity = s.parity, timeout= s.stop_bits, xonxoff= s.flow_control)
        print(f"Port Name: {s.name}\nBaud Rate: {s.baud_rate}\nData Bits: {s.data_bits}\nParity: {s.parity}\nStop Bits: {s.stop_bits}\nFlow Control: {s.flow_control}")
        try:
            self.m_ui.PushButton_PortConnect.setEnabled(False)  # Disable Connect Button
            self.m_ui.PushButton_PortDisconnect.setEnabled(True)  # Enable Disconnect Button
            self.m_ui.PushButton_Settings.setEnabled(False)  # Disable Settings Button
            self.m_ui.GroupBox_Home.setEnabled(True)  # Enable Home Checkbox
            self.m_ui.GroupBox_Jog.setEnabled(True)  # Enable Jog Checkbox
            self.m_ui.GroupBox_Limits.setEnabled(True)  # Enable Limits Checkbox
            self.m_ui.GroupBox_Move.setEnabled(True)  # Enable Move Checkbox
            self.m_ui.GroupBox_Sequences.setEnabled(True)  # Enable Sequences Checkbox
            self.m_ui.GroupBox_Motor.setEnabled(True)  # Enable Motor Checkbox
            self.m_ui.statusLabel.setText("Status: Connected")  # Update Connection Status
            self.show_port_info()
            self.start_check_position()
            
        except serial.SerialException as e:
            self.m_ui.statusLabel.setText(f"Status: Error - {str(e)}")  # Update Connection Status with error
 
    @Slot()
    def close_serial_port(self):
        print(f"Running close_serial_port...")
        if self.m_serial.isOpen():
            self.m_serial.close()
            self.m_ui.PushButton_PortConnect.setEnabled(True)
            self.m_ui.PushButton_PortDisconnect.setEnabled(False)
            self.m_ui.PushButton_Settings.setEnabled(True)
            self.m_ui.GroupBox_Home.setEnabled(False) #Enable Home Checkbox
            self.m_ui.GroupBox_Jog.setEnabled(False) #Enable Jog Checkbox
            self.m_ui.GroupBox_Home.setEnabled(False) #Enable Home Checkbox
            self.m_ui.GroupBox_Limits.setEnabled(False) #Enable Limits Checkbox
            self.m_ui.GroupBox_Move.setEnabled(False) #Enable Move Checkbox
            self.m_ui.GroupBox_Sequences.setEnabled(False) #Enable Sequences Checkbox
            self.m_ui.GroupBox_Motor.setEnabled(False) #Enable Motor Checkbox
            self.m_ui.statusLabel.setText("Status: Not Connected")
            self.show_status_message("Disconnected")
            self.check_port_open()
            self.stop_check_position()
        else:
            print(f"Port is already closed")
        print(f"close_serial_port successful")
    
    def show_settings(self):
        print(f"Running show_settings...")
        self.m_settings.show()

    def show_status_message(self, message):
        print(f"Running show_status_message...")
        self.m_ui.statusLabel.setText(message)
        print(f"show_status_message successful")

    def show_port_info(self):
        print(f"Running show_port_info...")
        self.m_ui.portNameLabel.setText(f"Port: {self.m_settings.settings().name}")
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
        if self.m_serial.isOpen():
            print(f"Port is open")
            return True
        else:
            print(f"Port is closed")
            return False

        
    @Slot()
    def abort_move(self):
        print(f"Running abort_move...")
        self.abort_flag = True
        if self.worker:
            self.worker.abort_move()
        
    def log_message(self, message):
        print(message)

    def start_test_move(self):
        if self.check_port_open():
            self.worker_thread = QThread()
            self.worker = Worker(self.m_serial)
            self.worker.moveToThread(self.worker_thread)

            self.worker_thread.started.connect(self.worker.test_move)
            self.worker.finished.connect(self.worker_thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)

            self.worker.command_sent.connect(self.log_message)
            self.worker.response_received.connect(self.log_message)
            self.worker.motion_checked.connect(self.log_message)
            self.worker.final_position_received.connect(self.log_message)
            self.worker.error_occurred.connect(self.log_message)

            self.worker_thread.start()

    def start_relative_move(self, commands):
        if self.check_port_open():
            self.worker_thread = QThread()
            self.worker = Worker(self.m_serial)
            self.worker.moveToThread(self.worker_thread)

            self.worker_thread.started.connect(lambda: self.worker.relative_move(commands))
            self.worker.finished.connect(self.worker_thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.worker_thread.finished.connect(self.worker_thread.deleteLater)

            self.worker.command_sent.connect(self.log_message)
            self.worker.response_received.connect(self.log_message)
            self.worker.motion_checked.connect(self.log_message)
            self.worker.final_position_received.connect(self.log_message)
            self.worker.error_occurred.connect(self.log_message)

            self.worker_thread.start()

    def start_check_position(self):
        if self.check_port_open():
            self.checkWorker_thread = QThread()
            self.checkWorker = checkWorker(self.m_serial)
            self.checkWorker.moveToThread(self.checkWorker_thread)

            self.checkWorker_thread.started.connect(lambda: self.checkWorker.start_continuous_loop())
            self.checkWorker.finished.connect(self.checkWorker_thread.quit)
            self.checkWorker.finished.connect(self.checkWorker.deleteLater)
            self.checkWorker_thread.finished.connect(self.checkWorker_thread.deleteLater)

            self.checkWorker.command_sent.connect(self.log_message)
            self.checkWorker.response_received.connect(self.log_message)
            self.checkWorker.motion_checked.connect(self.log_message)
            self.checkWorker.final_position_received.connect(self.log_message)
            self.checkWorker.error_occurred.connect(self.log_message)

            self.checkWorker_thread.start()

    def stop_check_position(self):
        self.checkWorker_thread.quit()
        self.checkWorker_thread.wait()
        if self.checkWorker_thread is not None:
            if self.checkWorker and self.checkWorker.continuous_loop_flag:
                self.checkWorker.stop_continuous_loop()
            

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
        cmds = self.generate_relative_move_command(distance, accel, decel, velocity)
        self.start_relative_move(cmds)
        print(f"relative_move successful")

    def generate_relative_move_command(self, move_distance, move_accel, move_decel, move_velocity):
        print(f"Running generate_relative_move_command...")
        """Getting axis data"""
        move_axis = self.m_ui.ComboBox_AxisSelect.currentIndex()
        axis = str(move_axis)
        distance = str(move_distance)
        accel = str(move_accel)
        decel = str(move_decel)
        velocity = str(move_velocity)

        """Generates an ASCII command for the motion controller"""
        cmds = [
            f"{axis} g r0x32",  # Initial position
            f"{axis} s r0x24 21",  # Set the desired state to "traj. generator drives position loop"
            f"{axis} s r0xc8 0x100",  # Set the trajectory generator to absolute move, trapezoidal profile
            f"{axis} s r0xca {distance}",  # Set distance (1000 counts = 1 mm)
            f"{axis} s r0xcb {velocity}",  # Set max velocity
            f"{axis} s r0xcc {accel}",  # Set max acceleration
            f"{axis} s r0xcd {decel}",  # Set max deceleration
            f"{axis} g r0x32",  # Read actual position
            f"{axis} t 1"  # Execute the move
        ]
        print(f"generate_relative_move_command successful")
        return cmds

