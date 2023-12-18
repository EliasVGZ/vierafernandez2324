import os.path
import shutil
from datetime import datetime

import xlrd
from PyQt6 import QtWidgets, QtCore, QtSql

import conexionClientes
import drivers, clientes
import var, sys, locale, zipfile, shutil, conexion, xlwt

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Eventos():

    @staticmethod
    def salir():
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
            print("error abrir ventana acerca de", error)

    @staticmethod
    def cerraracercade():
        try:
            var.dlgacercade.hide()

        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def cerrarsalir():
        try:
            var.dlgsalir.hide()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def mostrarsalir(self, event):
        try:
            var.dlgsalir.show()
        except Exception as error:
            print('error abrir ventana acerca de', error)

    @staticmethod
    def aceptar(self):
        sys.exit()  # Cierra la aplicación

    @staticmethod
    def cancelar():
        var.salir.hide()  # Oculta el cuadro de diálogo

    @staticmethod
    def cargarstatusbar(self):

        try:
            fecha = datetime.now().strftime("%A  -  " + "%d/%m/%Y")
            fecha = fecha.capitalize()
            self.labelstatus = QtWidgets.QLabel(fecha, self)
            self.labelstatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            var.ui.statusbar.addPermanentWidget(self.labelstatus, 1)

            self.labelstatusversion = QtWidgets.QLabel("Version: " + var.version, self)
            self.labelstatusversion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            var.ui.statusbar.addPermanentWidget(self.labelstatusversion, 0)
        except Exception as error:
            print('Error cargar el statusbar: ', error)

    def resizeTabDrivers(self):
        try:
            header = var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error al dimensionar la tabla", error)

    def resizeTabClientes(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(4):
                if i == 0 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)

        except Exception as error:
            print("error al dimensionar la tabla", error)

    def formatCajaTexto(self=None):
        try:

            var.ui.txtApellido.setText(
                var.ui.txtApellido.text().title())  # Toma el texto del widget txtApellido, lo convierte a título (es decir, la primera letra de cada palabra en mayúscula)
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(
                var.ui.txtSalario.text()))))  # Formatea el número como una cadena de texto en formato de moneda según la configuración regional actual

            var.ui.txtDni2.setText(var.ui.txtDni2.text().title())
            var.ui.txt_razonSocial.setText(var.ui.txt_razonSocial.text().title())
            var.ui.txtDireccionCliente.setText(var.ui.txtDireccionCliente.text().title())

        except Exception as error:
            print("error poner letra capital en caja de texto", error)

    def crearBackUp(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')  # formato año, mes, dia, hora, minuto, segundos
            copia = str(fecha + '_backup.zip')  # nombre del fichero
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia Seguridad', copia, '.zip')

            if var.dlgabrir.accept and filename:
                fichzip = zipfile.ZipFile(copia, 'w')
                fichzip.write(var.bbdd, os.path.basename(var.bbdd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(copia), str(directorio))
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Copia de Seguridad creada ')
                mbox.exec()
        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('Error en Copia de Seguridad: ')
            mbox.exec()

    def restaurarBackUp(self):
        try:
            filename = var.dlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridad',
                                                    '', '*.zip;;All Files(*)')
            file = filename[0]
            if var.dlgabrir.accept and file:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)

                bbdd.close()
                conexion.Conexion.mostrarDrivers()

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad Restaurada ')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en Restauracion Copia Seguridad ')
            msg.exec()

    def exportarDatosXls(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')  # formato año, mes, dia, hora, minuto, segundos
            file = (str(fecha) + ' _Datos.xls')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en Fichero XLS', file, '.xls')

            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Conductores')
                sheet1.write(0, 0, 'Codigo')  # el 0,0 es fila y columna
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Dirección')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Municipio')
                sheet1.write(0, 8, 'Móvil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Carnet')
                sheet1.write(0, 11, 'Fecha baja')

                registros = conexion.Conexion.selectDriversTodos(self)

                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(
                            registro[:-1]):  # el :-1 es para que no te muestre el ultimo dato, en este caso fecha baja
                        sheet1.write(fila, i, str(valor))
                wb.save(directorio)
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)  # para que la ventana sea modal, que nadie pueda acceder a la ventana de atras
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText('Exportacion datos correcta ')
            msg.exec()

    def exportarDatosClientesXls(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')  # formato año, mes, dia, hora, minuto, segundos
            file = (str(fecha) + ' _Datos.xls')
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar Datos en Fichero XLS', file, '.xls')

            if var.dlgabrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('Clientes')
                sheet1.write(0, 0, 'Codigo')  # el 0,0 es fila y columna
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Razon Social')
                sheet1.write(0, 3, 'Dirección')
                sheet1.write(0, 4, 'Provincia')
                sheet1.write(0, 5, 'Municipio')
                sheet1.write(0, 6, 'Teléfono')

                registros = conexionClientes.ConexionCliente.selectClientes(self)

                for fila, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro[:-1]):  # el :-1 es para que no te muestre el ultimo dato, en este caso fecha baja
                        sheet1.write(fila, i, str(valor))
                wb.save(directorio)

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)  # para que la ventana sea modal, que nadie pueda acceder a la ventana de atras
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Exportacion datos correcta ')
                msg.exec()

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)  # para que la ventana sea modal, que nadie pueda acceder a la ventana de atras
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error Exportar Datos en Hoja de Cálculos ' + str(error))
            msg.exec()


    def importardatosxls(self):
        try:
            estado = 0
            filename, _ = var.dlgabrir.getOpenFileName(None, 'Importar datos',
                                                       '', '*.xls;;All Files (*)')
            if filename:
                file = filename
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols
                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            if j == 1:
                                dato = xlrd.xldate_as_datetime(datos.cell_value(i, j), documento.datemode)
                                dato = dato.strftime('%d/%m/%Y')
                                new.append(str(dato))
                            else:
                                new.append(str(datos.cell_value(i, j)))

                        if drivers.Drivers.validarDni(str(new[0])):
                            conexion.Conexion.guardarClick(new)
                            drivers.Drivers.limpiarPanel(self)
                        elif estado == 0:
                            estado = 1
                            msg = QtWidgets.QMessageBox()
                            msg.setModal(True)
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                            msg.setText('Hay DNI incorrectos')
                            msg.exec()
                var.ui.lblValidarDni.setText('')

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importación de Datos Realizada')
                var.ui.lblValidarDni.setText('')
                msg.exec()

            conexion.Conexion.selectDrivers(1)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error', error)
            msg.exec()

    def importardatosclientesxls(self):
        try:
            estado = 0
            filename, _ = var.dlgabrir.getOpenFileName(None, 'Importar datos', '', '*.xls;;All Files (*)')
            if filename:
                file = filename
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)
                filas = datos.nrows
                columnas = datos.ncols

                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        new = []
                        for j in range(columnas):
                            cell_value = datos.cell_value(i, j)
                            if isinstance(cell_value, float):
                                new.append(str("{:.0f}".format(cell_value)))
                            else:
                                new.append(str(cell_value))

                        if clientes.Clientes.validarDni(str(new[0])):
                            conexionClientes.ConexionCliente.guardarCliente(new)
                            clientes.Clientes.limpiarPanelCliente(self)

                var.ui.lblValidarDni_2.setText('')

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Importación de Datos Realizada')
                var.ui.lblValidarDni_2.setText('')
                msg.exec()

            conexionClientes.ConexionCliente.selectClientes(1)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText(f'Error: {str(error)}')
            msg.exec()
