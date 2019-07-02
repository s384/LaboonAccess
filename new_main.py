#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QDesktopWidget, QDialog
from PyQt5.QtWidgets import QFileDialog

from new_maing import Ui_Form
from nosotros import Ui_Form as nosotrosGui

class windows(QWidget):
  def __init__(self):
    super(windows, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    # Conexion boton - funcion
    self.ui.btn_agregar.clicked.connect(self.agregar_dominio)
    self.ui.btn_quitar.clicked.connect(self.quitar_dominio)
    self.ui.btn_guardar.clicked.connect(self.guardar_dominio)
    self.ui.btn_importar.clicked.connect(self.importar_dominio)
    self.ui.btn_exportar.clicked.connect(self.exportar_dominio)
    self.ui.btn_acerca.clicked.connect(self.acerca_de)
    self.ui.btn_pass.clicked.connect(self.password)
    # Personalizando Componentes
    font = QFont()
    font.setFamily("Akaash")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    self.ui.lbl_estado.setFont(font)
    self.ui.lbl_estado.setText("Bienvenido a Laboon Access, vamos a bloquear paginas!!!")
    self.ui.lbl_estado.setStyleSheet("color: green")
    self.ui.listWidget.setGridSize(QSize(0, 20))
    # Cargar dominios
    self.center()
    self.cargar_dominios()

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def controles(self):
    if self.ui.listWidget.count() == 0:
      self.ui.btn_quitar.setEnabled(False)
      self.ui.btn_exportar.setEnabled(False)
    else:
      self.ui.btn_quitar.setEnabled(True)
      self.ui.btn_exportar.setEnabled(True)

  def cargar_dominios(self):
    # Abrimos el archivo para contar el total de filas
    archivo = open('/etc/hosts', 'r')
    total = 0
    for line in archivo:
      total += 1
    archivo.close()
    # Contamos las filas hasta Laboon Access
    archivo = open('/etc/hosts', 'r')
    laboon = 0
    for line in archivo:
      laboon += 1
      if 'LaboonAccess' in line:
        break
    # Iniciamos desde nuestros registros    
    paginas = archivo.readlines()
    contador = 0
    for x in paginas:
      contador += 1
      if 'alternativo' in x:
        break
      # Dividimos el dominio y la pagina
      if x != "\n":
        division = x.split("\n")
        dominio, page = division[0].split(" ")
        # Partimos para quitar el www
        parts = page.split('.')
        if parts[0] == 'www':
          pagina = '.'.join(parts[1:])
        else:
          pagina = '.'.join(parts[0:])

        if "\n" in pagina:
            page = pagina.split("\n")
            pagina = "".join(page[0:1])

        # Agregamos la pagina a la lista
        self.ui.listWidget.insertItem(contador, pagina)
    archivo.close()
    self.controles()

  def agregar_dominio(self):
    fila = int(self.ui.listWidget.count()) + 1
    item, acept = QInputDialog.getText(self, "Laboon Access", "Ingrese la pagina que desea bloquear")
    if acept and item != "":
      part = item.split("//")

      if part[0] == 'http:' or part[0] == 'https:':
        parts = part[1].split(".")
      else:
        parts = item.split(".")

      if parts[0] == 'www' or parts[0] == 'es' or parts[0] == 'm':
        pagina = '.'.join(parts[1:])
      else:
        pagina = '.'.join(parts[0:])
      
      if "/" in pagina:
        page = pagina.split("/")
        pagina = "".join(page[0:1])

      if "\n" in pagina:
            page = pagina.split("\n")
            pagina = "".join(page[0:1])

      self.ui.listWidget.insertItem(fila, pagina.lower())
      self.ui.lbl_estado.setText("Solo falta guardar los cambios")
      self.ui.lbl_estado.setStyleSheet("color: green")
    self.controles()

  def quitar_dominio(self):
    fila = self.ui.listWidget.currentRow()
    item = self.ui.listWidget.takeItem(fila)
    self.ui.lbl_estado.setText("dominio eliminado: " + item.text())
    self.ui.lbl_estado.setStyleSheet("color: red")
    del item
    self.controles()

  def guardar_dominio(self):
    try:
      # Contamos las filas hasta Laboon Access
      archivo = open('/etc/hosts', 'r')
      texto = []
      for line in archivo:
        if line == "\n":
          pass
        else:
          if 'LaboonAccess' not in line:
            texto.append(line)
          else:
            break
      archivo.close()
        
      archivo = open('/etc/hosts', 'w')
  
      for line in texto:
        archivo.write(line)
  
      archivo.write("\n#_Paginas bloqueadas por LaboonAccess\n")
  
      cuenta = self.ui.listWidget.count()
      lista_www = []
      for x in range(0, cuenta):
        fila = self.ui.listWidget.item(x)
        if fila.text() != "\n":
          texto = str(fila.text())
          lista_www.append("0.0.0.0 www." + texto)
          fila = "0.0.0.0 " + texto
          archivo.write(fila + "\n")

      archivo.write("\n\n#_Bloqueo alternativo con www LaboonAccess\n")
      for line in lista_www:
        archivo.write(line+"\n")  

      self.ui.lbl_estado.setText("Paginas agregadas correctamente, no olvides reiniciar")
      self.ui.lbl_estado.setStyleSheet("color: green")
    except Exception as e:
      raise e

  def importar_dominio(self):
    file, _ = QFileDialog.getOpenFileName(self, "Importar lista de paginas", "", 
                                      "Archivos de texto (*.txt)")
    if file != "":
      archivo = open(file, 'r')
      paginas = archivo.readlines()
      fila = self.ui.listWidget.count()
      for x in paginas:
        if x != "\n":
          # Partimos para quitar el www
          part = x.split("//")
          if part[0] == 'http:' or part[0] == 'https:':
            parts = part[1].split(".")
          else:
            parts = x.split(".")

          if parts[0] == 'www' or parts[0] == 'es' or parts[0] == 'm':
            pagina = '.'.join(parts[1:])
          else:
            pagina = '.'.join(parts[0:])
          
          if "/" in pagina:
            page = pagina.split("/")
            pagina = "".join(page[0:1])

          if "\n" in pagina:
            page = pagina.split("\n")
            pagina = "".join(page[0:1])

          # Agregamos la pagina a la lista
          fila += 1
          self.ui.listWidget.insertItem(fila, pagina.lower())
      self.ui.lbl_estado.setText("Archivo importado, no olvide guardar los cambios")
      self.ui.lbl_estado.setStyleSheet("color: green")

  def exportar_dominio(self):
    file = str(QFileDialog.getExistingDirectory(self, "Donde desea guardar el archivo?"))
    if file != "":
      archivo = open(file + '/LaboonAccess.txt', 'w')
      cuenta = self.ui.listWidget.count()

      for x in range(0, cuenta):
        fila = self.ui.listWidget.item(x)
        if fila.text() != "":
          archivo.write(str(fila.text())+"\n")
      archivo.close()

      self.ui.lbl_estado.setText("Archivo exportado correctamente")
      self.ui.lbl_estado.setStyleSheet("color: green")

  def acerca_de(self):
    widget = QDialog(self)
    ui=nosotrosGui()
    ui.setupUi(widget)
    widget.exec_()

  def password(self):
    print("Funcion oculta para el bloqueo por pass")
    
if __name__ == '__main__':
  if not os.path.exists('/etc/hosts.la.backup'):
    os.system('cp /etc/hosts /etc/hosts.la.backup')
  app = QApplication(sys.argv)
  win = windows()
  win.show()
  sys.exit(app.exec_())