from datetime import datetime

from PyQt6 import QtWidgets, QtCore

import var, sys

class Eventos():


    @staticmethod
    def salir():
        try:
            var.salir.show()

        except Exception as error:
            print(error, "en modulos eventos")


    @staticmethod
    def abrirCalendario(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error en abrir calendario", error)


    @staticmethod
    def acercade():
        try:
            var.dlgacercade.show()
        except Exception as error:
            print ("error abrir ventana acerca de", error)


    @staticmethod
    def cerraracercade():
        try:
            var.dlgacercade.hide()

        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def cerrarsalir():
        try:
            var.dlgsalir.hide()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def mostrarsalir(self, event):
        try:
            var.dlgsalir.show()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def aceptar(self):
        sys.exit()  # Cierra la aplicación

    @staticmethod
    def cancelar():
        var.salir.hide()  # Oculta el cuadro de diálogo

    @staticmethod
    def cargarstatusbar(self):

        try:
            fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
            fecha = fecha.capitalize()
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)

            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)
        except Exception as error:
            print('Error cargar el statusbar: ', error)

    @staticmethod
    def cargaprov(self):
        try:
            prov = ['A Coruña', 'Lugo', 'Vigo', 'Ferrol', 'Santiago de Compostela', 'Ourense', 'Pontevedra']
            var.ui.cmbProvincia.clear() # LIMPIA Y VUELVE A RECARGAR
            var.ui.cmbProvincia.addItem(' ')
            for i, m in enumerate (prov):
                var.ui.cmbProvincia.addItem(str(m))

        except Exception as error:
            print("error al carga provincias", error)

    @staticmethod
    def selEstado(self):

        if var.ui.rbtTodos.isChecked(): ##FUNCION PARA VERIFICAR QUE SE CLICKEO ENCIMA
            print("pulsaste todos")
        elif var.ui.rbtAlta.isChecked():
            print("pulsaste Alta")
        elif var.ui.rbtBaja.isChecked():
            print("pulsaste baja")


