import re
import sys

from PyQt6.QtWidgets import QComboBox
from PyQt6 import QtWidgets, QtCore
import var


class Drivers():

    @staticmethod
    def limpiarPanel(self):
        try:
            listawidgets = [var.ui.txtDni, var.ui.txtFechaAlta, var.ui.txtApellido, var.ui.txtFechaAlta,
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
            var.ui.txtSalario.setText(salario)
            patron = r'^\d{9}(\.\d{1,2})$'
            if not re.match(patron, salario):
                var.ui.txtMovil.clear()
                var.ui.txtMovil.setFocus()

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Valor de Salario Incorrecto (00000000.00)')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtSalario.setText("")

        except Exception as error:
            print('error poner movil', error)


    def validarMovil(self=None):
        try:
            var.ui.txtApel.setText(var.ui.txtApel.text().title())
            var.ui.txtNome.setText(var.ui.txtNome.text().title())
            movil = var.ui.txtMovil.text()
            patron = r'^\d{9}$'
            if not re.match(patron, movil):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Escriba un número de móvil correcto')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtMovil.setText("")


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
            driver = [var.ui.txtApellido, var.ui.txtNombre, var.ui.txtMovil]
            newDriver = []
            newDriver.append(1)
            for i in driver:
                newDriver.append(i.text().title())
            licencias = []

            chkLicencia = [var.ui.chkA, var.ui.chkB, var.ui.chkC, var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())

            newDriver.append(' - '.join(licencias))

            index = 0
            var.ui.tabDrivers.setRowCount(index + 1)  # crea una fila

            var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newDriver[0])))  # añadimos el new driver en la tabla
            var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newDriver[1])))  # añadimos el new driver en la tabla
            var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newDriver[2])))  # añadimos el new driver en la tabla
            var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newDriver[3])))  # añadimos el new driver en la tabla
            var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newDriver[4])))  # añadimos el new driver en la tabla

            var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Alineamos los items seleccionados
            var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            print(newDriver)

        except Exception as error:
            print("error alta cliente", error)



