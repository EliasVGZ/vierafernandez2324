from calendar import Calendar

import clientes
from windowaux import *
from PyQt6 import QtWidgets, QtSql, QtGui, QtCore
from datetime import date, datetime
import drivers
import eventos
import var

class ConexionCliente():

    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
        if not db.open():
            print("error de conexión")
            return False
        else:
            print("base de datos conectada")

    @staticmethod
    def cargarprov():
        try:
            var.ui.cmbProvinciaCliente.clear()  # LIMPIA Y VUELVE A RECARGAR

            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            var.ui.cmbProvinciaCliente.addItem(' ')

            if query.exec():
                var.ui.cmbProvinciaCliente.addItem(' ')
                while query.next():  # LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    var.ui.cmbProvinciaCliente.addItem(query.value(0))
        except Exception as error:
            print("error al carga provincias", error)


    def selMuni(self=None):
        try:
            var.ui.cmbLocalidadCliente.clear()
            id = 0
            provcliente = var.ui.cmbProvinciaCliente.currentText()  #
            query = QtSql.QSqlQuery()

            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', provcliente)
            if query.exec():
                while query.next():  # LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbLocalidadCliente.addItem('')
                while query1.next():
                    var.ui.cmbLocalidadCliente.addItem(query1.value(0))

        except Exception as error:
            print("error seleccion municipios ", error)

    def guardarCliente(newCliente):
        try:
            dni = str(newCliente[0])
            query = QtSql.QSqlQuery()
            query.prepare(
                'insert into clientes (dnicliente, razonSocial, direccioncliente, telefono, provinciacliente, municipiocliente '
                ') VALUES (:dni, :razonsocial, :direccioncliente, :telefono, :provcliente, :municliente)')

            query.bindValue(':dni', dni)
            query.bindValue(':razonsocial', str(newCliente[1]))
            query.bindValue(':direccioncliente', str(newCliente[2]))
            query.bindValue(':telefono', str(newCliente[3]))
            query.bindValue(':provcliente', str(newCliente[4]))
            query.bindValue(':municliente', str(newCliente[5]))


            if query.exec():
                return True
            else:
                return False

            ConexionCliente.mostrarClientes(self=None)


        except Exception as error:
            print("Error guardando los clientes", error)

    def borrarCliente(dni):
        global valor
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajacliente from clientes where  '
                           'dnicliente = :dni')
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
                    print(valor)
            if valor == '':
                fecha = datetime.today()
                fecha = fecha.strftime("%d/%m/%Y")

                query = QtSql.QSqlQuery()
                query.prepare('update clientes set bajacliente = :fechabaja where '
                              'dnicliente = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Cliente dado de baja')
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText('Error al dar de baja al Cliente: ' + query.lastError().text())
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Cliente ya está dado de baja')
                mbox.exec()
        except Exception as error:
            print("Error al dar de baja al Cliente", error)

    def mostrarClientes(self):
        try:
            registros = []
            if var.ui.rbtAltaCliente.isChecked():
                estado = 1
                ConexionCliente.selectClientes(estado)
            else:
                query1 = QtSql.QSqlQuery()
                query1.prepare("select codigo, razonSocial, telefono, provinciacliente from clientes")
                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())]  # funcion lambda
                        registros.append(row)

            if registros:
                clientes.Clientes.cargarTablaClientes(registros)
            else:
                var.ui.tabClientes.setRowCount(0)


        except Exception as error:
            print("error mostrar resultados", error)

    def oneCliente(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 cliente: ", error)

    def selectClientes(estado):
        try:
            registros = []
            if estado == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, razonSocial, telefono, provinciacliente from clientes")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)

                clientes.Clientes.cargarTablaClientes(registros)


            elif estado == 1:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, razonSocial, telefono, provinciacliente from clientes where bajacliente is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)


                clientes.Clientes.cargarTablaClientes(registros)



            elif estado == 2:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, razonSocial, telefono, provinciacliente from clientes where bajacliente is not null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)

                clientes.Clientes.cargarTablaClientes(registros)


        except Exception as error:
            print("Error al seleccionar los clientes", error)

    def modifCliente(modificarNewCliente):
        try:
            registro = ConexionCliente.oneCliente(int(modificarNewCliente[0]))
            query = QtSql.QSqlQuery()
            query.prepare(
                'update clientes set dnicliente = :dni, razonSocial = :razonsocial, direccioncliente = :dire, telefono = :tel, provinciacliente = :prov, '
                'municipiocliente = :muni where codigocliente = :codigo')

            query.bindValue(':codigo', int(modificarNewCliente[0]))
            query.bindValue(':dni', str(modificarNewCliente[1]))
            query.bindValue(':razonsocial', str(modificarNewCliente[2]))
            query.bindValue(':dire', str(modificarNewCliente[3]))
            query.bindValue(':tel', str(modificarNewCliente[4]))
            query.bindValue(':prov', str(modificarNewCliente[5]))
            query.bindValue(':muni', str(modificarNewCliente[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText('Datos cliente modificado')
                mbox.exec()
                ConexionCliente.mostrarClientes(1)
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText(query.lastError().text())
                mbox.exec()

        except Exception as error:
            print("Error al modificar cliente en conexion", error)