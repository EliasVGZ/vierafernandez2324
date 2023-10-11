# Form implementation generated from reading ui file 'venta_principal.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaPrincipal.sizePolicy().hasHeightForWidth())
        VentanaPrincipal.setSizePolicy(sizePolicy)
        VentanaPrincipal.setMinimumSize(QtCore.QSize(1024, 768))
        VentanaPrincipal.setMaximumSize(QtCore.QSize(16000, 16000))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        VentanaPrincipal.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG/travel_car_BMV_1741.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        VentanaPrincipal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabPrincipal.setObjectName("tabPrincipal")
        self.tabDrivers = QtWidgets.QWidget()
        self.tabDrivers.setObjectName("tabDrivers")
        self.frame = QtWidgets.QFrame(parent=self.tabDrivers)
        self.frame.setGeometry(QtCore.QRect(80, 10, 851, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.lblCod = QtWidgets.QLabel(parent=self.frame)
        self.lblCod.setGeometry(QtCore.QRect(20, 10, 50, 20))
        self.lblCod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCod.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblCod.setObjectName("lblCod")
        self.lblCodbd = QtWidgets.QLabel(parent=self.frame)
        self.lblCodbd.setGeometry(QtCore.QRect(78, 12, 100, 20))
        self.lblCodbd.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCodbd.setStyleSheet("background-color: rgb(253, 255, 210);")
        self.lblCodbd.setText("")
        self.lblCodbd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCodbd.setObjectName("lblCodbd")
        self.lblDni = QtWidgets.QLabel(parent=self.frame)
        self.lblDni.setGeometry(QtCore.QRect(210, 10, 23, 20))
        self.lblDni.setMinimumSize(QtCore.QSize(20, 20))
        self.lblDni.setObjectName("lblDni")
        self.txtDni = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDni.setGeometry(QtCore.QRect(250, 10, 161, 20))
        self.txtDni.setMinimumSize(QtCore.QSize(60, 20))
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.frame)
        self.lblFechaAlta.setGeometry(QtCore.QRect(600, 10, 61, 16))
        self.lblFechaAlta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.txtFechaAlta = QtWidgets.QLineEdit(parent=self.frame)
        self.txtFechaAlta.setEnabled(True)
        self.txtFechaAlta.setGeometry(QtCore.QRect(680, 10, 80, 20))
        self.txtFechaAlta.setMinimumSize(QtCore.QSize(80, 20))
        self.txtFechaAlta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtFechaAlta.setReadOnly(False)
        self.txtFechaAlta.setObjectName("txtFechaAlta")
        self.btnCalendario = QtWidgets.QPushButton(parent=self.frame)
        self.btnCalendario.setGeometry(QtCore.QRect(770, 10, 28, 20))
        self.btnCalendario.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG/descarga_calendario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCalendario.setIcon(icon1)
        self.btnCalendario.setObjectName("btnCalendario")
        self.lblApellido = QtWidgets.QLabel(parent=self.frame)
        self.lblApellido.setGeometry(QtCore.QRect(20, 50, 60, 20))
        self.lblApellido.setMinimumSize(QtCore.QSize(60, 20))
        self.lblApellido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblApellido.setObjectName("lblApellido")
        self.txtApellido = QtWidgets.QLineEdit(parent=self.frame)
        self.txtApellido.setGeometry(QtCore.QRect(80, 50, 331, 20))
        self.txtApellido.setMinimumSize(QtCore.QSize(300, 20))
        self.txtApellido.setObjectName("txtApellido")
        self.lblNombre = QtWidgets.QLabel(parent=self.frame)
        self.lblNombre.setGeometry(QtCore.QRect(490, 50, 47, 16))
        self.lblNombre.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblNombre.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblNombre.setObjectName("lblNombre")
        self.txtNombre = QtWidgets.QLineEdit(parent=self.frame)
        self.txtNombre.setGeometry(QtCore.QRect(550, 50, 251, 20))
        self.txtNombre.setMinimumSize(QtCore.QSize(120, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.lblValidarDni = QtWidgets.QLabel(parent=self.frame)
        self.lblValidarDni.setGeometry(QtCore.QRect(380, 10, 41, 21))
        self.lblValidarDni.setMinimumSize(QtCore.QSize(40, 20))
        self.lblValidarDni.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.lblValidarDni.setFont(font)
        self.lblValidarDni.setText("")
        self.lblValidarDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarDni.setObjectName("lblValidarDni")
        self.lblDireccion = QtWidgets.QLabel(parent=self.frame)
        self.lblDireccion.setGeometry(QtCore.QRect(20, 90, 60, 20))
        self.lblDireccion.setMinimumSize(QtCore.QSize(60, 20))
        self.lblDireccion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblDireccion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDireccion.setObjectName("lblDireccion")
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.frame)
        self.txtDireccion.setGeometry(QtCore.QRect(80, 90, 331, 20))
        self.txtDireccion.setMinimumSize(QtCore.QSize(300, 20))
        self.txtDireccion.setObjectName("txtDireccion")
        self.lblMovil = QtWidgets.QLabel(parent=self.frame)
        self.lblMovil.setGeometry(QtCore.QRect(30, 130, 47, 16))
        self.lblMovil.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblMovil.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblMovil.setObjectName("lblMovil")
        self.txtMovil = QtWidgets.QLineEdit(parent=self.frame)
        self.txtMovil.setGeometry(QtCore.QRect(80, 130, 120, 20))
        self.txtMovil.setMinimumSize(QtCore.QSize(120, 20))
        self.txtMovil.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtMovil.setObjectName("txtMovil")
        self.lblLocalidad = QtWidgets.QLabel(parent=self.frame)
        self.lblLocalidad.setGeometry(QtCore.QRect(620, 90, 61, 16))
        self.lblLocalidad.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblLocalidad.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.cmbLocalidad = QtWidgets.QComboBox(parent=self.frame)
        self.cmbLocalidad.setGeometry(QtCore.QRect(690, 90, 131, 22))
        self.cmbLocalidad.setObjectName("cmbLocalidad")
        self.lblProvincia = QtWidgets.QLabel(parent=self.frame)
        self.lblProvincia.setGeometry(QtCore.QRect(420, 90, 61, 16))
        self.lblProvincia.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblProvincia.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblProvincia.setObjectName("lblProvincia")
        self.cmbProvincia = QtWidgets.QComboBox(parent=self.frame)
        self.cmbProvincia.setGeometry(QtCore.QRect(490, 90, 111, 22))
        self.cmbProvincia.setObjectName("cmbProvincia")
        self.cmbProvincia.addItem("")
        self.cmbProvincia.addItem("")
        self.cmbProvincia.addItem("")
        self.cmbProvincia.addItem("")
        self.lblSalario = QtWidgets.QLabel(parent=self.frame)
        self.lblSalario.setGeometry(QtCore.QRect(220, 130, 47, 16))
        self.lblSalario.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblSalario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblSalario.setObjectName("lblSalario")
        self.txtSalario = QtWidgets.QLineEdit(parent=self.frame)
        self.txtSalario.setGeometry(QtCore.QRect(270, 130, 71, 20))
        self.txtSalario.setMinimumSize(QtCore.QSize(0, 0))
        self.txtSalario.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSalario.setObjectName("txtSalario")
        self.lblEuro = QtWidgets.QLabel(parent=self.frame)
        self.lblEuro.setGeometry(QtCore.QRect(350, 130, 16, 16))
        self.lblEuro.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblEuro.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblEuro.setObjectName("lblEuro")
        self.tabPrincipal.addTab(self.tabDrivers, "")
        self.tab_Principal = QtWidgets.QWidget()
        self.tab_Principal.setObjectName("tab_Principal")
        self.lbTab2 = QtWidgets.QLabel(parent=self.tab_Principal)
        self.lbTab2.setGeometry(QtCore.QRect(190, 210, 141, 16))
        self.lbTab2.setObjectName("lbTab2")
        self.tabPrincipal.addTab(self.tab_Principal, "")
        self.gridLayout.addWidget(self.tabPrincipal, 0, 1, 1, 1)
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=VentanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.barSalir = QtWidgets.QToolBar(parent=VentanaPrincipal)
        self.barSalir.setIconSize(QtCore.QSize(20, 20))
        self.barSalir.setObjectName("barSalir")
        VentanaPrincipal.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.barSalir)
        self.actionSalir = QtGui.QAction(parent=VentanaPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actAcerca_de = QtGui.QAction(parent=VentanaPrincipal)
        self.actAcerca_de.setObjectName("actAcerca_de")
        self.actionbarSalir = QtGui.QAction(parent=VentanaPrincipal)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../.designer/backup/IMG/imagen_salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("IMG/imagen_salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionbarSalir.setIcon(icon2)
        self.actionbarSalir.setObjectName("actionbarSalir")
        self.actionlimpiarPanel = QtGui.QAction(parent=VentanaPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../.designer/backup/IMG/reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("IMG/reload.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionlimpiarPanel.setIcon(icon3)
        self.actionlimpiarPanel.setObjectName("actionlimpiarPanel")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuHelp.addAction(self.actAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.barSalir.addSeparator()
        self.barSalir.addAction(self.actionlimpiarPanel)
        self.barSalir.addSeparator()
        self.barSalir.addAction(self.actionbarSalir)
        self.barSalir.addSeparator()

        self.retranslateUi(VentanaPrincipal)
        self.tabPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)
        VentanaPrincipal.setTabOrder(self.tabPrincipal, self.txtDni)
        VentanaPrincipal.setTabOrder(self.txtDni, self.txtFechaAlta)
        VentanaPrincipal.setTabOrder(self.txtFechaAlta, self.btnCalendario)
        VentanaPrincipal.setTabOrder(self.btnCalendario, self.txtApellido)
        VentanaPrincipal.setTabOrder(self.txtApellido, self.txtNombre)
        VentanaPrincipal.setTabOrder(self.txtNombre, self.txtDireccion)
        VentanaPrincipal.setTabOrder(self.txtDireccion, self.cmbProvincia)
        VentanaPrincipal.setTabOrder(self.cmbProvincia, self.cmbLocalidad)
        VentanaPrincipal.setTabOrder(self.cmbLocalidad, self.txtMovil)
        VentanaPrincipal.setTabOrder(self.txtMovil, self.txtSalario)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "CarTeis"))
        self.lblCod.setText(_translate("VentanaPrincipal", "Código:"))
        self.lblDni.setText(_translate("VentanaPrincipal", "DNI:"))
        self.lblFechaAlta.setText(_translate("VentanaPrincipal", "Fecha alta:"))
        self.lblApellido.setText(_translate("VentanaPrincipal", "Apellidos:"))
        self.lblNombre.setText(_translate("VentanaPrincipal", "Nombre:"))
        self.lblDireccion.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Direccion: </p></body></html>"))
        self.lblMovil.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Movil: </p></body></html>"))
        self.lblLocalidad.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Localidad: </p></body></html>"))
        self.lblProvincia.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Provincia</p></body></html>"))
        self.cmbProvincia.setItemText(0, _translate("VentanaPrincipal", "Pontevedra"))
        self.cmbProvincia.setItemText(1, _translate("VentanaPrincipal", "A Coruña"))
        self.cmbProvincia.setItemText(2, _translate("VentanaPrincipal", "Ourense"))
        self.cmbProvincia.setItemText(3, _translate("VentanaPrincipal", "Lugo"))
        self.lblSalario.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Salario: </p></body></html>"))
        self.lblEuro.setText(_translate("VentanaPrincipal", "<html><head/><body><p>€</p></body></html>"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tabDrivers), _translate("VentanaPrincipal", "CONDUCTORES"))
        self.lbTab2.setText(_translate("VentanaPrincipal", "ESTO ES LA PESTAAÑA 2"))
        self.tabPrincipal.setTabText(self.tabPrincipal.indexOf(self.tab_Principal), _translate("VentanaPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("VentanaPrincipal", "Archivo"))
        self.menuHelp.setTitle(_translate("VentanaPrincipal", "Ayuda"))
        self.barSalir.setWindowTitle(_translate("VentanaPrincipal", "toolBar"))
        self.actionSalir.setText(_translate("VentanaPrincipal", "Salir"))
        self.actAcerca_de.setText(_translate("VentanaPrincipal", "Acerca de..."))
        self.actionbarSalir.setText(_translate("VentanaPrincipal", "barSalir"))
        self.actionlimpiarPanel.setText(_translate("VentanaPrincipal", "limpiarPanel"))
