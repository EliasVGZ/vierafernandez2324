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
                            var.ui.txtTelefono, var.ui.cmbProvinciaCliente, var.ui.cmbLocalidadCliente]
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

            if not telefono.isdigit():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Escriba un número de teléfono correcto')
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.button(QtWidgets.QMessageBox.StandardButton.Ok).setText('Aceptar')
                msg.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()

                # Limpiar y enfocar el campo de teléfono
                var.ui.txtTelefono.clear()
                var.ui.txtTelefono.setFocus()

        except Exception as error:
            print('error al validar teléfono', error)

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
            newCliente.insert(4, prov)

            muni = var.ui.cmbLocalidadCliente.currentText()
            newCliente.insert(5, muni)
            print(newCliente)

            conexionClientes.ConexionCliente.guardarCliente(newCliente)

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
            cliente = [var.ui.lblCodCliente, var.ui.txtDni2, var.ui.txt_razonSocial, var.ui.txtDireccionCliente, var.ui.txtTelefono]
            modificarNewCliente = []

            for i in cliente:
                modificarNewCliente.append(i.text().title())

            ##AÑADIR PROVINCIAS AL CONDUCTOR
            prov = var.ui.cmbProvinciaCliente.currentText()
            modificarNewCliente.insert(4, prov)
            muni = var.ui.cmbLocalidadCliente.currentText()
            modificarNewCliente.insert(5, muni)

            conexionClientes.ConexionCliente.modifCliente(modificarNewCliente)

        except Exception as error:
            print("Error al modificar el cliente", error)

    def cargarTablaClientes(registros):
        try:

            index = 0
            for registro in registros:
                var.ui.tabClientes.setRowCount(index + 1)  # crea una fila
                var.ui.tabClientes.setItem(index, 0,QtWidgets.QTableWidgetItem(str(registro[0])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                var.ui.tabClientes.setItem(index, 2,QtWidgets.QTableWidgetItem(str(registro[2])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))  # añadimos el new  en la tabla
                var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))

                # Alineamos los items seleccionados
                var.ui.tabClientes.item(index, 1).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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



        except Exception as error:
            print("Error al cargar los datos de un cliente ", error)

    def cargarDatosCliente(registro):
        try:
            var.ui.lblCodCliente.setText(str(registro[0]))
            var.ui.txtDni2.setText(str(registro[1]))
            var.ui.txt_razonSocial.setText(str(registro[2]))
            var.ui.txtDireccionCliente.setText(str(registro[3]))
            var.ui.cmbProvinciaCliente.setCurrentText(str(registro[5]))
            var.ui.cmbLocalidadCliente.setCurrentText(str(registro[6]))
            var.ui.txtTelefono.setText(str(registro[4]))

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

    def buscarClienteTabla(codigo):
        try:
            tabla = var.ui.tabClientes
            for fila in range(tabla.rowCount()):
                item = tabla.item(fila, 0)
                valorCelda = item.text()
                if valorCelda == int(codigo):
                    tabla.selectRow(fila)
                    tabla.scrollToItem(item)
                    print("Fila encontrada:", fila)
        except Exception as error:
            print('No se ha podido seleccionar al cliente en la tabla', error)
