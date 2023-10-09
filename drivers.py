import var
class Drivers():
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


            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')


        except Exception as error:
            print("Error en validar dni", error)

