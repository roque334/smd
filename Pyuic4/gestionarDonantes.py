# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Ui/gestionar_donantes.ui'
#
# Created: Thu Apr 18 19:05:49 2013
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

class Ui_gestionarDonantes(object):
    text_anterior = ""
    def setupUi(self, gestionarDonantes):
        gestionarDonantes.setObjectName(_fromUtf8("gestionarDonantes"))
        gestionarDonantes.resize(1300, 700)
        self.centralwidget = QtGui.QWidget(gestionarDonantes)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_atras = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_atras.sizePolicy().hasHeightForWidth())
        self.pushButton_atras.setSizePolicy(sizePolicy)
        self.pushButton_atras.setText(u"Ir al Menú Principal")
        self.pushButton_atras.setObjectName(_fromUtf8("pushButton_atras"))
        self.verticalLayout.addWidget(self.pushButton_atras)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.lineEdit = QtGui.QLineEdit()
        self.lineEdit.setObjectName(_fromUtf8("lineEditBuscar"))
        self.horizontalLayout_1.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton()
        self.pushButton.setObjectName(_fromUtf8("pushButtonBuscar"))
        self.pushButton.setText("Buscar")
        self.horizontalLayout_1.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_1)
        gestionarDonantes.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(gestionarDonantes)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        gestionarDonantes.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(gestionarDonantes)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        gestionarDonantes.setStatusBar(self.statusbar)

        self.retranslateUi(gestionarDonantes)
        QtCore.QObject.connect(self.pushButton_atras, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarDonantes.atras)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), gestionarDonantes.buscar)
        QtCore.QMetaObject.connectSlotsByName(gestionarDonantes)

    def retranslateUi(self, gestionarDonantes):
        gestionarDonantes.setWindowTitle(_translate("gestionarDonantes", "Gestionar Donantes", None))
