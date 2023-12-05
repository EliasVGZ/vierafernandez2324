import re

from PyQt6 import QtWidgets, QtCore, QtGui, QtSql
from PyQt6.QtWidgets import QComboBox

import conexion
import conexionClientes
import var


class Clientes():

    @staticmethod
    def limpiarPanelCliente(self):
        try:
            listawidgets = [var.ui.lblCodCliente, var.ui.txtDni2, var.ui.txt_razonSocial, var.ui.txtDireccionCliente,
                            var.ui.txtTelefono]
            for i in listawidgets:
                if hasattr(i, 'setText'):
                    i.setText(None)
                elif isinstance(i, QComboBox):  # borrar combobox
                    i.setCurrentIndex(-1)

        except Exception as error:
            print("error limpiando panel", error)


    def cargarFecha(qDate):
        try:
            data = ('{:02d}/{:02d}/{:4d}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.txtFechaAlta.setText(str(data))
            var.calendar.hide()

        except Exception as error:
            print("error en cargar fecha", error)

    def validarTelefono(self=None):
        try:
            telefono = var.ui.txtTelefono.text()
            var.ui.txtTelefono.setText(telefono)
            patron = r'^\d{1,20}$'
            if not re.match(patron, telefono):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Escriba un número de teléfono correcto')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                var.ui.txtMovil.setText("")
                var.ui.txtMovil.clear()
                var.ui.txtMovil.setFocus()

        except Exception as error:
            print('error poner movil', error)

    def validarDni(dni):
        try:
            dni = str(dni).upper()
            var.ui.txtDni2.setText(str(dni))
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
                    var.ui.lblValidarDni_2.setStyleSheet('color:green;')
                    var.ui.lblValidarDni_2.setText('V')
                    return True
                else:
                    var.ui.lblValidarDni_2.setStyleSheet('color:red;')
                    var.ui.lblValidarDni_2.setText('X')
                    var.ui.txtDni2.clear()  # Limpia el campo de texto
                    var.ui.txtDni2.setFocus()  # Mantiene el foco en el campo de texto

            else:
                var.ui.lblValidarDni_2.setStyleSheet('color:red;')
                var.ui.lblValidarDni_2.setText('X')
                var.ui.txtDni2.clear()  # Limpia el campo de texto
                var.ui.txtDni2.setFocus()  # Mantiene el foco en el campo de texto


        except Exception as error:
            print("Error en validar dni", error)

    def altaCliente(self):
        try:

            cliente = [var.ui.txtDni2, var.ui.txt_razonSocial, var.ui.txtDireccionCliente, var.ui.txtTelefono]
            newCliente = []

            for i in cliente:
                newCliente.append(i.text().title())

            ##AÑADIR PROVINCIAS AL CONDUCTOR
            prov = var.ui.cmbProvinciaCliente.currentText()
            newCliente.insert(3, prov)

            muni = var.ui.cmbLocalidadCliente.currentText()
            newCliente.insert(4, muni)

            conexionClientes.ConexionCliente.guardarCliente(newCliente)

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText('Cliente dado de alta')
            mbox.exec()

        except Exception as error:
            print("error alta cliente", error)

    def borrarCliente(self):
        try:
            dni = var.ui.txtDni2.text()
            conexionClientes.ConexionCliente.borrarCliente(dni)
            conexionClientes.ConexionCliente.selectClientes(1)

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mensaje = ('          Cliente no existe o no se puede dar de baja          ')
            mbox.setText(mensaje)
            mbox.exec()

    def modificaCliente(self):
        try:
            cliente = [var.ui.txtDni2, var.ui.txt_razonSocial, var.ui.txtDireccionCliente, var.ui.txtTelefono]
            modificarNewCliente = []

            for i in cliente:
                modificarNewCliente.append(i.text().title())

            ##AÑADIR PROVINCIAS AL CONDUCTOR
            prov = var.ui.cmbProvincia.currentText()
            modificarNewCliente.insert(3, prov)
            muni = var.ui.cmbLocalidad.currentText()
            modificarNewCliente.insert(4, muni)


            conexionClientes.ConexionCliente.modifCliente(modificarNewCliente)

        except Exception as error:
            print("Error al modificar el driverrrrrrrrrrrrrrrrrr", error)

    def cargarTablaClientes(registros):
        try:

            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)  # crea una fila
                var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))

                # Alineamos los items seleccionados
                var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                index += 1


        except Exception as error:
            print("Error mostrar tabla", error)

    def cargaCliente(self):
        try:
            Clientes.limpiarPanelCliente(self)

            row = var.ui.tabClientes.selectedItems()
            fila = [dato.text() for dato in row]
            registro = conexionClientes.ConexionCliente.oneCliente(fila[0])

            # LLAMAMOS AL METODO CARGARDATOS PARA NO COPIAR CODIGO
            Clientes.cargarDatosCliente(registro)

            print(fila)

        except Exception as error:
            print("Error al cargar los datos de un cliente ", error)

    def cargarDatosCliente(registro):
        try:
            datos = [var.ui.lblCodCliente, var.ui.txtDni2, var.ui.txt_razonSocial, var.ui.txtDireccionCliente, var.ui.cmbProvinciaCliente,
                     var.ui.cmbLocalidadCliente, var.ui.txtTelefono]
            # CARGAR LOS DATOS CUANDO CLICKEAMOS ENCIMA DE ALGUN DRIVER
            for j, dato in enumerate(datos):
                if j == 4 or j == 5:
                    dato.setCurrentText(str(registro[j]))
                else:
                    dato.setText(str(registro[j]))


            print(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente ", error)

    def selEstadoCliente(self):

        try:

            if var.ui.rbtTodosCliente.isChecked():  ##FUNCION PARA VERIFICAR QUE SE CLICKEO ENCIMA
                estado = 0
                conexionClientes.ConexionCliente.selectClientes(estado)
            elif var.ui.rbtAltaCliente.isChecked():

                estado = 1
                conexionClientes.ConexionCliente.selectClientes(estado)

            elif var.ui.rbtBajaCliente.isChecked():

                estado = 2
                conexionClientes.ConexionCliente.selectClientes(estado)


        except Exception as error:
            print("Error en selEstado:", error)

