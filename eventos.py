import var

class Eventos():
    def saludar(self):
        try:
            var.ui.lblTitulo.setText("Hola, haz pulsado el boton")

        except Exception as error:
            print(error, "en modulos eventos")