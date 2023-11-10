import re

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QComboBox

import conexion
import var


class Drivers():

    @staticmethod
    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.lblCodbd, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApellido,
                            var.ui.txtFechaAlta,
                            var.ui.txtDireccion,
                            var.ui.txtMovil, var.ui.txtSalario, var.ui.txtNombre, var.ui.lblValidarDni,
                            var.ui.cmbProvincia, var.ui.cmbLocalidad]
            for i in listawidgets:
                if hasattr(i, 'setText'):
                    i.setText(None)
                elif isinstance(i, QComboBox):  # borrar combobox
                    i.setCurrentIndex(-1)

            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                i.setChecked(False)

        except Exception as error:
            print("error limpiando panel", error)

    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar fecha", error)

    def validarSalario(self=None):
        try:
            salario = var.ui.txtSalario.text()
            if salario != "":
                var.ui.txtSalario.setText(salario)
                patronReg = r'^\d{1,8}(\.\d{1,2})?$'
                if not re.match(patronReg, salario):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Aviso')
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText('Valor de Salario Incorrecto (00000000.00)')
                    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                    msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                    msg.exec()
                    var.ui.txtSalario.setText("")
                    var.ui.txtSalario.setFocus()

        except Exception as error:
            print('error poner salario', error)

    def validarMovil(self=None):
        try:
            var.ui.txtApellido.setText(var.ui.txtApellido.text().title())
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            movil = var.ui.txtMovil.text()
            var.ui.txtMovil.setText(movil)
            patron = r'^\d{9}$'
            if not re.match(patron, movil):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Escriba un número de móvil correcto (9 digitos)')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtMovil.setText("")
                var.ui.txtMovil.clear()
                var.ui.txtMovil.setFocus()


        except Exception as error:
            print('error poner movil', error)

    def validarDni(self=None):
        try:
            dni = var.ui.txtDni.text()
            dni = dni.upper()
            var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_digito_extranjero = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            if len(dni) == 9:  # COMPRUEBO QUE SON 9
                dig_control = dni[8]  # TOMO LA LETRA DEL DNI QUE ESTÁ SITUADO EN LA POSICION 8
                dni = dni[:8]  # tomo los numeros del dni
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_digito_extranjero[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidarDni.setStyleSheet('color:green;')
                    var.ui.lblValidarDni.setText('V')
                else:
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.clear()  # Limpia el campo de texto
                    var.ui.txtDni.setFocus()  # Mantiene el foco en el campo de texto

            else:
                var.ui.lblValidarDni.setStyleSheet('color:red;')
                var.ui.lblValidarDni.setText('X')
                var.ui.txtDni.clear()  # Limpia el campo de texto
                var.ui.txtDni.setFocus()  # Mantiene el foco en el campo de texto


        except Exception as error:
            print("Error en validar dni", error)

    def altaDriver(self):
        try:
            driver = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApellido, var.ui.txtNombre, var.ui.txtDireccion,
                      var.ui.txtMovil, var.ui.txtSalario]
            newDriver = []

            for i in driver:
                newDriver.append(i.text().title())

            ##AÑADIR PROVINCIAS AL CONDUCTOR
            prov = var.ui.cmbProvincia.currentText()
            newDriver.insert(5, prov)

            muni = var.ui.cmbLocalidad.currentText()
            newDriver.insert(6, muni)

            licencias = []
            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())

            newDriver.append(' - '.join(licencias))

            conexion.Conexion.guardarClick(newDriver)

            print(newDriver)

        except Exception as error:
            print("error alta cliente", error)

    def cargarTablaDriver(registros):
        try:
            index = 0
            for registro in registros:
                var.ui.tabDrivers.setRowCount(index + 1)  # crea una fila
                var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(
                    str(registro[0])))  # añadimos el new driver en la tabla
                var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(
                    str(registro[1])))  # añadimos el new driver en la tabla
                var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(
                    str(registro[2])))  # añadimos el new driver en la tabla
                var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(
                    str(registro[3])))  # añadimos el new driver en la tabla
                var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(
                    str(registro[4])))  # añadimos el new driver en la tabla

                var.ui.tabDrivers.item(index, 0).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter)  # Alineamos los items seleccionados
                var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1


        except Exception as error:
            print("Error mostrar tabla", error)

    def cargaDriver(self):
        try:

            Drivers.limpiarPanel(self)

            row = var.ui.tabDrivers.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexion.Conexion.oneDriver(fila[0])
            # LLAMAMOS AL METODO CARGARDATOS PARA NO COPIAR CODIGO
            Drivers.cargarDatos(registro)

            print(fila)

        except Exception as error:
            print("Error al cargar los datos de un cliente ", error)

    ##BOTON BUSCAR CONDUCTOR!!!!!!!!!!!!
    def buscarDriverLupa(self):
        try:
            dni = var.ui.txtDni.text()
            registro = conexion.Conexion.codigoDriver(dni)
            Drivers.cargarDatos(registro)



        except Exception as error:
            print("Error al buscar por DNI: ", error)

    #BUSCAR EL CONDUCTOR Y LO MARQUE EN LA TABLA
    def buscarDriverTabla(codigo):
        try:
            tabla = var.ui.tabDrivers
            for fila in range(tabla.rowCount()):
                item = tabla.item(fila, 0)
                valorCelda = item.text()
                if valorCelda == str(codigo):
                    tabla.selectRow(fila)
                    tabla.scrollToItem(item)
                    print("Fila encontrada:", fila)
        except Exception as error:
            print('No se ha podido seleccionar al driver en la tabla', error)

    def cargarDatos(registro):
        try:
            datos = [var.ui.lblCodbd, var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApellido, var.ui.txtNombre,
                     var.ui.txtDireccion, var.ui.cmbProvincia, var.ui.cmbLocalidad,
                     var.ui.txtMovil, var.ui.txtSalario]
            # CARGAR LOS DATOS CUANDO CLICKEAMOS ENCIMA DE ALGUN DRIVER
            for j, dato in enumerate(datos):
                # si el índice j es igual a 6 o 7. Si es el caso, significa que dato se refiere a un elemento desplegable (cmbProvincia o cmbLocalidad).
                if j == 6 or j == 7:
                    # se utiliza el método setCurrentText para establecer el texto seleccionado en el elemento desplegable, utilizando el valor str(registro[j]).
                    dato.setCurrentText(str(registro[j]))
                else:
                    dato.setText(str(registro[j]))

            if 'A' in registro[10]:
                var.ui.chkA.setChecked(True)
            if 'B' in registro[10]:
                var.ui.chkB.setChecked(True)
            if 'C' in registro[10]:
                var.ui.chkC.setChecked(True)
            if 'D' in registro[10]:
                var.ui.chkD.setChecked(True)

            print(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente ", error)
