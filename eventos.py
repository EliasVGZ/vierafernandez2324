import var

class Eventos():
    def saludar(self):
        try:
            var.ui.lblTitulo.setText("hola, haz pulsado el boton")

        except Exception as error:
            print(error, "en modulos eventos")