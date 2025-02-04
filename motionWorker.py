from PySide6.QtCore import QObject, Signal, Slot
import serial

class Worker(QObject):
    finished = Signal()
    command_sent = Signal(str)
    response_received = Signal(str)
    motion_checked = Signal(str)
    final_position_received = Signal(str)
    error_occurred = Signal(str)

    def __init__(self, serial_port, parent=None):
        super(Worker, self).__init__(parent)
        self.serial_port = serial_port
        self.abort_flag = False

    @Slot(list)
    def test_move(self):
        self.abort_flag = False  # Reset the abort flag
        cmds = [
            '2 g r0x32',       # Initial position
            '2 s r0x24 21',     # Desired state to "traj. generator drives position loop"
            '2 s r0xc8 0x100',  # Trapezoidal relative move (same as 256)
            '2 s r0xca -4000', # Position (1000 counts = 1 mm)
            '2 s r0xcb 10000',   # Velocity (Max: 20000 counts/s)
            '2 s r0xcc 20000',  # Acceleration
            '2 s r0xcd 20000',  # Deceleration
            '2 t 1'             # Execute trajectory
        ]
        try:
            for cmd in cmds:
                if self.abort_flag:
                    self.send_command('t0')
                    self.command_sent.emit("Move aborted.")
                    break
                self.send_command(cmd)
            self.check_motion()
            final_position = self.send_command('2 g r0x32')
            self.final_position_received.emit(f"Final Position: {final_position}")
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error: {str(e)}")
        self.finished.emit()

    @Slot(list)
    def relative_move(self, cmds):
        self.abort_flag = False
        try:
            for cmd in cmds:
                if self.abort_flag:
                    self.send_command('t0')
                    self.command_sent.emit("Move aborted.")
                    break
                print(f"Sending command: {cmd}")
                self.send_command(cmd)
            self.check_motion()
            final_position = self.send_command('0 g r0x32')
            self.final_position_received.emit(f"Final Position: {final_position}")
        except serial.SerialException as e:
            self.error_occurred.emit(f"Error: {str(e)}")
        self.finished.emit()
        

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

    def check_motion(self):
        iteration_count = 0
        max_iterations = 100  # Limit the number of iterations for debugging
        while iteration_count < max_iterations:
            if self.abort_flag:
                self.send_command('t0')
                self.motion_checked.emit("Move aborted.")
                break
            res = self.send_command('0 g r0xa0')
            val = res[2:]
            # Check 28th bit
            if val.isnumeric():
                if ((int(val)) & (1 << 27) == 0):
                    self.motion_checked.emit("Not moving or move done!\n")
                    break
                else:
                    self.motion_checked.emit("In motion\r")
            else:
                self.motion_checked.emit(f"Error: {res}. Couldn't check motion")
                break
            iteration_count += 1
            self.motion_checked.emit(f"Iteration: {iteration_count}")

        if iteration_count >= max_iterations:
            self.motion_checked.emit("Reached maximum iterations, exiting loop")

    @Slot()
    def abort_move(self):
        self.abort_flag = True
        self.send_command('t 0')
        