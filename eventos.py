from PyQt6.uic.properties import QtWidgets

import var, sys

class Eventos():


    @staticmethod
    def salir(self):
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
            var.dlgacerca.hide()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def cerrarsalir():
        try:
            var.dlgsalir.hide()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def mostrarsalir():
        try:
            var.dlgsalir.show()
        except Exception as error:
            print('error abrir ventana acerca de', error)

