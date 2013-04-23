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

class Ui_gestionarDonaciones(object):
    def setupUi(self, gestionarDonaciones):
        gestionarDonaciones.setObjectName(_fromUtf8("gestionarDonaciones"))
        gestionarDonaciones.resize(1300, 700)
        self.centralwidget = QtGui.QWidget(gestionarDonaciones)
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
        self.razonCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.razonCombo.sizePolicy().hasHeightForWidth())
        self.razonCombo.setSizePolicy(sizePolicy)
        self.razonCombo.setObjectName(_fromUtf8("razonCombo"))
        self.horizontalLayout.addWidget(self.razonCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buscarButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buscarButton.sizePolicy().hasHeightForWidth())
        self.buscarButton.setSizePolicy(sizePolicy)
        self.buscarButton.setObjectName(_fromUtf8("buscarButton"))
        self.verticalLayout.addWidget(self.buscarButton)
        gestionarDonaciones.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(gestionarDonaciones)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        gestionarDonaciones.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(gestionarDonaciones)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        gestionarDonaciones.setStatusBar(self.statusbar)

        self.retranslateUi(gestionarDonaciones)
        QtCore.QObject.connect(self.menuButton, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarDonaciones.atras)
        QtCore.QObject.connect(self.buscarButton, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarDonaciones.buscar)
        QtCore.QMetaObject.connectSlotsByName(gestionarDonaciones)

    def retranslateUi(self, gestionarDonaciones):
        gestionarDonaciones.setWindowTitle(_translate("gestionarDonaciones", "Gestionar Donaciones", None))
        self.menuButton.setText(_translate("gestionarDonaciones", "Ir al Menú Principal", None))
        self.label.setText(_translate("gestionarDonaciones", "Desde:", None))
        self.label_2.setText(_translate("gestionarDonaciones", "Hasta:", None))
        self.label_3.setText(_translate("gestionarDonaciones", "Cliente:", None))
        self.buscarButton.setText(_translate("gestionarDonaciones", "Buscar", None))

