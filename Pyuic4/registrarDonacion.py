# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrar_donacion.ui'
#
# Created: Tue Apr 23 17:23:51 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_registrarDonacion(object):
    def setupUi(self, registrarDonacion):
        registrarDonacion.setObjectName(_fromUtf8("registrarDonacion"))
        registrarDonacion.resize(1300, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(registrarDonacion.sizePolicy().hasHeightForWidth())
        registrarDonacion.setSizePolicy(sizePolicy)
        self.form_2 = QtGui.QWidget(registrarDonacion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.form_2.sizePolicy().hasHeightForWidth())
        self.form_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.form_2.setFont(font)
        self.form_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.form_2.setObjectName(_fromUtf8("form_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.form_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.form = QtGui.QFormLayout()
        self.form.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.form.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.form.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.form.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.form.setFormAlignment(QtCore.Qt.AlignCenter)
        self.form.setMargin(9)
        self.form.setHorizontalSpacing(9)
        self.form.setObjectName(_fromUtf8("form"))
        self.label_4 = QtGui.QLabel(self.form_2)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("../Code/ImgFundacion.JPG")))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.form.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.form.setWidget(1, QtGui.QFormLayout.SpanningRole, self.label_3)
        self.label_RIF = QtGui.QLabel(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_RIF.sizePolicy().hasHeightForWidth())
        self.label_RIF.setSizePolicy(sizePolicy)
        self.label_RIF.setObjectName(_fromUtf8("label_RIF"))
        self.form.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_RIF)
        self.gridWidget = QtGui.QWidget(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Rif_Ci = QtGui.QLineEdit(self.gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Rif_Ci.sizePolicy().hasHeightForWidth())
        self.Rif_Ci.setSizePolicy(sizePolicy)
        self.Rif_Ci.setObjectName(_fromUtf8("Rif_Ci"))
        self.gridLayout_3.addWidget(self.Rif_Ci, 1, 0, 1, 1)
        self.irAgregar = QtGui.QPushButton(self.gridWidget)
        self.irAgregar.setEnabled(False)
        self.irAgregar.setObjectName(_fromUtf8("irAgregar"))
        self.gridLayout_3.addWidget(self.irAgregar, 1, 1, 1, 1)
        self.form.setWidget(3, QtGui.QFormLayout.FieldRole, self.gridWidget)
        self.label = QtGui.QLabel(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.form.setWidget(4, QtGui.QFormLayout.FieldRole, self.label)
        self.label_registrado = QtGui.QLabel(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_registrado.sizePolicy().hasHeightForWidth())
        self.label_registrado.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(250, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_registrado.setPalette(palette)
        self.label_registrado.setText(_fromUtf8(""))
        self.label_registrado.setObjectName(_fromUtf8("label_registrado"))
        self.form.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_registrado)
        self.razon_nombre = QtGui.QLineEdit(self.form_2)
        self.razon_nombre.setEnabled(True)
        self.razon_nombre.setReadOnly(True)
        self.razon_nombre.setObjectName(_fromUtf8("razon_nombre"))
        self.form.setWidget(6, QtGui.QFormLayout.FieldRole, self.razon_nombre)
        self.label_tipo_don = QtGui.QLabel(self.form_2)
        self.label_tipo_don.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tipo_don.sizePolicy().hasHeightForWidth())
        self.label_tipo_don.setSizePolicy(sizePolicy)
        self.label_tipo_don.setObjectName(_fromUtf8("label_tipo_don"))
        self.form.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_tipo_don)
        self.gridWidget1 = QtGui.QWidget(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget1.sizePolicy().hasHeightForWidth())
        self.gridWidget1.setSizePolicy(sizePolicy)
        self.gridWidget1.setObjectName(_fromUtf8("gridWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.gridWidget1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.monetaria = QtGui.QRadioButton(self.gridWidget1)
        self.monetaria.setEnabled(False)
        self.monetaria.setCheckable(False)
        self.monetaria.setObjectName(_fromUtf8("monetaria"))
        self.gridLayout.addWidget(self.monetaria, 4, 0, 1, 1)
        self.mobiliaria = QtGui.QRadioButton(self.gridWidget1)
        self.mobiliaria.setEnabled(False)
        self.mobiliaria.setCheckable(False)
        self.mobiliaria.setObjectName(_fromUtf8("mobiliaria"))
        self.gridLayout.addWidget(self.mobiliaria, 2, 0, 1, 1)
        self.especie = QtGui.QRadioButton(self.gridWidget1)
        self.especie.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.especie.sizePolicy().hasHeightForWidth())
        self.especie.setSizePolicy(sizePolicy)
        self.especie.setCheckable(False)
        self.especie.setObjectName(_fromUtf8("especie"))
        self.gridLayout.addWidget(self.especie, 1, 0, 1, 1)
        self.tipoMonetaria = QtGui.QComboBox(self.gridWidget1)
        self.tipoMonetaria.setEnabled(False)
        self.tipoMonetaria.setAutoFillBackground(False)
        self.tipoMonetaria.setEditable(False)
        self.tipoMonetaria.setObjectName(_fromUtf8("tipoMonetaria"))
        self.tipoMonetaria.addItem(_fromUtf8(""))
        self.tipoMonetaria.addItem(_fromUtf8(""))
        self.tipoMonetaria.addItem(_fromUtf8(""))
        self.tipoMonetaria.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.tipoMonetaria, 4, 1, 1, 1)
        self.form.setWidget(7, QtGui.QFormLayout.FieldRole, self.gridWidget1)
        self.label_cantmon = QtGui.QLabel(self.form_2)
        self.label_cantmon.setEnabled(False)
        self.label_cantmon.setObjectName(_fromUtf8("label_cantmon"))
        self.form.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_cantmon)
        self.cantidad_monto = QtGui.QLineEdit(self.form_2)
        self.cantidad_monto.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cantidad_monto.sizePolicy().hasHeightForWidth())
        self.cantidad_monto.setSizePolicy(sizePolicy)
        self.cantidad_monto.setReadOnly(False)
        self.cantidad_monto.setObjectName(_fromUtf8("cantidad_monto"))
        self.form.setWidget(9, QtGui.QFormLayout.FieldRole, self.cantidad_monto)
        self.label_concep = QtGui.QLabel(self.form_2)
        self.label_concep.setEnabled(False)
        self.label_concep.setObjectName(_fromUtf8("label_concep"))
        self.form.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_concep)
        self.concepto = QtGui.QLineEdit(self.form_2)
        self.concepto.setEnabled(False)
        self.concepto.setObjectName(_fromUtf8("concepto"))
        self.form.setWidget(10, QtGui.QFormLayout.FieldRole, self.concepto)
        self.label_fecha = QtGui.QLabel(self.form_2)
        self.label_fecha.setEnabled(False)
        self.label_fecha.setObjectName(_fromUtf8("label_fecha"))
        self.form.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_fecha)
        self.gridWidget2 = QtGui.QWidget(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget2.sizePolicy().hasHeightForWidth())
        self.gridWidget2.setSizePolicy(sizePolicy)
        self.gridWidget2.setObjectName(_fromUtf8("gridWidget2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridWidget2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_ayuda_fecha = QtGui.QLabel(self.gridWidget2)
        self.label_ayuda_fecha.setEnabled(False)
        self.label_ayuda_fecha.setObjectName(_fromUtf8("label_ayuda_fecha"))
        self.gridLayout_2.addWidget(self.label_ayuda_fecha, 0, 2, 1, 1)
        self.campoFecha = QtGui.QDateEdit(self.gridWidget2)
        self.campoFecha.setEnabled(False)
        self.campoFecha.setObjectName(_fromUtf8("campoFecha"))
        self.gridLayout_2.addWidget(self.campoFecha, 0, 1, 1, 1)
        self.form.setWidget(11, QtGui.QFormLayout.FieldRole, self.gridWidget2)
        self.label_campo1 = QtGui.QLabel(self.form_2)
        self.label_campo1.setEnabled(False)
        self.label_campo1.setText(_fromUtf8(""))
        self.label_campo1.setObjectName(_fromUtf8("label_campo1"))
        self.form.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_campo1)
        self.label_2 = QtGui.QLabel(self.form_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.form.setWidget(13, QtGui.QFormLayout.LabelRole, self.label_2)
        self.textEdit = QtGui.QTextEdit(self.form_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.form.setWidget(13, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.pushButton = QtGui.QPushButton(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.form.setWidget(16, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.form_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.form.setWidget(16, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.label_5 = QtGui.QLabel(self.form_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.form.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.verticalLayout.addLayout(self.form)
        registrarDonacion.setCentralWidget(self.form_2)
        self.menubar = QtGui.QMenuBar(registrarDonacion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        registrarDonacion.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(registrarDonacion)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        registrarDonacion.setStatusBar(self.statusbar)

        self.retranslateUi(registrarDonacion)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.verifiedAndSave)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.cancel)
        QtCore.QObject.connect(self.Rif_Ci, QtCore.SIGNAL(_fromUtf8("editingFinished()")), registrarDonacion.verified_Rif_Ci)
        QtCore.QObject.connect(self.monetaria, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.select_monetario)
        QtCore.QObject.connect(self.mobiliaria, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.select_mobiliaria)
        QtCore.QObject.connect(self.especie, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.select_especie)
        QtCore.QObject.connect(self.irAgregar, QtCore.SIGNAL(_fromUtf8("clicked()")), registrarDonacion.goRegistrarDonante)
        QtCore.QObject.connect(self.tipoMonetaria, QtCore.SIGNAL(_fromUtf8("activated(QString)")), registrarDonacion.guardar_tipoMon)
        QtCore.QMetaObject.connectSlotsByName(registrarDonacion)

    def retranslateUi(self, registrarDonacion):
        registrarDonacion.setWindowTitle(QtGui.QApplication.translate("registrarDonacion", "Registrar Donante", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("registrarDonacion", "Registrar Donación", None, QtGui.QApplication.UnicodeUTF8))
        self.label_RIF.setText(QtGui.QApplication.translate("registrarDonacion", "RIF/CI:", None, QtGui.QApplication.UnicodeUTF8))
        self.irAgregar.setText(QtGui.QApplication.translate("registrarDonacion", "Ir a Agregar Donante", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("registrarDonacion", "-Natural: V-12345678 o E-12345678   -Jurídica:J-12345678-9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tipo_don.setText(QtGui.QApplication.translate("registrarDonacion", "Tipo de Donación:", None, QtGui.QApplication.UnicodeUTF8))
        self.monetaria.setText(QtGui.QApplication.translate("registrarDonacion", "Monetaria", None, QtGui.QApplication.UnicodeUTF8))
        self.mobiliaria.setText(QtGui.QApplication.translate("registrarDonacion", "Mobiliaria", None, QtGui.QApplication.UnicodeUTF8))
        self.especie.setText(QtGui.QApplication.translate("registrarDonacion", "Especie", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoMonetaria.setItemText(0, QtGui.QApplication.translate("registrarDonacion", "Baucher", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoMonetaria.setItemText(1, QtGui.QApplication.translate("registrarDonacion", "Cheque", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoMonetaria.setItemText(2, QtGui.QApplication.translate("registrarDonacion", "Efectivo", None, QtGui.QApplication.UnicodeUTF8))
        self.tipoMonetaria.setItemText(3, QtGui.QApplication.translate("registrarDonacion", "Transferencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_cantmon.setText(QtGui.QApplication.translate("registrarDonacion", "Cantidad/Monto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_concep.setText(QtGui.QApplication.translate("registrarDonacion", "Concepto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fecha.setText(QtGui.QApplication.translate("registrarDonacion", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ayuda_fecha.setText(QtGui.QApplication.translate("registrarDonacion", "aaaa-mm-dd", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("registrarDonacion", "Observaciones del Sistema:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("registrarDonacion", "Registrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("registrarDonacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("registrarDonacion", "Razón/Nombre:", None, QtGui.QApplication.UnicodeUTF8))
