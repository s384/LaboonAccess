import sys, gettext, os, time
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PySide2.QtCore import QFile
from ui_add_domain import Ui_MainWindow

hosts_tmp = 'tmp/control'

class AddDomain(QMainWindow):
    def __init__(self, parent = None):
        super(AddDomain, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Conexion boton - funcion
        self.ui.btn_grabar_dominio.clicked.connect(self.agregar_dominio)
        self.ui.btn_cancelar_dominio.clicked.connect(self.cancelar)

    # funcion para agregar dominio al arbol
    def agregar_dominio(self):
        fichero = open(hosts_tmp,'a')
        texto = self.ui.txt_agregar_dominio.text()
        fichero.write(texto + "\n")
        fichero.close()
        self.close()

    def mostran(self):
        AddDomain.show(self)

    # funcion para cerrar
    def cancelar(self):
        self.close()