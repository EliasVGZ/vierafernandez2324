from datetime import datetime

import PyQt6
from PyQt6 import QtWidgets

import drivers
import eventos
from venta_principal import *
import sys, var
from calendario import *
from ventana_acercade import Ui_dlgAbout
from ventana_salir import Ui_dlgSalir
from windowaux import Calendar, Salir, DlgAcerca


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

        """STATUS BAR"""

        fecha = str(datetime.now())
        var.ui.statusbar.showMessage(fecha)



        """ZONA EVENTOS CERRAR VENTANA"""



    def closeEvent(self, event):
        resultado = QtWidgets.QMessageBox.information(self, "Confirmar salida", "¿Estás seguro de que quieres salir?",
                                                      QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if resultado == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        if resultado == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


