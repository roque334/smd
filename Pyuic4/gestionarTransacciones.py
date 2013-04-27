# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Ui/buscar_Donaciones.ui'
#
# Created: Mon Apr 22 16:30:06 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_gestionarTransacciones(object):
    def setupUi(self, gestionarTransacciones):
        gestionarTransacciones.setObjectName(_fromUtf8("gestionarTransacciones"))
        gestionarTransacciones.resize(1300, 700)
        self.centralwidget = QtGui.QWidget(gestionarTransacciones)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.menuButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setObjectName(_fromUtf8("menuButton"))
        self.verticalLayout.addWidget(self.menuButton)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEdit_2 = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.labelError = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelError.sizePolicy().hasHeightForWidth())
        self.labelError.setSizePolicy(sizePolicy)
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
        self.labelError.setPalette(palette)
        self.labelError.setText(_fromUtf8(""))
        self.labelError.setObjectName(_fromUtf8("labelError"))
        self.verticalLayout.addWidget(self.labelError)
        self.labelError.hide()
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.productoCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productoCombo.sizePolicy().hasHeightForWidth())
        self.productoCombo.setSizePolicy(sizePolicy)
        self.productoCombo.setObjectName(_fromUtf8("productoCombo"))
        self.horizontalLayout.addWidget(self.productoCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buscarButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buscarButton.sizePolicy().hasHeightForWidth())
        self.buscarButton.setSizePolicy(sizePolicy)
        self.buscarButton.setObjectName(_fromUtf8("buscarButton"))
        self.verticalLayout.addWidget(self.buscarButton)
        gestionarTransacciones.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(gestionarTransacciones)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        gestionarTransacciones.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(gestionarTransacciones)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        gestionarTransacciones.setStatusBar(self.statusbar)

        self.retranslateUi(gestionarTransacciones)
        QtCore.QObject.connect(self.menuButton, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarTransacciones.atras)
        QtCore.QObject.connect(self.buscarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarTransacciones.buscar)
        QtCore.QMetaObject.connectSlotsByName(gestionarTransacciones)

    def retranslateUi(self, gestionarTransacciones):
        gestionarTransacciones.setWindowTitle(_translate("gestionarTransacciones", "Gestionar Transacciones al Albergue", None))
        self.menuButton.setText(_translate("gestionarTransacciones", "Ir al Menú Principal", None))
        self.label.setText(_translate("gestionarTransacciones", "Desde:", None))
        self.label_2.setText(_translate("gestionarTransacciones", "Hasta:", None))
        self.label_3.setText(_translate("gestionarTransacciones", "Producto:", None))
        self.buscarButton.setText(_translate("gestionarTransacciones", "Buscar", None))

