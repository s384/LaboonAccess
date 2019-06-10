#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QDesktopWidget

from new_maing import Ui_Form


class windows(QWidget):
	def __init__(self):
		super(windows, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.la_exist = False
		# Conexion boton - funcion
		self.ui.btn_agregar.clicked.connect(self.agregar_dominio)
		self.ui.btn_quitar.clicked.connect(self.quitar_dominio)
		self.ui.btn_guardar.clicked.connect(self.guardar_dominio)
		self.ui.btn_importar.clicked.connect(self.importar_dominio)
		self.ui.btn_exportar.clicked.connect(self.exportar_dominio)
		self.ui.btn_acerca.clicked.connect(self.acerca_de)
		font = QFont()
		font.setFamily("Akaash")
		font.setPointSize(15)
		font.setBold(False)
		font.setWeight(50)
		self.ui.lbl_estado.setFont(font)
		self.ui.lbl_estado.setText("Bienvenido a Laboon Access, vamos a bloquear paginas!!!")
		self.ui.lbl_estado.setStyleSheet("color: green")
		self.center()
		self.cargar_dominios()

	def center(self):
				
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def cargar_dominios(self):
		# Abrimos el archivo para contar el total de filas
		archivo = open('/etc/hosts.la.backup', 'r')
		fila = self.ui.listWidget.currentRow()
		total = 0
		for line in archivo:
			total += 1
		archivo.close()
		# Contamos las filas hasta Laboon Access
		archivo = open('/etc/hosts.la.backup', 'r')
		laboon = 0
		for line in archivo:
			laboon += 1
			if 'LaboonAccess' in line:
				self.la_exist = True
				break
		# Iniciamos desde nuestros registros		
		paginas = archivo.readlines()
		for x in paginas:
			# Dividimos el dominio y la pagina
			if x != "\n":
				dominio, page = x.split(" ")
				# Partimos para quitar el www
				parts = page.split('.')
				if parts[0] == 'www':
					pagina = '.'.join(parts[1:])
				else:
					pagina = '.'.join(parts[0:])
				# Agregamos la pagina a la lista
				self.ui.listWidget.insertItem(fila, pagina)
		archivo.close()

	def agregar_dominio(self):
		fila = self.ui.listWidget.currentRow()
		item, acept = QInputDialog.getText(self, "Laboon Access", "Ingrese la pagina que desea bloquear")
		if acept and item != "":
			parts = item.split(".")
			if parts[0] == 'www':
				pagina = '.'.join(parts[1:])
			else:
				pagina = '.'.join(parts[0:])
			self.ui.listWidget.insertItem(fila, pagina.lower())

		if self.ui.listWidget.count() != 0:
			self.ui.btn_quitar.setEnabled(True)
		

	def quitar_dominio(self):
		fila = self.ui.listWidget.currentRow()
		item = self.ui.listWidget.takeItem(fila)
		del item
		if self.ui.listWidget.count() == 0:
			self.ui.btn_quitar.setEnabled(False)

	def guardar_dominio(self):
		try:
			archivo = open('/etc/hosts.la.backup', 'r')
			# Contamos las filas hasta Laboon Access
			archivo = open('/etc/hosts.la.backup', 'r')
			texto = []
			for line in archivo:
				if 'LaboonAccess' not in line:
					texto.append(line)
				else:
					break
			archivo.close()

				
			archivo = open('/etc/hosts.la.backup', 'w')
	
			for line in texto:
				archivo.write(line)
	
			if not self.la_exist:
				archivo.write("#_Paginas bloqueadas por LaboonAccess \n")
	
			cuenta = self.ui.listWidget.count()
			for x in range(0, cuenta):
				fila = self.ui.listWidget.item(x)
				fila = "127.0.0.1 " + str(fila.text())
				archivo.write(fila + "\n")
				#os.system('echo "' + fila + '" >> /etc/hosts.la.backup')
			self.ui.lbl_estado.setText("Paginas agregadas correctamente, cuando reinicie esto funcionara")
			self.ui.lbl_estado.setStyleSheet("color: green")
		except Exception as e:
			raise e

	def importar_dominio(self):
		print("Importar")

	def exportar_dominio(self):
		print("Exportar")

	def acerca_de(self):
		print("Acerca de")
		
if __name__ == '__main__':
	if not os.path.exists('/etc/hosts.la.backup'):
		os.system('sudo cp /etc/hosts /etc/hosts.la.backup')
	app = QApplication(sys.argv)
	win = windows()
	win.show()
	sys.exit(app.exec_())