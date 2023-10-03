
from PyQt6 import QtWidgets

import eventos
from venta_principal import *
import sys, var

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VentanaPrincipal()
        var.ui.setupUi(self) #encargado de la interfaz

        '''
        zona de eventos de botones
        
        '''



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


