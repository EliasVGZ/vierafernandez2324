from datetime import datetime

from PyQt6 import QtWidgets

import eventos
from venta_principal import *
import sys, var
from calendario import *



class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self) #encargado de la interfaz
        var.calendar=Calendar()

        """zona de eventos de botones"""

        var.ui.btnCalendario.clicked.connect(eventos.Eventos.abrirCalendario)

        """ ZONA DE EVENTOS DEL MENU BAR"""

        var.ui.actionSalir.triggered.connect(eventos.Eventos.salir)



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self). __init__()
        var.calendar = Ui_Calendario()
        var.calendar.setupUi(self)
        dia= datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


