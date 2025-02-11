from PySide6.QtCore import QThread, QTimer, QObject, Signal, Slot
from PySide6.QtWidgets import QMainWindow
import serial

from ui_MotionClient import Ui_MainWindow


class checkWorker(QObject):
    finished = Signal()
    command_sent = Signal(str)
    response_received = Signal(str)
    motion_checked = Signal(str)
    final_position_received = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, serial_port, parent=None):
        super(checkWorker, self).__init__(parent)
        self.m_ui = Ui_MainWindow()
        self.serial_port = serial_port
        self.continuous_loop_flag = False
        # Start the check worker thread

    def start_continuous_loop(self):
        self.continuous_loop_flag = True
        self.continuous_loop()

    def stop_continuous_loop(self):
        self.continuous_loop_flag = False

    def continuous_loop(self):
        if self.continuous_loop_flag:
            self.check_position()
            print("Running continuous loop...")
            # Call this method again after a short delay
            QTimer.singleShot(1000, self.continuous_loop)

    def check_position(self):
        axis = 2
        try:
            position = self.send_command(f'{axis} g r0x32')
            self.motion_checked.emit(f"Position: {position}")
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error checking position: {e}")

    def send_command(self, command):
        try:
            self.serial_port.write((command + '\r').encode())
            self.command_sent.emit(f"Sending command: {command}")
            response = self.serial_port.readline().decode().strip()
            self.response_received.emit(f"Received response: {response}")
            return response
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error sending command: {e}")
            return ""
