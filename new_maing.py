# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 480)
        Form.setMinimumSize(QtCore.QSize(542, 480))
        Form.setMaximumSize(QtCore.QSize(542, 480))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(11)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/control parental.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtWidgets.QPushButton(Form)
        self.btn_agregar.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_agregar.setStyleSheet("#btn_agregar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_agregar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_agregar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/plus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon1)
        self.btn_agregar.setIconSize(QtCore.QSize(48, 48))
        self.btn_agregar.setShortcut("")
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_quitar = QtWidgets.QPushButton(Form)
        self.btn_quitar.setMinimumSize(QtCore.QSize(50, 80))
        self.btn_quitar.setStyleSheet("#btn_quitar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_quitar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_quitar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/minus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_quitar.setIcon(icon2)
        self.btn_quitar.setIconSize(QtCore.QSize(48, 48))
        self.btn_quitar.setObjectName("btn_quitar")
        self.horizontalLayout.addWidget(self.btn_quitar)
        self.btn_guardar = QtWidgets.QPushButton(Form)
        self.btn_guardar.setMinimumSize(QtCore.QSize(50, 80))
        self.btn_guardar.setStyleSheet("#btn_guardar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_guardar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_guardar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon3)
        self.btn_guardar.setIconSize(QtCore.QSize(48, 48))
        self.btn_guardar.setObjectName("btn_guardar")
        self.horizontalLayout.addWidget(self.btn_guardar)
        self.btn_importar = QtWidgets.QPushButton(Form)
        self.btn_importar.setMinimumSize(QtCore.QSize(50, 80))
        self.btn_importar.setStyleSheet("#btn_importar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_importar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_importar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/sunset.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_importar.setIcon(icon4)
        self.btn_importar.setIconSize(QtCore.QSize(48, 48))
        self.btn_importar.setObjectName("btn_importar")
        self.horizontalLayout.addWidget(self.btn_importar)
        self.btn_exportar = QtWidgets.QPushButton(Form)
        self.btn_exportar.setMinimumSize(QtCore.QSize(50, 80))
        self.btn_exportar.setStyleSheet("#btn_exportar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_exportar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_exportar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/sunrise.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exportar.setIcon(icon5)
        self.btn_exportar.setIconSize(QtCore.QSize(48, 48))
        self.btn_exportar.setObjectName("btn_exportar")
        self.horizontalLayout.addWidget(self.btn_exportar)
        self.btn_acerca = QtWidgets.QPushButton(Form)
        self.btn_acerca.setMinimumSize(QtCore.QSize(50, 80))
        self.btn_acerca.setStyleSheet("#btn_acerca {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"}\n"
"#btn_acerca:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 40px;\n"
"    background-color: #419fd9;\n"
"}")
        self.btn_acerca.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_acerca.setIcon(icon6)
        self.btn_acerca.setIconSize(QtCore.QSize(48, 48))
        self.btn_acerca.setObjectName("btn_acerca")
        self.horizontalLayout.addWidget(self.btn_acerca)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(200, 200, 200);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setEnabled(True)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Akaash")
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: rgb(103, 103, 103);")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.lbl_estado = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lbl_estado.setFont(font)
        self.lbl_estado.setStyleSheet("color: rgb(200, 200, 200);")
        self.lbl_estado.setText("")
        self.lbl_estado.setObjectName("lbl_estado")
        self.verticalLayout.addWidget(self.lbl_estado)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LaboonAccess"))
        self.btn_agregar.setToolTip(_translate("Form", "Agregar una pagina ( ctrl + A )"))
        self.btn_agregar.setShortcut(_translate("Form", "Ctrl+A"))
        self.btn_quitar.setToolTip(_translate("Form", "Quitar pagina seleccionado ( supr )"))
        self.btn_quitar.setShortcut(_translate("Form", "Del"))
        self.btn_guardar.setToolTip(_translate("Form", "Guardar la lista ( ctrl + S )"))
        self.btn_guardar.setShortcut(_translate("Form", "Ctrl+S"))
        self.btn_importar.setToolTip(_translate("Form", "Importar lista de paginas ( ctrl + O )"))
        self.btn_importar.setShortcut(_translate("Form", "Ctrl+O"))
        self.btn_exportar.setToolTip(_translate("Form", "Exportar mi llista ( ctrl + E )"))
        self.btn_exportar.setShortcut(_translate("Form", "Ctrl+E"))
        self.btn_acerca.setToolTip(_translate("Form", "Acerca de nosotros ( ctrl + D )"))
        self.btn_acerca.setShortcut(_translate("Form", "Ctrl+D"))
        self.label.setText(_translate("Form", "Lista con las paginas a ser bloqueadas"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
