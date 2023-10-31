from PyQt6 import QtWidgets, QtSql, QtCore
import var


class Conexion():

    def conexion(self=None):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('bbdd.sqlite')
        if not db.open():
            print("error de conexión")
            return False
        else:
            print("base de datos conectada")
            return True

    @staticmethod
    def cargaprov(self=None):
        try:
            var.ui.cmbProvincia.clear()  # LIMPIA Y VUELVE A RECARGAR

            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            # query.prepare('select municipio from municipios')
            var.ui.cmbProvincia.addItem(' ')
            # var.ui.cmbLocalidad.addItem('')

            if query.exec():
                var.ui.cmbProvincia.addItem(' ')
                while query.next():  # LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    var.ui.cmbProvincia.addItem(query.value(0))
                    # var.ui.cmbLocalidad.addItem(query.value(0))



        except Exception as error:
            print("error al carga provincias", error)

    def selMuni(self=None):
        try:
            var.ui.cmbLocalidad.clear()
            id = 0
            prov = var.ui.cmbProvincia.currentText()  #
            query = QtSql.QSqlQuery()

            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)
            if query.exec():
                while query.next():  # LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    id = query.value(0)
            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))
            if query1.exec():
                var.ui.cmbLocalidad.addItem('')
                while query1.next():
                    var.ui.cmbLocalidad.addItem(query1.value(0))

        except Exception as error:
            print("error seleccion municipios ", error)




    @staticmethod
    def guardarClick(newDriver):
       try:
           query = QtSql.QSqlQuery()
           query.prepare('insert into drivers (dnidriver, altadriver, apeldriver, nombredriver, direcciondriver, provdriver, munidriver, movildriver, salario, carnet) VALUES (:dni, :alta, :apel, :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet)')

           query.bindValue(':dni', str(newDriver[0]))
           query.bindValue(':alta', str(newDriver[1]))
           query.bindValue(':apel', str(newDriver[2]))
           query.bindValue(':nombre', str(newDriver[3]))
           query.bindValue(':direccion', str(newDriver[4]))
           query.bindValue(':provincia', str(newDriver[5]))
           query.bindValue(':municipio', str(newDriver[6]))
           query.bindValue(':movil', str(newDriver[7]))
           query.bindValue(':salario', str(newDriver[8]))
           query.bindValue(':carnet', str(newDriver[9]))

           if query.exec():
               mbox = QtWidgets.QMessageBox()
               mbox.setWindowTitle('Aviso')
               mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
               mbox.setText('Empleado dado de alta')
               mbox.exec()
           else:
               mbox = QtWidgets.QMessageBox()
               mbox.setWindowTitle('Aviso')
               mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
               mbox.setText(query.lastError().text())
               mbox.exec()
           #select de los datos de conductores de la base de datos
           #drivers.Drivers.cargarTabla(datosdriver)

       except Exception as error:
           print ("error guardando los drivers", error)

