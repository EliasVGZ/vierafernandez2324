from datetime import datetime

from PyQt6 import QtWidgets

import drivers
import eventos
from venta_principal import *
import sys, var
from calendario import *
from ventana_acercade import Ui_dlgAbout
from ventana_salir import Ui_dlgSalir


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self) #encargado de la interfaz
        var.calendar=Calendar()
        var.salir=Salir()
        var.dlgacercade=DlgAcerca()



        """ZONA DE EVENTOS DEL BOTON"""

        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendario)


        """ ZONA DE EVENTOS DEL MENU BAR"""

        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actAcerca_de.triggered.connect(eventos.Eventos.acercade)

        """ZONA DE EVENTOS DE LA CAJAS DE TEXTO"""
        var.ui.txtDni.editingFinished.connect(drivers.Drivers.validarDni)  #cuando estás escribiendo y salgas, ejecuta ese evento

        """EVENTOS DEl TOOL BAR"""
        var.ui.actionbarSalir.triggered.connect(eventos.Eventos.salir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)




class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self). __init__()
        var.calendar = Ui_Calendario()
        var.calendar.setupUi(self)
        dia= datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.ventanaCalendario.setSelectedDate((QtCore.QDate(ano,mes,dia)))
        var.calendar.ventanaCalendario.clicked.connect(drivers.Drivers.cargarFecha)


class Salir(QtWidgets.QDialog):
    def __init__(self):
        super(Salir, self). __init__()
        var.salir = Ui_dlgSalir()
        var.salir.setupUi(self)
        var.salir.btnAceptar.clicked.connect(self.aceptar)
        var.salir.btnCancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        sys.exit()  # Cierra la aplicación

    def cancelar(self):
        self.hide()  # Oculta el cuadro de diálogo


class DlgAcerca(QtWidgets.QDialog):
    def __init__(self):
        super(DlgAcerca, self).__init__()
        var.dlgacerca = Ui_dlgAbout()
        var.dlgacerca.setupUi(self)
        var.dlgacerca.btnAceptar.clicked.connect(self.aceptar)
    def aceptar(self):
        self.hide()  # Oculta el cuadro de diálogo

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


