#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QFileDialog
from PySide2.QtCore import QFile, QEvent
from ui_view import Ui_MainWindow
from add_domain import AddDomain

# Variables
user = os.environ.get('SUDO_USER')
hosts = '/etc/hosts'
hosts_tmp = 'tmp/control'
hosts_save = 'tmp/hosts'
hosts_exp = 'tmp/control.tcp'

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		# Conexion boton - funcion
		self.ui.btn_agregar.clicked.connect(self.agergar_dominio)
		self.ui.btn_quitar.clicked.connect(self.quitar_dominio)
		self.ui.btn_guardar.clicked.connect(self.guardar_dominio)
		self.ui.btn_importar.clicked.connect(self.importar_dominio)
		self.ui.btn_exportar.clicked.connect(self.exportar_dominio)
		self.ui.btn_acerca.clicked.connect(self.acerca_de)
		# Cargamos los dominios
		self.installEventFilter(self)
		self.cuenta_1 = 0
		self.cuenta_2 = 0

	def eventFilter(self, object, event):
		if event.type() == QEvent.WindowActivate:
			self.cargar_dominios()
			if self.cuenta_2 != self.cuenta_1:
				self.ui.lbl_estado.setText("Dominios agregado")
				self.ui.lbl_estado.setStyleSheet("color: green")
		return False

	# Carga incial de los dominios
	def cargar_dominios(self):
		try:
			# Limpiamos la tabla
			rows = self.ui.tableWidget.rowCount()	
			if rows != 0:
				for x in range(0, rows+1):
					self.ui.tableWidget.removeRow(rows)
					rows = rows - 1

			# Leemos los datos y los agregamos al archivo
			fichero = open(hosts_tmp,'r')
			r = 0
			for line in fichero:
				line = str.strip(line)
				self.ui.tableWidget.insertRow(r)
				self.ui.tableWidget.setItem(r, 0, QTableWidgetItem(line))
				r = r+1
			fichero.close()
			self.cuenta_1 = r
			self.ui.lbl_estado.setText("Dominios cargados")
			self.ui.lbl_estado.setStyleSheet("color: green")
		except:
			self.ui.lbl_estado.setText("Error al cargar los dominios")
			self.ui.lbl_estado.setStyleSheet("color: orange")

	# funcion para agregar dominio
	def agergar_dominio(self):
		self.cuenta_2 = self.cuenta_1
		self.agregar = AddDomain()
		self.agregar.mostran()

	# funcion quitar dominio
	def quitar_dominio(self):
		try:
			delete = int(self.ui.tableWidget.currentRow())
			self.ui.tableWidget.removeRow(delete)
			
			fichero = open(hosts_tmp, 'w')
			fichero.write("")
			fichero.close()

			fichero = open(hosts_tmp, 'a')
			rows = self.ui.tableWidget.rowCount()
			if rows != 0:
				for x in range(0, rows):
					item = self.ui.tableWidget.item(x,0)
					fichero.write(item.text() + "\n")
			fichero.close()

			self.ui.lbl_estado.setText("Dominio eliminado")
			self.ui.lbl_estado.setStyleSheet("color: blue")
		except:
			self.ui.lbl_estado.setText("Error al eliminar el dominio")
			self.ui.lbl_estado.setStyleSheet("color: orange")

	def guardar_dominio(self):
		try:
			fichero = open(hosts, 'a')
			rows = self.ui.tableWidget.rowCount()
			for x in range(0, rows):
				item = self.ui.tableWidget.item(x,0)
				if item.text() != None:
					fichero.write("\n" + '127.0.0.1 ' + item.text())
			fichero.close()
			
			self.ui.lbl_estado.setText("Dominios guardados")
			self.ui.lbl_estado.setStyleSheet("color: green")
		except:
			self.ui.lbl_estado.setText("Error al guardar los dominio")
			self.ui.lbl_estado.setStyleSheet("color: orange")

	def importar_dominio(self):
		print("Say import")

	def exportar_dominio(self):
		try:
			ruta_home = os.environ['HOME']
			ruta = QFileDialog.getExistingDirectory(self, "Donde desea guardar el archivo?", ruta_home,
													  QFileDialog.ShowDirsOnly)
			if ruta:
				fichero = open(hosts_exp, 'w')
				fichero.write("")
				fichero.close()

				fichero = open(hosts_exp, 'a')
				rows = self.ui.tableWidget.rowCount()
				for x in range(0, (rows-1)):
					item = self.ui.tableWidget.item(x,0)
					if item.text() != None:
						fichero.write(item.text() + "\n")
				fichero.close()
				os.system('cp ' + hosts_exp + ' ' + ruta + '/hosts')
				self.ui.lbl_estado.setText("Archivo exportado")
				self.ui.lbl_estado.setStyleSheet("color: green")
		except:
			self.ui.lbl_estado.setText("Ha ocurrido un error")
			self.ui.lbl_estado.setStyleSheet("color: red")

	def acerca_de(self):
		print("Say hello")


if __name__ == "__main__":
	if not os.path.exists('/etc/hosts.tcp.backup'):
		os.system('sudo cp /etc/hosts /etc/hosts.tcp.backup')
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())