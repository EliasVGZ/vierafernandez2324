# Form implementation generated from reading ui file '.\templates\venta_principal.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(1107, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(VentanaPrincipal.sizePolicy().hasHeightForWidth())
        VentanaPrincipal.setSizePolicy(sizePolicy)
        VentanaPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        VentanaPrincipal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        VentanaPrincipal.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/travel_car_BMV_1741.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/travel_car_BMV_1741.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        VentanaPrincipal.setWindowIcon(icon)
        VentanaPrincipal.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(160000, 160000))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panelPrincipal = QtWidgets.QTabWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.panelPrincipal.sizePolicy().hasHeightForWidth())
        self.panelPrincipal.setSizePolicy(sizePolicy)
        self.panelPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        self.panelPrincipal.setMaximumSize(QtCore.QSize(1028, 674))
        self.panelPrincipal.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.panelPrincipal.setObjectName("panelPrincipal")
        self.panelDrivers = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelDrivers.sizePolicy().hasHeightForWidth())
        self.panelDrivers.setSizePolicy(sizePolicy)
        self.panelDrivers.setMaximumSize(QtCore.QSize(1200, 900))
        self.panelDrivers.setObjectName("panelDrivers")
        self.frame = QtWidgets.QFrame(parent=self.panelDrivers)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1021, 212))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(900, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 141, 983, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbltipoCarnet = QtWidgets.QLabel(parent=self.layoutWidget)
        self.lbltipoCarnet.setMaximumSize(QtCore.QSize(100, 20))
        self.lbltipoCarnet.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lbltipoCarnet.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lbltipoCarnet.setObjectName("lbltipoCarnet")
        self.horizontalLayout_5.addWidget(self.lbltipoCarnet)
        self.chkA = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkA.setMaximumSize(QtCore.QSize(40, 20))
        self.chkA.setObjectName("chkA")
        self.horizontalLayout_5.addWidget(self.chkA)
        self.chkB = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkB.setMaximumSize(QtCore.QSize(40, 20))
        self.chkB.setObjectName("chkB")
        self.horizontalLayout_5.addWidget(self.chkB)
        self.chkC = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkC.setMaximumSize(QtCore.QSize(40, 20))
        self.chkC.setObjectName("chkC")
        self.horizontalLayout_5.addWidget(self.chkC)
        self.chkD = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.chkD.setMaximumSize(QtCore.QSize(40, 20))
        self.chkD.setObjectName("chkD")
        self.horizontalLayout_5.addWidget(self.chkD)
        spacerItem = QtWidgets.QSpacerItem(728, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(14, 170, 989, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btnAltaDriver = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btnAltaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnAltaDriver.setObjectName("btnAltaDriver")
        self.horizontalLayout_6.addWidget(self.btnAltaDriver)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btnModifDriver = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btnModifDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnModifDriver.setObjectName("btnModifDriver")
        self.horizontalLayout_6.addWidget(self.btnModifDriver)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.btnBajaDriver = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.btnBajaDriver.setMinimumSize(QtCore.QSize(75, 20))
        self.btnBajaDriver.setObjectName("btnBajaDriver")
        self.horizontalLayout_6.addWidget(self.btnBajaDriver)
        spacerItem4 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(17, 12, 938, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblCod = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.lblCod.setMinimumSize(QtCore.QSize(50, 20))
        self.lblCod.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lblCod.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblCod.setObjectName("lblCod")
        self.horizontalLayout_2.addWidget(self.lblCod)
        self.lblCodbd = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.lblCodbd.setMinimumSize(QtCore.QSize(100, 20))
        self.lblCodbd.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lblCodbd.setStyleSheet("background-color: rgb(253, 255, 210);")
        self.lblCodbd.setText("")
        self.lblCodbd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblCodbd.setObjectName("lblCodbd")
        self.horizontalLayout_2.addWidget(self.lblCodbd)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lblDni = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.lblDni.setMinimumSize(QtCore.QSize(20, 20))
        self.lblDni.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lblDni.setObjectName("lblDni")
        self.horizontalLayout_2.addWidget(self.lblDni)
        self.txtDni = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.txtDni.setMinimumSize(QtCore.QSize(60, 20))
        self.txtDni.setMaximumSize(QtCore.QSize(170, 16777215))
        self.txtDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtDni.setObjectName("txtDni")
        self.horizontalLayout_2.addWidget(self.txtDni)
        self.lblValidarDni = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.lblValidarDni.setMinimumSize(QtCore.QSize(20, 20))
        self.lblValidarDni.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.lblValidarDni.setFont(font)
        self.lblValidarDni.setText("")
        self.lblValidarDni.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblValidarDni.setObjectName("lblValidarDni")
        self.horizontalLayout_2.addWidget(self.lblValidarDni)
        spacerItem6 = QtWidgets.QSpacerItem(288, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.lblFechaAlta = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.lblFechaAlta.setMaximumSize(QtCore.QSize(52, 16777215))
        self.lblFechaAlta.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblFechaAlta.setObjectName("lblFechaAlta")
        self.horizontalLayout_2.addWidget(self.lblFechaAlta)
        self.txtFechaAlta = QtWidgets.QLineEdit(parent=self.layoutWidget2)
        self.txtFechaAlta.setEnabled(True)
        self.txtFechaAlta.setMinimumSize(QtCore.QSize(100, 20))
        self.txtFechaAlta.setMaximumSize(QtCore.QSize(110, 16777215))
        self.txtFechaAlta.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtFechaAlta.setReadOnly(False)
        self.txtFechaAlta.setObjectName("txtFechaAlta")
        self.horizontalLayout_2.addWidget(self.txtFechaAlta)
        self.btnCalendario = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.btnCalendario.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnCalendario.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../../../.designer/IMG/descarga_calendario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/descarga_calendario.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.btnCalendario.setIcon(icon1)
        self.btnCalendario.setObjectName("btnCalendario")
        self.horizontalLayout_2.addWidget(self.btnCalendario)
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(9, 51, 971, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblApellido = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.lblApellido.setMinimumSize(QtCore.QSize(0, 20))
        self.lblApellido.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lblApellido.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblApellido.setObjectName("lblApellido")
        self.horizontalLayout_3.addWidget(self.lblApellido)
        self.txtApellido = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.txtApellido.setMinimumSize(QtCore.QSize(350, 20))
        self.txtApellido.setMaximumSize(QtCore.QSize(350, 16777215))
        self.txtApellido.setObjectName("txtApellido")
        self.horizontalLayout_3.addWidget(self.txtApellido)
        spacerItem7 = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.txtNombre.setMinimumSize(QtCore.QSize(200, 20))
        self.txtNombre.setMaximumSize(QtCore.QSize(200, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.horizontalLayout_3.addWidget(self.txtNombre)
        self.layoutWidget4 = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 80, 1011, 24))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.lblDireccion = QtWidgets.QLabel(parent=self.layoutWidget4)
        self.lblDireccion.setMinimumSize(QtCore.QSize(60, 20))
        self.lblDireccion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblDireccion.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDireccion.setObjectName("lblDireccion")
        self.horizontalLayout_4.addWidget(self.lblDireccion)
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.layoutWidget4)
        self.txtDireccion.setMinimumSize(QtCore.QSize(350, 20))
        self.txtDireccion.setMaximumSize(QtCore.QSize(315, 16777215))
        self.txtDireccion.setObjectName("txtDireccion")
        self.horizontalLayout_4.addWidget(self.txtDireccion)
        spacerItem9 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.lblProvincia = QtWidgets.QLabel(parent=self.layoutWidget4)
        self.lblProvincia.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblProvincia.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblProvincia.setObjectName("lblProvincia")
        self.horizontalLayout_4.addWidget(self.lblProvincia)
        self.cmbProvincia = QtWidgets.QComboBox(parent=self.layoutWidget4)
        self.cmbProvincia.setMinimumSize(QtCore.QSize(140, 0))
        self.cmbProvincia.setObjectName("cmbProvincia")
        self.horizontalLayout_4.addWidget(self.cmbProvincia)
        self.lblLocalidad = QtWidgets.QLabel(parent=self.layoutWidget4)
        self.lblLocalidad.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblLocalidad.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblLocalidad.setObjectName("lblLocalidad")
        self.horizontalLayout_4.addWidget(self.lblLocalidad)
        self.cmbLocalidad = QtWidgets.QComboBox(parent=self.layoutWidget4)
        self.cmbLocalidad.setMinimumSize(QtCore.QSize(170, 0))
        self.cmbLocalidad.setMaximumSize(QtCore.QSize(170, 16777215))
        self.cmbLocalidad.setObjectName("cmbLocalidad")
        self.horizontalLayout_4.addWidget(self.cmbLocalidad)
        spacerItem10 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setGeometry(QtCore.QRect(16, 110, 991, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblMovil = QtWidgets.QLabel(parent=self.widget)
        self.lblMovil.setMinimumSize(QtCore.QSize(55, 0))
        self.lblMovil.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lblMovil.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblMovil.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblMovil.setObjectName("lblMovil")
        self.horizontalLayout_7.addWidget(self.lblMovil)
        self.txtMovil = QtWidgets.QLineEdit(parent=self.widget)
        self.txtMovil.setMinimumSize(QtCore.QSize(120, 20))
        self.txtMovil.setMaximumSize(QtCore.QSize(150, 16777215))
        self.txtMovil.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtMovil.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txtMovil.setObjectName("txtMovil")
        self.horizontalLayout_7.addWidget(self.txtMovil)
        self.lblSalario = QtWidgets.QLabel(parent=self.widget)
        self.lblSalario.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lblSalario.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblSalario.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblSalario.setObjectName("lblSalario")
        self.horizontalLayout_7.addWidget(self.lblSalario)
        self.txtSalario = QtWidgets.QLineEdit(parent=self.widget)
        self.txtSalario.setMinimumSize(QtCore.QSize(85, 0))
        self.txtSalario.setMaximumSize(QtCore.QSize(60, 16777215))
        self.txtSalario.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.txtSalario.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.txtSalario.setObjectName("txtSalario")
        self.horizontalLayout_7.addWidget(self.txtSalario)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem11 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.lblEstado = QtWidgets.QLabel(parent=self.widget)
        self.lblEstado.setMaximumSize(QtCore.QSize(60, 20))
        self.lblEstado.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblEstado.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lblEstado.setObjectName("lblEstado")
        self.horizontalLayout_7.addWidget(self.lblEstado)
        self.rbtTodos = QtWidgets.QRadioButton(parent=self.widget)
        self.rbtTodos.setMinimumSize(QtCore.QSize(80, 0))
        self.rbtTodos.setChecked(True)
        self.rbtTodos.setObjectName("rbtTodos")
        self.buttonGroup = QtWidgets.QButtonGroup(VentanaPrincipal)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbtTodos)
        self.horizontalLayout_7.addWidget(self.rbtTodos)
        self.rbtAlta = QtWidgets.QRadioButton(parent=self.widget)
        self.rbtAlta.setObjectName("rbtAlta")
        self.buttonGroup.addButton(self.rbtAlta)
        self.horizontalLayout_7.addWidget(self.rbtAlta)
        self.rbtBaja = QtWidgets.QRadioButton(parent=self.widget)
        self.rbtBaja.setObjectName("rbtBaja")
        self.buttonGroup.addButton(self.rbtBaja)
        self.horizontalLayout_7.addWidget(self.rbtBaja)
        spacerItem12 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.tabDrivers = QtWidgets.QTableWidget(parent=self.panelDrivers)
        self.tabDrivers.setGeometry(QtCore.QRect(0, 230, 1021, 431))
        self.tabDrivers.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tabDrivers.setLineWidth(3)
        self.tabDrivers.setMidLineWidth(3)
        self.tabDrivers.setAlternatingRowColors(True)
        self.tabDrivers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tabDrivers.setObjectName("tabDrivers")
        self.tabDrivers.setColumnCount(6)
        self.tabDrivers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabDrivers.setHorizontalHeaderItem(5, item)
        self.tabDrivers.verticalHeader().setVisible(False)
        self.panelPrincipal.addTab(self.panelDrivers, "")
        self.tab_Principal = QtWidgets.QWidget()
        self.tab_Principal.setObjectName("tab_Principal")
        self.lbTab2 = QtWidgets.QLabel(parent=self.tab_Principal)
        self.lbTab2.setGeometry(QtCore.QRect(190, 210, 141, 16))
        self.lbTab2.setObjectName("lbTab2")
        self.panelPrincipal.addTab(self.tab_Principal, "")
        self.horizontalLayout.addWidget(self.panelPrincipal)
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=VentanaPrincipal)
        self.statusbar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 21))
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
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../../../../../Documents/Desenvolvemento Interfaces/imagenes/imagen_salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/imagen_salir.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionbarSalir.setIcon(icon2)
        self.actionbarSalir.setObjectName("actionbarSalir")
        self.actionlimpiarPanel = QtGui.QAction(parent=VentanaPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../../../../.designer/IMG/limpiar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(".\\templates\\../IMG/limpiar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
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
        self.panelPrincipal.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)
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
        self.lbltipoCarnet.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Tipo de Carnet: </p></body></html>"))
        self.chkA.setText(_translate("VentanaPrincipal", "A"))
        self.chkB.setText(_translate("VentanaPrincipal", "B"))
        self.chkC.setText(_translate("VentanaPrincipal", "C"))
        self.chkD.setText(_translate("VentanaPrincipal", "D"))
        self.btnAltaDriver.setText(_translate("VentanaPrincipal", "Alta"))
        self.btnModifDriver.setText(_translate("VentanaPrincipal", "Modificar"))
        self.btnBajaDriver.setText(_translate("VentanaPrincipal", "Baja"))
        self.lblCod.setText(_translate("VentanaPrincipal", "Código:"))
        self.lblDni.setText(_translate("VentanaPrincipal", "DNI:"))
        self.lblFechaAlta.setText(_translate("VentanaPrincipal", "Fecha alta:"))
        self.lblApellido.setText(_translate("VentanaPrincipal", "Apellidos:"))
        self.label.setText(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" font-size:8pt;\">Nombre: </span></p></body></html>"))
        self.lblDireccion.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Direccion: </p></body></html>"))
        self.lblProvincia.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Provincia: </p></body></html>"))
        self.lblLocalidad.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Localidad: </p></body></html>"))
        self.lblMovil.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Movil: </p></body></html>"))
        self.lblSalario.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Salario: </p></body></html>"))
        self.label_2.setText(_translate("VentanaPrincipal", "<html><head/><body><p>(00000000.00)</p></body></html>"))
        self.lblEstado.setText(_translate("VentanaPrincipal", "<html><head/><body><p>Histórico:</p></body></html>"))
        self.rbtTodos.setText(_translate("VentanaPrincipal", "Todos"))
        self.rbtAlta.setText(_translate("VentanaPrincipal", "Alta"))
        self.rbtBaja.setText(_translate("VentanaPrincipal", "Baja"))
        item = self.tabDrivers.horizontalHeaderItem(0)
        item.setText(_translate("VentanaPrincipal", "Codigo"))
        item = self.tabDrivers.horizontalHeaderItem(1)
        item.setText(_translate("VentanaPrincipal", "Apellidos"))
        item = self.tabDrivers.horizontalHeaderItem(2)
        item.setText(_translate("VentanaPrincipal", "Nombre"))
        item = self.tabDrivers.horizontalHeaderItem(3)
        item.setText(_translate("VentanaPrincipal", "Móvil"))
        item = self.tabDrivers.horizontalHeaderItem(4)
        item.setText(_translate("VentanaPrincipal", "Licencias"))
        item = self.tabDrivers.horizontalHeaderItem(5)
        item.setText(_translate("VentanaPrincipal", "Fecha Baja"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.panelDrivers), _translate("VentanaPrincipal", "CONDUCTORES"))
        self.lbTab2.setText(_translate("VentanaPrincipal", "ESTO ES LA PESTAAÑA 2"))
        self.panelPrincipal.setTabText(self.panelPrincipal.indexOf(self.tab_Principal), _translate("VentanaPrincipal", "Tab 2"))
        self.menuArchivo.setTitle(_translate("VentanaPrincipal", "Archivo"))
        self.menuHelp.setTitle(_translate("VentanaPrincipal", "Ayuda"))
        self.barSalir.setWindowTitle(_translate("VentanaPrincipal", "toolBar"))
        self.actionSalir.setText(_translate("VentanaPrincipal", "Salir"))
        self.actAcerca_de.setText(_translate("VentanaPrincipal", "Acerca de..."))
        self.actionbarSalir.setText(_translate("VentanaPrincipal", "barSalir"))
        self.actionlimpiarPanel.setText(_translate("VentanaPrincipal", "limpiarPanel"))
