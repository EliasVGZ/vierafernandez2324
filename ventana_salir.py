# Form implementation generated from reading ui file 'ventana_salir.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgSalir(object):
    def setupUi(self, dlgSalir):
        dlgSalir.setObjectName("dlgSalir")
        dlgSalir.resize(300, 250)
        dlgSalir.setMinimumSize(QtCore.QSize(300, 250))
        dlgSalir.setMaximumSize(QtCore.QSize(300, 250))
        dlgSalir.setSizeGripEnabled(True)
        dlgSalir.setModal(True)
        self.label = QtWidgets.QLabel(parent=dlgSalir)
        self.label.setGeometry(QtCore.QRect(80, 20, 121, 31))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btnAceptar = QtWidgets.QPushButton(parent=dlgSalir)
        self.btnAceptar.setGeometry(QtCore.QRect(20, 190, 101, 41))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnCancelar = QtWidgets.QPushButton(parent=dlgSalir)
        self.btnCancelar.setGeometry(QtCore.QRect(170, 190, 101, 41))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_2 = QtWidgets.QLabel(parent=dlgSalir)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 131, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Documents/Desenvolvemento Interfaces/imagenes/imagen_salir.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(dlgSalir)
        QtCore.QMetaObject.connectSlotsByName(dlgSalir)

    def retranslateUi(self, dlgSalir):
        _translate = QtCore.QCoreApplication.translate
        dlgSalir.setWindowTitle(_translate("dlgSalir", "Salir"))
        self.label.setText(_translate("dlgSalir", "<html><head/><body><p><span style=\" font-weight:600;\">¿Desea salir?</span></p></body></html>"))
        self.btnAceptar.setText(_translate("dlgSalir", "Aceptar"))
        self.btnCancelar.setText(_translate("dlgSalir", "Cancelar"))
