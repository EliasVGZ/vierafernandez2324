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
    def cargaprov(self = None):
        try:
            var.ui.cmbProvincia.clear() # LIMPIA Y VUELVE A RECARGAR

            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')
            query.prepare('select municipio from municipios')
            var.ui.cmbProvincia.addItem(' ')
            var.ui.cmbLocalidad.addItem('')

            if query.exec():
                var.ui.cmbProvincia.addItem(' ')
                while query.next(): #LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    var.ui.cmbProvincia.addItem(query.value(0))
                    var.ui.cmbLocalidad.addItem(query.value(0))



        except Exception as error:
            print("error al carga provincias", error)