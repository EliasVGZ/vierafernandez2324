
from calendar import Calendar
from windowaux import *
from PyQt6 import QtWidgets, QtSql, QtGui, QtCore
from datetime import date, datetime
import drivers
import eventos
import var


class Conexion():

    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)
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
            var.ui.cmbProvincia.addItem(' ')


            if query.exec():
                var.ui.cmbProvincia.addItem(' ')
                while query.next():  # LLENAR LAS PROVINCIAS MIENTRAS HAYA
                    var.ui.cmbProvincia.addItem(query.value(0))




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
            dni = str(newDriver[0])
            if (dni.strip() == "" or newDriver[2].strip() == "" or newDriver[3].strip() == "" or newDriver[
                7].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setWindowIcon(QtGui.QIcon('./IMG/aviso.jpg'))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = ('Faltan datos:\n Dni, Apellido, Nombre, Fecha de alta o Movil no pueden estar vacíos')
                mbox.setText(mensaje)
                mbox.exec()

            else:
                query = QtSql.QSqlQuery()
                query.prepare(
                    'insert into drivers (dnidriver, altadriver, apeldriver, nombredriver, direcciondriver, provdriver, munidriver, movildriver, salario, carnet) VALUES (:dni, :alta, :apel, :nombre, :direccion, :provincia, :municipio, :movil, :salario, :carnet)')

                query.bindValue(':dni', dni)
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
                return True
            else:
                return False
            Conexion.mostrarDrivers(self=None)

        except Exception as error:
            print("Error guardando los drivers", error)

    def mostrarDrivers(self):
        try:
            registros = []
            if var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.selectDrivers(estado)
            else:
                query1 = QtSql.QSqlQuery()
                query1.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                               "carnet, bajadriver from drivers")
                if query1.exec():
                    while query1.next():
                        row = [query1.value(i) for i in range(query1.record().count())]  # funcion lambda
                        registros.append(row)
            # SI ESTAN TODOS DE BAJA DEBE MOSTRAR LA TABLA DE ALTA VACIA
            if registros:
                drivers.Drivers.cargarTablaDriver(registros)
            else:
                var.ui.tabDrivers.setRowCount(0)

        except Exception as error:
            print("error mostrar resultados", error)

    def oneDriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 driver: ", error)

    def codigoDriver(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo FROM drivers WHERE dnidriver = :dnidri")
            query.bindValue(":dnidri", str(dni))

            if query.exec():
                codigo = None
                while query.next():
                    codigo = query.value(0)
                    drivers.Drivers.buscarDriverTabla(codigo)

                if codigo is not None:
                    registro = Conexion.oneDriver(codigo)
                    return registro
                else:
                    # Si no se encuentra el conductor, mostrar un aviso
                    var.ui.lblValidarDni.setStyleSheet('color:red;')
                    var.ui.lblValidarDni.setText('X')
                    var.ui.txtDni.clear()  # Limpia el campo de texto
                    var.ui.txtDni.setFocus()  # Mantiene el foco en el campo de texto
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./IMG/aviso.jpg'))  # Ruta del archivo del icono
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mensaje = ('          DNI no existe          ')
                    mbox.setText(mensaje)
                    mbox.exec()
                    return None

        except Exception as error:
            print("Error en búsqueda de código de un conductor: ", error)
            return None

    def modifDriver(modificarNewDriver):
        try:
            registro = Conexion.oneDriver(int(modificarNewDriver[0]))
            if modificarNewDriver == registro[:-1]:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('No hay datos que modificar. Desea cambiar la fecha o eliminar fecha de baja?')
                msg.setStandardButtons(
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No |
                    QtWidgets.QMessageBox.StandardButton.Cancel)
                msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText("Alta")
                msg.button(QtWidgets.QMessageBox.StandardButton.No).setText("Modificar")
                msg.button(QtWidgets.QMessageBox.StandardButton.Cancel).setText('Cancelar')
                opcion = msg.exec()
                if opcion == QtWidgets.QMessageBox.StandardButton.Yes:
                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadriver = NULL where '
                                       ' dnidriver = :dni')
                        query1.bindValue(':dni', str(modificarNewDriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Datos Conductor Modificados')
                            msg.exec()
                            Conexion.selectDrivers(2)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.No:
                    var.calendar2 = Calendar()
                    var.calendar2.show()
                    var.calendar2.selectionChanged.connect(Conexion.showSelectedDate)

                    data = Conexion.showSelectedDate()
                    print("Fecha seleccionada; ", data)
                    print('hola')
                    data = data.toString("dd/MM/yyyy")
                    print(data)


                    if registro[11] != '':
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update drivers set bajadriver = :data where '
                                       ' dnidriver = :dni')
                        query1.bindValue(':data', str(data))
                        query1.bindValue(':dni', str(modificarNewDriver[1]))
                        if query1.exec():
                            msg = QtWidgets.QMessageBox()
                            msg.setWindowTitle('Aviso')
                            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                            msg.setText('Baja Modificada. Nueva Fecha Baja')
                            msg.exec()
                        Conexion.selectDrivers(0)
                    else:
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle('Aviso')
                        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        msg.setText('El conductor está en alta. Nada que modificar')
                        msg.exec()
                        Conexion.selectDrivers(1)
                elif opcion == QtWidgets.QMessageBox.StandardButton.Cancel:
                    pass
            else:

                query = QtSql.QSqlQuery()
                query.prepare(
                    'update drivers set dnidriver = :dni, altadriver = :alta, apeldriver = :apel, nombredriver = :nombre, direcciondriver = :direccion, '
                    'provdriver = :provincia, munidriver = :municipio, movildriver = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

                query.bindValue(':codigo', int(modificarNewDriver[0]))
                query.bindValue(':dni', str(modificarNewDriver[1]))
                query.bindValue(':alta', str(modificarNewDriver[2]))
                query.bindValue(':apel', str(modificarNewDriver[3]))
                query.bindValue(':nombre', str(modificarNewDriver[4]))
                query.bindValue(':direccion', str(modificarNewDriver[5]))
                query.bindValue(':provincia', str(modificarNewDriver[6]))
                query.bindValue(':municipio', str(modificarNewDriver[7]))
                query.bindValue(':movil', str(modificarNewDriver[8]))
                query.bindValue(':salario', str(modificarNewDriver[9]))
                query.bindValue(':carnet', str(modificarNewDriver[10]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Datos conductor modificado')
                    mbox.exec()
                    Conexion.mostrarDrivers(1)
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText(query.lastError().text())
                    mbox.exec()

        except Exception as error:
            print("Error al modificar driver en conexion", error)

    def showSelectedDate(self=None):
        selected_date = var.calendar2.selectedDate()
        return selected_date.toString("dd/MM/yyyy")

    def borraDriv(dni):
        global valor
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadriver from drivers where  '
                           'dnidriver = :dni')
            query1.bindValue(':dni', str(dni))

            if query1.exec():
                while query1.next():
                    valor = query1.value(0)
                    print(valor)
            if valor == '':
                fecha = datetime.today()
                fecha = fecha.strftime("%d/%m/%Y")

                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadriver = :fechabaja where '
                              'dnidriver = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText('Conductor dado de baja')
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText('Error al dar de baja al conductor: ' + query.lastError().text())
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText('Conductor ya está dado de baja')
                mbox.exec()
        except Exception as error:
            print("Error al dar de baja al driver", error)

    def selectDrivers(estado):
        try:
            registros = []
            if estado == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                              "carnet, bajadriver from drivers")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)

                if registros:
                    drivers.Drivers.cargarTablaDriver(registros)
                else:
                    var.ui.tabDrivers.setRowCount(0)

            elif estado == 1:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                              "carnet, bajadriver from drivers where bajadriver is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)

                if registros:
                    drivers.Drivers.cargarTablaDriver(registros)
                else:
                    var.ui.tabDrivers.setRowCount(0)


            elif estado == 2:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                              "carnet, bajadriver from drivers where bajadriver is not null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)

                drivers.Drivers.cargarTablaDriver(registros)
        except Exception as error:
            print("Error al seleccionar los drivers", error)

    def selectDriversTodos(self):  # METODO PARA LLAMAR A TODOS
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from drivers order by codigo")

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros

        except Exception as error:
            print("error devolver todos los drivers", error)

    def volverDarAlta(dni):
        try:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Dar Alta")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)
            mbox.setText("El conductor está dado de baja.\n¿Desea darlo de alta de nuevo?")
            mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
            mbox.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Si')
            mbox.button(QtWidgets.QMessageBox.StandardButton.No).setText('No')
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
            mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.No)

            if mbox.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
                query = QtSql.QSqlQuery()
                query.prepare("update drivers set bajadriver = :baja where dnidriver = :dni")
                query.bindValue(":dni", dni)
                # query.bindValue(":baja", None)
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Conductor dado de alta")
                    mbox.exec()
                    drivers.Drivers.cargarTablaDriver()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("El conductor no se pudo dar de alta")
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Conductor no dado de alta")
                mbox.exec()

        except Exception as error:
            print("Error al dar alta de nuevo conductor en BD", error)

    def conductorEstaDadoDeBaja(self, dni):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT bajadriver FROM drivers WHERE dnidriver = :dni")
        query.bindValue(":dni", dni)

        if query.exec() and query.next():
            bajadriver_value = query.value(0)
            return bajadriver_value is not None and bajadriver_value != 0

        return False

    def driversEstadoAlta(self):
        try:
            conductores_alta = []
            query = QtSql.QSqlQuery()
            query.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                          "carnet, bajadriver from drivers where bajadriver is null")

            if query.exec():
                while query.next():
                    conductor = [str(query.value(i)) for i in range(12)]
                    conductores_alta.append(conductor)

            return conductores_alta

        except Exception as error:
            print("Error al obtener conductores de alta:", error)
            return []

    def driversEstadoBaja(self):
        try:
            conductores_baja = []
            query = QtSql.QSqlQuery()
            query.prepare("select codigo, apeldriver, nombredriver, movildriver, "
                          "carnet, bajadriver from drivers where bajadriver is not null")

            if query.exec():
                while query.next():
                    conductor = [str(query.value(i)) for i in range(12)]
                    conductores_baja.append(conductor)

            return conductores_baja

        except Exception as error:
            print("Error al obtener conductores de baja:", error)
            return []

    def conductorExiste(self, dni):
        query = QtSql.QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM drivers WHERE bajadriver = :dni")
        query.bindValue(":dni", dni)

        if query.exec() and query.next():
            count = query.value(0)
            return count > 0

        return False
