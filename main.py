from datetime import datetime

import PyQt6
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication

import clientes
import conexion
import conexionClientes
import drivers
import eventos
from venta_principal import *
import sys, var
from calendario import *
from ventana_acercade import Ui_dlgAbout
from ventana_salir import Ui_dlgSalir
from windowaux import Calendar, Salir, DlgAcerca, FileDialogAbrir
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
        var.dlgabrir = FileDialogAbrir()
        conexion.Conexion.conexion()
        conexionClientes.ConexionCliente.conexion()

        conexion.Conexion.cargaprov(self)
        conexionClientes.ConexionCliente.cargarprov()

        conexion.Conexion.mostrarDrivers(self)
        conexionClientes.ConexionCliente.mostrarClientes(self)

        estado = 1
        conexion.Conexion.selectDrivers(estado)#PARA QUE AL COMENZAR EL PRO ME MUESTRE LOS DE ALTA
        conexionClientes.ConexionCliente.selectClientes(estado)


        """ZONA DE EVENTOS DEL BOTON"""

        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendario) #abrir calendario al clickearlo
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver) #alta driver al darle click
        var.ui.btnBuscarDriver.clicked.connect(drivers.Drivers.buscarDriverLupa)
        var.ui.btnModifDriver.clicked.connect(drivers.Drivers.modificarDriver)
        var.ui.btnBajaDriver.clicked.connect(drivers.Drivers.borrarDriver)

        """ZONA DE EVENTOS DEL BOTON DEL EXAMEN"""
        var.ui.btnAltaCliente.clicked.connect(clientes.Clientes.altaCliente)
        var.ui.btnBajaCliente.clicked.connect(clientes.Clientes.borrarCliente)
        var.ui.btnModifCliente.clicked.connect(clientes.Clientes.modificaCliente)


        """ ZONA DE EVENTOS DEL MENU BAR"""

        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actAcerca_de.triggered.connect(eventos.Eventos.acercade)
        var.ui.actionCrear_Copia_Seguridad.triggered.connect(eventos.Eventos.crearBackUp)#Herramienta
        var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(eventos.Eventos.restaurarBackUp)#Herramienta
        var.ui.actionExportar_Datos_xls.triggered.connect(eventos.Eventos.exportarDatosXls)#Herramienta
        var.ui.actionImportar_Datos_XLS.triggered.connect(eventos.Eventos.importardatosxls)

        """ZONA DE EVENTOS DE LA CAJAS DE TEXTO"""
        var.ui.txtDni.editingFinished.connect(lambda: drivers.Drivers.validarDni(var.ui.txtDni.text()))  #cuando estás escribiendo y salgas, ejecuta ese evento
        var.ui.txtMovil.editingFinished.connect(drivers.Drivers.validarMovil) #valida que el movil tiene 9 digitos
        var.ui.txtMovil.editingFinished.connect(drivers.Drivers.validarSalario)

        """ZONA DE EVENTOS DE LA CAJAS DE TEXTO del EXAMEN"""
        var.ui.txtTelefono.editingFinished.connect(clientes.Clientes.validarTelefono)
        var.ui.txtDni2.editingFinished.connect(lambda: clientes.Clientes.validarDni(var.ui.txtDni2.text()))




        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtApellido.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.formatCajaTexto)

        var.ui.txtDni2.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txt_razonSocial.editingFinished.connect(eventos.Eventos.formatCajaTexto)
        var.ui.txtDireccionCliente.editingFinished.connect(eventos.Eventos.formatCajaTexto)

        """EVENTOS DEl TOOL BAR"""
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)
        var.ui.actioncrearCopia.triggered.connect(eventos.Eventos.crearBackUp)#llamada al icono
        var.ui.actionrestaurarCopia.triggered.connect(eventos.Eventos.restaurarBackUp)#llamada al icono



        """EVENTOS DE TABLAS"""

        eventos.Eventos.resizeTabDrivers(self)
        var.ui.tabClientes.clicked.connect(clientes.Clientes.cargaCliente)
        var.ui.tabDrivers.clicked.connect(drivers.Drivers.cargaDriver)


        """EVENTOS COMBOBOX"""
        var.ui.cmbProvincia.currentIndexChanged.connect(conexion.Conexion.selMuni)
        var.ui.buttonGroup.buttonClicked.connect(drivers.Drivers.selEstado)

        var.ui.cmbProvinciaCliente.currentIndexChanged.connect(conexionClientes.ConexionCliente.selMuni)

        """DIFERENTES EVENTOS AL CARGAR EL PROGRAMA"""
        eventos.Eventos.cargarstatusbar(self)

        """
        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(eventos.Eventos.selEstado)"""


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


