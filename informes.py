import os, var, shutil
from PyQt6 import QtSql, QtWidgets
from reportlab.pdfgen import canvas
from datetime import datetime
import conexion
import svglib.svglib


class Informes:

    def reportclientes(self):
        try:
            fecha = datetime.today()
            nombre = fecha.strftime('%d-%m-%Y_%H-%M-%S') + '_listadoclientes.pdf'
            var.report = canvas.Canvas(os.path.join('informes', nombre))
            titulo = "Listado Clientes"
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            var.report.drawString(250, 200, 'Mi primer informe')

            var.report.save()
            rootPath = '.\\informes'

            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile(os.path.join(rootPath, file))

        except Exception as error:
            print('Error en informe', error)

    def topInforme(titulo):
        try:
            logo = '.\IMG\icono.png'
            var.report.line(50, 800, 525, 800)
            var.report.setFont('Helvetica-Bold', size=14)
            var.report.drawString(55, 785, 'Transportes Teis')
            var.report.drawString(240, 695, titulo)
            var.report.line(50, 690, 525, 690)
            var.report.drawImage(logo, 440, 725, width=40, height=35)
            var.report.setFont('Helvetica', size=9)
            var.report.drawString(55, 770, 'CIF:A12345678')
            var.report.drawString(55, 755, 'Avda Galicia - 101')
            var.report.drawString(55, 740, 'Vigo - 36216 - España')
            var.report.drawString(55, 710, 'Telefono: 986123 456')
            var.report.drawString(55, 725, 'e-mail: cartesteis@gmail.com')


        except Exception as error:
            print('Error en cabecera de informe', error)

    def footInforme(titulo):
        try:
            var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            var.report.setFont('Helvetica', size=7)
            var.report.drawString(50, 40, str(fecha))
            var.report.drawString(250, 40, str(titulo))
            var.report.drawString(490, 40, str('Página %s' % var.report.getPageNumber()))


        except Exception as error:
            print('Error en pie de informe', error)
