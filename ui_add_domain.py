# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_domain.ui',
# licensing of 'add_domain.ui' applies.
#
# Created: Thu May  9 20:17:43 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 150)
        MainWindow.setMinimumSize(QtCore.QSize(300, 150))
        MainWindow.setMaximumSize(QtCore.QSize(300, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_agregar_dominio = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_agregar_dominio.setGeometry(QtCore.QRect(10, 40, 271, 31))
        self.txt_agregar_dominio.setObjectName("txt_agregar_dominio")
        self.btn_grabar_dominio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_grabar_dominio.setGeometry(QtCore.QRect(30, 80, 81, 51))
        self.btn_grabar_dominio.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_grabar_dominio.setIcon(icon)
        self.btn_grabar_dominio.setIconSize(QtCore.QSize(32, 32))
        self.btn_grabar_dominio.setObjectName("btn_grabar_dominio")
        self.btn_cancelar_dominio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar_dominio.setGeometry(QtCore.QRect(180, 80, 80, 51))
        self.btn_cancelar_dominio.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/x-octagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancelar_dominio.setIcon(icon1)
        self.btn_cancelar_dominio.setIconSize(QtCore.QSize(32, 32))
        self.btn_cancelar_dominio.setObjectName("btn_cancelar_dominio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "LaboonAccess | Agregar Dominio", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Agregar Dominio", None, -1))

