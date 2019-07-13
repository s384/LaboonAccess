# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import join, abspath, dirname

ruta_parental = abspath(join(dirname(__file__), 'icons', 'parental.svg'))
ruta_minus = abspath(join(dirname(__file__), 'icons', 'minus-circle.svg'))
ruta_plus = abspath(join(dirname(__file__), 'icons', 'plus-circle.svg'))
ruta_save = abspath(join(dirname(__file__), 'icons', 'save.svg'))
ruta_shield = abspath(join(dirname(__file__), 'icons', 'shield.svg'))
ruta_sunrise = abspath(join(dirname(__file__), 'icons', 'sunrise.svg'))
ruta_sunset = abspath(join(dirname(__file__), 'icons', 'sunset.svg'))
ruta_user = abspath(join(dirname(__file__), 'icons', 'user.svg'))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 512)
        Dialog.setMinimumSize(QtCore.QSize(510, 512))
        Dialog.setMaximumSize(QtCore.QSize(510, 512))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_parental),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QWidget{\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QToolTip {\n"
"    border: 2px solid #419fd9;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font-size: 20px;\n"
"}"
"QInputDialog{\n"
"    background-color: white;\n"
"}"
)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_pass = QtWidgets.QPushButton(Dialog)
        self.btn_pass.setMaximumSize(QtCore.QSize(0, 0))
        self.btn_pass.setText("")
        self.btn_pass.setObjectName("btn_pass")
        self.gridLayout.addWidget(self.btn_pass, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #419fd9;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(200, 200, 200);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 3)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setEnabled(True)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QScrollBar {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    height: 15px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"QScrollBar::handle {\n"
"    background: white;\n"
"    min-width: 20px;\n"
"}\n"
"QScrollBar::add-line {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"} \n"
"#listWidget::item:selected  {\n"
"    border: 1px solid #6a6ea9;\n"
"    color: #419fd9;\n"
"}\n"
"#listWidget::item:hover {\n"
"    border: 0px;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 8, 0, 1, 4)
        self.lbl_estado = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        self.lbl_estado.setFont(font)
        self.lbl_estado.setText("")
        self.lbl_estado.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_estado.setObjectName("lbl_estado")
        self.gridLayout.addWidget(self.lbl_estado, 9, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtWidgets.QPushButton(Dialog)
        self.btn_agregar.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_agregar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(ruta_plus), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon1)
        self.btn_agregar.setIconSize(QtCore.QSize(32, 32))
        self.btn_agregar.setShortcut("")
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_quitar = QtWidgets.QPushButton(Dialog)
        self.btn_quitar.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_quitar.setFont(font)
        self.btn_quitar.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_quitar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(ruta_minus), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quitar.setIcon(icon2)
        self.btn_quitar.setIconSize(QtCore.QSize(32, 32))
        self.btn_quitar.setObjectName("btn_quitar")
        self.horizontalLayout.addWidget(self.btn_quitar)
        self.btn_guardar = QtWidgets.QPushButton(Dialog)
        self.btn_guardar.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_guardar.setFont(font)
        self.btn_guardar.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_guardar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(ruta_save), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon3)
        self.btn_guardar.setIconSize(QtCore.QSize(32, 32))
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout.addWidget(self.btn_guardar)
        self.btn_odns = QtWidgets.QPushButton(Dialog)
        self.btn_odns.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_odns.setFont(font)
        self.btn_odns.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_odns.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(ruta_shield), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_odns.setIcon(icon4)
        self.btn_odns.setIconSize(QtCore.QSize(32, 32))
        self.btn_odns.setObjectName("btn_odns")
        self.horizontalLayout.addWidget(self.btn_odns)
        self.btn_importar = QtWidgets.QPushButton(Dialog)
        self.btn_importar.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_importar.setFont(font)
        self.btn_importar.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_importar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(ruta_sunset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_importar.setIcon(icon5)
        self.btn_importar.setIconSize(QtCore.QSize(32, 32))
        self.btn_importar.setObjectName("btn_importar")
        self.horizontalLayout.addWidget(self.btn_importar)
        self.btn_exportar = QtWidgets.QPushButton(Dialog)
        self.btn_exportar.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_exportar.setFont(font)
        self.btn_exportar.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_exportar.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(ruta_sunrise), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exportar.setIcon(icon6)
        self.btn_exportar.setIconSize(QtCore.QSize(32, 32))
        self.btn_exportar.setObjectName("btn_exportar")
        self.horizontalLayout.addWidget(self.btn_exportar)
        self.btn_acerca = QtWidgets.QPushButton(Dialog)
        self.btn_acerca.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.btn_acerca.setFont(font)
        self.btn_acerca.setStyleSheet("QPushButton{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 30px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_acerca.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(ruta_user), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_acerca.setIcon(icon7)
        self.btn_acerca.setIconSize(QtCore.QSize(32, 32))
        self.btn_acerca.setObjectName("btn_acerca")
        self.horizontalLayout.addWidget(self.btn_acerca)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Laboon Access"))
        self.btn_pass.setShortcut(_translate("Dialog", "Ctrl+B"))
        self.label_3.setText(_translate("Dialog", "deepinenespañol.org"))
        self.label.setText(_translate("Dialog", "Lista con las paginas a ser bloqueadas"))
        self.btn_agregar.setToolTip(_translate("Dialog", "Agregar una pagina ( ctrl + A )"))
        self.btn_agregar.setShortcut(_translate("Dialog", "Ctrl+A"))
        self.btn_quitar.setToolTip(_translate("Dialog", "Quitar pagina seleccionado ( supr )"))
        self.btn_quitar.setShortcut(_translate("Dialog", "Del"))
        self.btn_guardar.setToolTip(_translate("Dialog", "Guardar la lista ( ctrl + S )"))
        self.btn_guardar.setShortcut(_translate("Dialog", "Ctrl+S"))
        self.btn_odns.setToolTip(_translate("Dialog", "Activar bloqueos OpenDns ( ctrl + F )"))
        self.btn_odns.setShortcut(_translate("Dialog", "Ctrl+F"))
        self.btn_importar.setToolTip(_translate("Dialog", "Importar lista de paginas ( ctrl + O )"))
        self.btn_importar.setShortcut(_translate("Dialog", "Ctrl+O"))
        self.btn_exportar.setToolTip(_translate("Dialog", "Exportar mi llista ( ctrl + E )"))
        self.btn_exportar.setShortcut(_translate("Dialog", "Ctrl+E"))
        self.btn_acerca.setToolTip(_translate("Dialog", "Acerca de nosotros ( ctrl + D )"))
        self.btn_acerca.setShortcut(_translate("Dialog", "Ctrl+D"))


