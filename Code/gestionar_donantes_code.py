# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import Qt
import sys
sys.path.insert(0,'../Pyuic4/')
from gestionarDonantes import Ui_gestionarDonantes
from modificar_donante_code import ModificarDonante
import re
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtCore import pyqtSignal
from sqlalchemy import *
from math import ceil

db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')
db.echo = True
metadata = MetaData(db)
donante = Table('donante', metadata, autoload=True)
eliminar = ""

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class GestionarDonantes(QtGui.QMainWindow):
        closed = pyqtSignal()

        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_gestionarDonantes()
                self.ui.setupUi(self)
                self.text=""

        def modifiedOrDelete(self, item):
                table = item.tableWidget()
                fila = item.row()
                columna = item.column()
                item_RC = table.item(fila,0)
                if len(str(item_RC.text()))!=0:
                        if columna==5:
                                self.modificarDonanteWindow = ModificarDonante(self)
                                self.ui.horizontalLayout.removeWidget(self.ui.horizontalScrollBar)
                                self.ui.horizontalLayout.removeWidget(self.ui.label)
                                self.ui.horizontalLayout.removeWidget(self.ui.spinBox)
                                self.ui.horizontalLayout.removeWidget(self.ui.label_2)
                                self.ui.verticalLayout.removeWidget(self.ui.stackedWidget)
                                self.ui.lineEdit.setText(self.text)
                                self.modificarDonanteWindow.closed.connect(self.buscar)
                                self.modificarDonanteWindow.closed.connect(self.show)
                                self.modificarDonanteWindow.Rif_Ci = item_RC.text()
                                self.modificarDonanteWindow.ui.Rif_Ci.setText(self.modificarDonanteWindow.Rif_Ci)
                                self.modificarDonanteWindow.show()
                                self.hide()
                        elif(columna==6):
                                global eliminar
                                eliminar = str(item_RC.text())
                                self.ui._dialog = QtGui.QDialog(self)
                                self.ui._dialog.resize(400, 300)
                                self.ui._dialog.setModal(True)
                                self.ui.verticalLayout_dialog = QtGui.QVBoxLayout(self.ui._dialog)
                                self.ui.verticalLayout_dialog.setObjectName(_fromUtf8("verticalLayout_dialog"))
                                self.ui.textEdit_eli = QtGui.QTextEdit(self.ui._dialog)
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
                                self.ui.textEdit_eli.setPalette(palette)
                                self.ui.textEdit_eli.setFrameShape(QtGui.QFrame.NoFrame)
                                self.ui.textEdit_eli.setReadOnly(True)
                                self.ui.textEdit_eli.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
                                self.ui.textEdit_eli.setText("Desea eliminar el donante con RIF/CI"+item_RC.text()+"?")
                                self.ui.textEdit_eli.setObjectName(_fromUtf8("textEdit_eli"))
                                self.ui.verticalLayout_dialog.addWidget(self.ui.textEdit_eli)
                                self.ui.buttonBox = QtGui.QDialogButtonBox(self.ui._dialog)
                                self.ui.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
                                self.ui.buttonBox.setObjectName(_fromUtf8("buttonBox"))
                                self.ui.verticalLayout_dialog.addWidget(self.ui.buttonBox)
        
                                QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.eliminar)
                                QtCore.QObject.connect(self.ui.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.ui._dialog.reject)
                                QtCore.QMetaObject.connectSlotsByName(self.ui._dialog)
        
                                self.ui._dialog.show()

        def eliminar(self):
                self.delete = donante.delete().where(donante.c.donante_id==eliminar)
                db.execute(self.delete)
                self.ui._dialog.accept()
                self.buscar()

        def atras(self):
                self.hide()
                self.closed.emit()

        def buscar(self):
                if len(str(self.ui.lineEdit.text()))==0:
                        self.ui.s = select([donante]).order_by(desc(donante.c.tipo))
                        self.text=""
                        self.ui.text_anterior= self.text
                else:
                        self.text = str(self.ui.lineEdit.text())
                        if(cmp(self.text,u"Jurídico")==0):
                                self.text = "Juridico"
                        self.text = str.upper(self.text)
                        self.ui.s = select([donante]).where(or_(func.upper(donante.c.donante_id).like('%'+self.text+'%'), func.upper(donante.c.razon).like('%'+self.text+'%'),
                                func.upper(donante.c.tipo).like('%'+self.text+'%'), func.upper(donante.c.direccion).like('%'+self.text+'%'),
                                func.upper(donante.c.telefono).like('%'+self.text+'%'))).order_by(desc(donante.c.tipo))
                self.ui.result = db.execute(self.ui.s)
                self.ui.i=0
                for row in self.ui.result:
                        self.ui.i+=1
                if self.ui.i==0:
                        try:
                                self.ui.horizontalScrollBar.hide()
                                self.ui.label.hide()
                                self.ui.label_2.hide()
                                self.ui.spinBox.hide()
                                self.ui.stackedWidget.hide()
                        except:
                                pass
                else:
                        try:
                                self.ui.horizontalScrollBar.hide()
                                self.ui.label.hide()
                                self.ui.label_2.hide()
                                self.ui.spinBox.hide()
                                self.ui.stackedWidget.hide()
                        except:
                                pass
                        self.ui.text_anterior = self.text
                        self.ui.numtablas = int(ceil(self.ui.i/5.0))
                        print self.ui.numtablas
                        self.ui.numColumnas = 7
                        self.ui.numFilas = 5
                        self.ui.stackedWidget = QtGui.QStackedWidget(self.ui.centralwidget)
                        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(self.ui.stackedWidget.sizePolicy().hasHeightForWidth())
                        self.ui.stackedWidget.setSizePolicy(sizePolicy)
                        self.ui.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
                        self.ui.result = db.execute(self.ui.s)
                        row = 0
                        for x in range(0,self.ui.numtablas):
                                self.ui.page = QtGui.QWidget()
                                self.ui.page.setObjectName(_fromUtf8("page_"+str(x)))
                                self.ui.stackedWidget.addWidget(self.ui.page)
                                self.ui.verticalLayout_1 = QtGui.QHBoxLayout(self.ui.page)
                                self.ui.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_"+str(x)))
                                self.ui.tableWidget = QtGui.QTableWidget(self.ui.page)
                                self.ui.tableWidget.setAlternatingRowColors(True)
                                self.ui.tableWidget.setObjectName(_fromUtf8("tableWidget_"+str(x)))
                                self.ui.tableWidget.setColumnCount(self.ui.numColumnas)
                                self.ui.tableWidget.setRowCount(self.ui.numFilas)
                                header = self.ui.tableWidget.horizontalHeader()
                                header.setResizeMode(QHeaderView.Stretch)
                                header = self.ui.tableWidget.verticalHeader()
                                header.setResizeMode(QHeaderView.Stretch)
                                self.ui.tableWidget.setHorizontalHeaderLabels(('RIF/CI', u'Razón Solcial', 'Tipo de Donante', u'Teléfono', u'Dirección','Modificar', 'Eliminar'))
                                i=0
                                for row in self.ui.result:
                                        if i<self.ui.numFilas:
                                                for j in range(0,self.ui.numColumnas):
                                                        self.ui.label = QtGui.QLabel()
                                                        if (j==2):
                                                                if cmp(row[j],"Natural")==0:
                                                                        self.ui.label.setText("Natural")
                                                                        self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                                else:
                                                                        self.ui.label.setText(u"Jurídico")
                                                                        self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                        elif (j==5):
                                                                self.ui.label.setText("Modificar")
                                                                self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                        elif (j==6):
                                                                self.ui.label.setText("Eliminar")
                                                                self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                        else:
                                                                self.ui.label.setText(row[j])
                                                                self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                        item = self.ui.tableWidget.item(i,j)
                                                        item.setFlags(Qt.ItemIsEnabled)
                                                i+=1
                                                if i==self.ui.numFilas:
                                                        break
                                while i < self.ui.numFilas:
                                        for j in range(0,self.ui.numColumnas):
                                                self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(""))
                                                item = self.ui.tableWidget.item(i,j)
                                                item.setFlags(Qt.ItemIsEnabled)
                                        i+=1
                                QtCore.QObject.connect(self.ui.tableWidget, QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")), self.modifiedOrDelete)
                                self.ui.verticalLayout_1.addWidget(self.ui.tableWidget)
                        self.ui.verticalLayout.addWidget(self.ui.stackedWidget)
                        self.ui.horizontalLayout = QtGui.QHBoxLayout()
                        self.ui.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
                        self.ui.horizontalScrollBar = QtGui.QScrollBar(self.ui.centralwidget)
                        self.ui.horizontalScrollBar.setMaximum(self.ui.numtablas-1)
                        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(self.ui.horizontalScrollBar.sizePolicy().hasHeightForWidth())
                        self.ui.horizontalScrollBar.setSizePolicy(sizePolicy)
                        self.ui.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
                        self.ui.horizontalScrollBar.setObjectName(_fromUtf8("horizontalScrollBar"))
                        self.ui.horizontalLayout.addWidget(self.ui.horizontalScrollBar)
                        self.ui.label = QtGui.QLabel(self.ui.centralwidget)
                        self.ui.label.setObjectName(_fromUtf8("label"))
                        self.ui.label.setText("page")
                        self.ui.horizontalLayout.addWidget(self.ui.label)
                        self.ui.spinBox = QtGui.QSpinBox(self.ui.centralwidget)
                        self.ui.spinBox.setMaximum(self.ui.numtablas-1)
                        self.ui.spinBox.setObjectName(_fromUtf8("spinBox"))
                        self.ui.horizontalLayout.addWidget(self.ui.spinBox)
                        self.ui.label_2 = QtGui.QLabel(self.ui.centralwidget)
                        self.ui.label_2.setObjectName(_fromUtf8("label_2"))
                        self.ui.label_2.setText("of "+str(self.ui.numtablas-1))
                        self.ui.horizontalLayout.addWidget(self.ui.label_2)
                        self.ui.verticalLayout.addLayout(self.ui.horizontalLayout)
        
                        self.ui.stackedWidget.setCurrentIndex(0)
                        QtCore.QObject.connect(self.ui.horizontalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.ui.stackedWidget.setCurrentIndex)
                        QtCore.QObject.connect(self.ui.horizontalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.ui.spinBox.setValue)
                        QtCore.QObject.connect(self.ui.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.ui.horizontalScrollBar.setValue)
                        QtCore.QObject.connect(self.ui.stackedWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), self.ui.spinBox.setValue)

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = GestionarDonantes()
        myapp.show()
        sys.exit(app.exec_())
