# Form implementation generated from reading ui file '.\templates\ventana_acercade.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_dlgAbout(object):
    def setupUi(self, dlgAbout):
        dlgAbout.setObjectName("dlgAbout")
        dlgAbout.resize(390, 385)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/travel_car_BMV_1741.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        dlgAbout.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(dlgAbout)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=dlgAbout)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lblImagen = QtWidgets.QLabel(parent=self.frame)
        self.lblImagen.setGeometry(QtCore.QRect(10, 10, 96, 96))
        self.lblImagen.setText("")
        self.lblImagen.setPixmap(QtGui.QPixmap(".\\templates\\../IMG/travel_car_BMV_1741.png"))
        self.lblImagen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblImagen.setObjectName("lblImagen")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(112, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(112, 44, 58, 16))
        self.label_2.setObjectName("label_2")
        self.lblVersion = QtWidgets.QLabel(parent=self.frame)
        self.lblVersion.setGeometry(QtCore.QRect(112, 78, 106, 16))
        self.lblVersion.setObjectName("lblVersion")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(81, 127, 271, 121))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.btnAceptar = QtWidgets.QPushButton(parent=dlgAbout)
        self.btnAceptar.setObjectName("btnAceptar")
        self.gridLayout.addWidget(self.btnAceptar, 1, 0, 1, 1)

        self.retranslateUi(dlgAbout)
        QtCore.QMetaObject.connectSlotsByName(dlgAbout)

    def retranslateUi(self, dlgAbout):
        _translate = QtCore.QCoreApplication.translate
        dlgAbout.setWindowTitle(_translate("dlgAbout", "Acerca de..."))
        self.label.setText(_translate("dlgAbout", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">CT</span></p></body></html>"))
        self.label_2.setText(_translate("dlgAbout", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">  CAR TEIS</span></p></body></html>"))
        self.lblVersion.setText(_translate("dlgAbout", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Version 0.0.1 RC</span></p></body></html>"))
        self.label_4.setText(_translate("dlgAbout", "<html><head/><body><p>06/10/2023 - Elias Viera Fernadez</p><p>Proyecto INTERFACES GRAFICAS</p><p>Desarrollo Aplicaciones Web</p><p>2023 - IES Teis</p></body></html>"))
        self.btnAceptar.setText(_translate("dlgAbout", "ACEPTAR"))
