import var, sys

class Eventos():
    @staticmethod
    def salir(self):
        try:
            sys.exit()

        except Exception as error:
            print(error, "en modulos eventos")

    @staticmethod
    def abrirCalendario(self):
        try:
            var.calendar.show()
        except Exception as error:
            print("error en abrir calendario", error)


    @staticmethod
    def acercaDe(self):
        try:
            pass
        except Exception as error:
            print ("error abrir ventana acerca de", error)