#!/usr/bin/python3
# Ejecutar con python3 run.py
import subprocess, os, sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QDesktopWidget, QDialog
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QPushButton


def resolver_ruta(ruta_relativa):
    global ruta
    if hasattr(sys, '_MEIPASS'):
        ruta = sys._MEIPASS
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

subprocess.call(['gksudo', 'python3 ' + resolver_ruta('new_main.py')])