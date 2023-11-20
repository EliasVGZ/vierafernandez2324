import os.path
import shutil
from datetime import datetime
from PyQt6 import QtWidgets, QtCore
import var, sys,locale, zipfile, shutil
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
            print ("error abrir ventana acerca de", error)


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



    def formatCajaTexto(self=None):
        try:

            var.ui.txtApellido.setText(var.ui.txtApellido.text().title())# Toma el texto del widget txtApellido, lo convierte a título (es decir, la primera letra de cada palabra en mayúscula)
            var.ui.txtNombre.setText(var.ui.txtNombre.text().title())
            var.ui.txtSalario.setText(str(locale.currency(float(var.ui.txtSalario.text()))))# Formatea el número como una cadena de texto en formato de moneda según la configuración regional actual


        except Exception as error:
            print("error poner letra capital en caja de texto", error)

    @classmethod
    def crearBackUp(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')#formato año, mes, dia, hora, minuto, segundos
            copia = str(fecha + '_backup.zip') #nombre del fichero
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Guardar Copia Seguridad', copia, '.zip')
            if var.dlgabrir.accept and filename != '':
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
            mbox.setText('Error en Copia de Seguridad: ' )
            mbox.exec()

