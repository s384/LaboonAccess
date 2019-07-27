#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QDesktopWidget, QDialog
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QPushButton

from maing import Ui_Dialog
from nosotros import Ui_Form as nosotrosGui

global password
password = False
global contra

class windows(QWidget):
  def __init__(self):
    super(windows, self).__init__()
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
    # Conexion boton - funcion
    self.ui.btn_agregar.clicked.connect(self.agregar_dominio)
    self.ui.btn_quitar.clicked.connect(self.quitar_dominio)
    self.ui.btn_guardar.clicked.connect(self.guardar_dominio)
    self.ui.btn_importar.clicked.connect(self.importar_dominio)
    self.ui.btn_exportar.clicked.connect(self.exportar_dominio)
    self.ui.btn_acerca.clicked.connect(self.acerca_de)
    self.ui.btn_pass.clicked.connect(self.password)
    self.ui.btn_odns.clicked.connect(self.open_dns)
    # Personalizando Componentes
    font = QFont()
    font.setFamily("Akaash")
    font.setPointSize(12)
    font.setBold(False)
    font.setWeight(50)
    self.ui.lbl_estado.setFont(font)
    self.mensaje("Bienvenido a Laboon Access, vamos a bloquear paginas!!!", "green")
    self.ui.listWidget.setGridSize(QSize(0, 20))
    # Cargar dominios
    self.center()
    self.cargar_dominios()
    if password:
      self.bloque_control(False)

  def center(self):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

  def mensaje(self, text, color):
    self.ui.lbl_estado.setText(text)
    self.ui.lbl_estado.setStyleSheet("color: " + color)

  def controles(self):
    if self.ui.listWidget.count() == 0:
      self.ui.btn_quitar.setEnabled(False)
      self.ui.btn_exportar.setEnabled(False)
    else:
      self.ui.btn_quitar.setEnabled(True)
      self.ui.btn_exportar.setEnabled(True)

  def bloque_control(self, boolean):
    self.ui.btn_agregar.setEnabled(boolean)
    self.ui.btn_quitar.setEnabled(boolean)
    self.ui.btn_guardar.setEnabled(boolean)
    self.ui.btn_odns.setEnabled(boolean)
    self.ui.btn_exportar.setEnabled(boolean)
    self.ui.btn_importar.setEnabled(boolean)
    self.ui.listWidget.setEnabled(boolean)

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
    item, acept = QInputDialog.getText(
        self, "Laboon Access", "Ingrese la pagina que desea bloquear")
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
      self.mensaje("Solo falta guardar los cambios", "green")
    self.controles()

  def quitar_dominio(self):
    fila = self.ui.listWidget.currentRow()
    item = self.ui.listWidget.takeItem(fila)
    self.mensaje("Dominio eliminado: " + item.text(), "red")
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

      self.mensaje("Paginas agregadas correctamente", "green")
      os.system("sudo /etc/init.d/networking restart")
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
      self.mensaje("Archivo importado, no olvide guardar los cambios", "green")

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

      self.mensaje("Archivo exportado correctamente", "green")

  def acerca_de(self):
    widget = QDialog(self)
    ui=nosotrosGui()
    ui.setupUi(widget)
    widget.exec_()

  def open_dns(self):
    """
    if not laboon:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("¿Desea activar el OpenDns?")
      msg.setInformativeText(
          "Ayuda a hacer de la web un lugar más seguro.")
      msg.setWindowTitle("LaboonAccess OpenDns")
      msg.setDetailedText("IMPORTANTE: Este servicio no esta vinculado con Laboon Access\n"
                          "Con el filtro de protección preconfigurado, puede "
                          "proteger a su familia contra el contenido para adultos "
                          "y más. Es la forma más fácil de agregar controles de "
                          "filtrado parental y de contenido.")
      msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

      retval = msg.exec_()
      if retval == QMessageBox.Yes:

        self.mensaje("Bloqueo de OpenDns, activado", "green")

    else:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)
      msg.setWindowTitle("LaboonAccess OpenDns")
      msg.setText("¿Desea desactivar OpenDns?")
      msg.setInformativeText("Esto le permitira navegar libremente por internet")
      msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
      retval = msg.exec_()
      
      self.mensaje("Bloqueo de OpenDns, deshabilitado", "#419fd9")
    """
    os.system("sudo /etc/init.d/networking restart")

  def password(self):
    global password
    if password == True:
      item, acept = QInputDialog.getText(
          self, "Laboon Access", "Contraseña: ", QLineEdit.Password)
      if contra == self.encrypt(item):
        msgBox = QMessageBox()
        msgBox.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        msgBox.setStyleSheet("QMessageBox { font: bold 14px; padding: 6px;"
                            "background-color: white; min-width: 10em;"
          "}"
        )
        msgBox.setText('Que accion desea realizar??')
        btnYes = QPushButton('Desactivar proteccion')
        msgBox.addButton(btnYes, QMessageBox.ActionRole)
        btnNo = QPushButton('Eliminar contraseña')
        msgBox.addButton(btnNo, QMessageBox.ActionRole)
        btnCan = QPushButton('Cancelar')
        msgBox.addButton(btnCan, QMessageBox.NoRole)
        btnYes.setStyleSheet("QPushButton {padding: 4px; margin: 6px;"
                            "border: 2px solid green; border-radius: 5px;}"
                            "QPushButton:hover{ border: 2px solid #419fd9;}")
        btnNo.setStyleSheet("QPushButton {padding: 4px; margin: 6px;"
                            "border: 2px solid red; border-radius: 5px;}"
                            "QPushButton:hover{ border: 2px solid #419fd9;}")
        btnCan.setStyleSheet("QPushButton {padding: 4px; margin: 6px;"
                            "border: 2px solid orange; border-radius: 5px;}"
                            "QPushButton:hover{ border: 2px solid #419fd9;}")
        msgBox.exec_()
        ret = msgBox.clickedButton()
        if ret == btnYes:
          self.bloque_control(True)
        elif ret == btnNo:
          os.system('rm - r /etc/labac.pas')
          self.ui.lbl_estado.setText("Contraseña eliminada")
          self.ui.lbl_estado.setStyleSheet("color: red")
          password = False
        else:
          return
    else:
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("¿Desea establecer una contraseña de seguridad?")
      msg.setInformativeText("Esta contraseña impedira el uso del programa")
      msg.setWindowTitle("LaboonAccess Password")
      msg.setDetailedText("Esta contraseña impedira que se agregen, quiten o guarde "
        "cambios en la lista de paginas, a no ser que ingrese la contraseña")
      msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

      retval = msg.exec_()
      if retval == QMessageBox.Yes:
        file = open('/etc/labac.pas', 'w')
        item = ""
        item2 = " "
        while item != item2:
          item, acept = QInputDialog.getText(self, "Laboon Access", "Ingrese una contraseña", QLineEdit.Password)
          item2, acept2 = QInputDialog.getText(self, "Laboon Access", "Repita la contraseña", QLineEdit.Password)
          if item == item2:
            file.write(self.encrypt(item))
            file.close()
            self.mensaje("Contraseña establecida", "green")
            password = True
  
  def encrypt(self, message):
    newS = ''
    for car in message:
        newS = newS+chr(ord(car)+2)
    return newS

if __name__ == '__main__':
  if not os.path.exists('/etc/hosts.la.backup'):
    os.system('cp /etc/hosts /etc/hosts.la.backup')
  if os.path.exists('/etc/labac.pas'):
    archivo = open('/etc/labac.pas', 'r')
    contra = archivo.readline()
    password = True
  app = QApplication(sys.argv)
  win = windows()
  win.show()
  sys.exit(app.exec_())
