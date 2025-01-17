# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations


from PySide6.QtCore import QIODeviceBase, Slot
from PySide6.QtWidgets import QLabel, QMainWindow, QMessageBox, QApplication


import sys

from motionWindow import MainWindow


"""PySide6 port of the serialport/terminal example from Qt v6.x"""

if __name__ == "__main__":

    

    a = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec())

