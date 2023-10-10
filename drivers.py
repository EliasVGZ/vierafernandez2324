import var

class Drivers():

    @staticmethod
    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApellido, var.ui.txtFechaAlta, var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario, var.ui.txtNombre, var.ui.lblValidarDni]
            for i in listawidgets:
                i.setText(None)

        except Exception as error:
            print("error limpiando panel", error)
    def cargarFecha(qDate):
        try:
            data=('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar fecha", error)
    def validarDni(self=None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_digito_extranjero = {'X':'0', 'Y':'1', 'Z':'2'}
            numeros = "1234567890"
            if len(dni) == 9:           #COMPRUEBO QUE SON 9
                dig_control = dni[8]    #TOMO LA LETRA DEL DNI QUE ESTÁ SITUADO EN LA POSICION 8
                dni = dni[:8]           #tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_digito_extranjero[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla [int(dni) % 23 ]== dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')



                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.clear()  # Limpia el campo de texto
                    var.ui.txtDni.setFocus() # Mantiene el foco en el campo de texto

            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.clear()  # Limpia el campo de texto
                var.ui.txtDni.setFocus() # Mantiene el foco en el campo de texto


        except Exception as error:
            print("Error en validar dni", error)

