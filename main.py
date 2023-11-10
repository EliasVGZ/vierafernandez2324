from datetime import datetime

import PyQt6
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication

import conexion
import drivers
import eventos
from venta_principal import *
import sys, var
from calendario import *
from ventana_acercade import Ui_dlgAbout
from ventana_salir import Ui_dlgSalir
from windowaux import Calendar, Salir, DlgAcerca
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self) #encargado de la interfaz
        var.calendar=Calendar()
        var.salir=Salir()
        var.dlgacercade=DlgAcerca()
        conexion.Conexion.conexion()
        conexion.Conexion.cargaprov(self)
        conexion.Conexion.mostrarDrivers()

        """ZONA DE EVENTOS DEL BOTON"""

        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendario) #abrir calendario al clickearlo
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver) #alta driver al darle click
        var.ui.btnBuscarDriver.clicked.connect(drivers.Drivers.buscarDriverLupa)


        """ ZONA DE EVENTOS DEL MENU BAR"""

        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actAcerca_de.triggered.connect(eventos.Eventos.acercade)

        """ZONA DE EVENTOS DE LA CAJAS DE TEXTO"""
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDni)  #cuando estás escribiendo y salgas, ejecuta ese evento
        var.ui.txtMovil.editingFinished.connect(drivers.Drivers.validarMovil) #valida que el movil tiene 9 digitos
        var.ui.txtMovil.editingFinished.connect(drivers.Drivers.validarSalario)

        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtApellido.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajaTexto)

        """EVENTOS DEl TOOL BAR"""
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)



        """EVENTOS DE TABLAS"""

        eventos.Eventos.resizeTabDrivers(self)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargaDriver)


        """EVENTOS COMBOBOX"""
        var.ui.cmbProvincia.currentIndexChanged.connect(conexion.Conexion.selMuni)

        """DIFERENTES EVENTOS AL CARGAR EL PROGRAMA"""
        eventos.Eventos.cargarstatusbar(self)

        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)


    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox()
        mbox.setWindowTitle('Confirmar Salida')
        mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
        mbox.setText('¿Está seguro de que desea salir?')
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
        mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

        if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            event.accept()
            #sys.exit()
        else:
            event.ignore()
            #mbox.hide()




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


