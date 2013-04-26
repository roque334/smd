# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QDate
import sys
sys.path.insert(0,'../Pyuic4/')
from gestionarDonaciones import Ui_gestionarDonaciones
from modificar_donacion_code import ModificarDonacion
import re
from PyQt4.QtCore import pyqtSignal
from sqlalchemy import *
from math import ceil
import datetime

db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')
db.echo = True
metadata = MetaData(db)
donante = Table('donante', metadata, autoload=True)
monetaria = Table('monetaria', metadata, autoload=True)
mobiliaria = Table('mobiliaria', metadata, autoload=True)
especie = Table('especie', metadata, autoload=True)
eliminar_id = ""
eliminar_tabla = ""

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class GestionarDonaciones(QtGui.QMainWindow):
        closed = pyqtSignal()
        fecha1_anterior=""
        fecha2_anterior=""
        select_anterior=""

        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_gestionarDonaciones()
                self.ui.setupUi(self)

                temp = datetime.datetime.now()
                date3 = str(temp.year)+"-"+str(temp.month)+"-"+str(temp.day)
                now = datetime.datetime.strptime(date3, "%Y-%m-%d")
                self.ui.dateEdit_2.setDate(QtCore.QDate(now.date()))
                self.ui.razonCombo.addItem("Seleccione")
                self.s1 = select([donante.c.razon])
                result1 = db.execute(self.s1)
                self.i = 0
                for row in result1:
                        self.ui.razonCombo.addItem(row[0])
                        self.i+=1

        def modifiedOrDelete(self, item):
                table = item.tableWidget()
                fila = item.row()
                columna = item.column()
                item_id = table.item(fila,0)
                item_tabla = table.item(fila,1)
                if len(str(item_id.text()))!=0: #Contiene el identificador del item seleccionado.
                        
                        if columna==6:
                                eliminar_id = str(item_id.text())
                                eliminar_tabla = str(item_tabla.text())
                                if(cmp(eliminar_tabla,"monetaria"))==0:
                                    
                                    s = select([monetaria]).where(monetaria.c.monetaria_id==eliminar_id)
                                    result = db.execute(s)
                                    for row in result:
                                        numero= row['nro']
                                        concepto=row['concepto']
                                        tipo_mon=row['tipo_op']
                                        monto=row['monto']
                                        razon_nom = row['donante_id']
                                        print row

                                    if(tipo_mon=='B'):
                                        flag = 1
                                    elif(tipo_mon=='C'):
                                        flag = 2
                                    elif(tipo_mon=='E'):
                                        flag = 3
                                    else:
                                        flag = 4    

                                    self.modificarDonacionWindow = ModificarDonacion(self)
                                    try:
                                            self.ui.horizontalScrollBar.hide()
                                            self.ui.label.hide()
                                            self.ui.label_2.hide()
                                            self.ui.spinBox.hide()
                                            self.ui.stackedWidget.hide()
                                    except:
                                            pass
                                    #self.ui.razonCombo.setCurrentIndex(self.ui.razonCombo.findText(select_anterior, Qt.MatchExactly))
                                    self.modificarDonacionWindow.closed.connect(self.buscar)
                                    self.modificarDonacionWindow.closed.connect(self.show)
                                    self.modificarDonacionWindow.Rif_Ci = razon_nom
                                    self.modificarDonacionWindow.ui.Rif_Ci.setText(self.modificarDonacionWindow.Rif_Ci)
                                    self.modificarDonacionWindow.ui.monetaria.setChecked(True)
                                    self.modificarDonacionWindow.concepto=concepto
                                    self.modificarDonacionWindow.ui.concepto.setText(self.modificarDonacionWindow.concepto)
                                    self.modificarDonacionWindow.ui.tipoMonetaria.setCurrentIndex(flag)
                                    self.modificarDonacionWindow.numero=numero
                                    self.modificarDonacionWindow.ui.numero.setEnabled(True)
                                    self.modificarDonacionWindow.ui.label_num.setEnabled(True)
                                    self.modificarDonacionWindow.ui.numero.setText(self.modificarDonacionWindow.numero)
                                    self.modificarDonacionWindow.Serial="C"+eliminar_id
                                    self.modificarDonacionWindow.ui.Serial.setText(self.modificarDonacionWindow.Serial)
                                    self.modificarDonacionWindow.cantidad_monto=str(monto)
                                    self.modificarDonacionWindow.ui.cantidad_monto.setText(self.modificarDonacionWindow.cantidad_monto)
                                    self.modificarDonacionWindow.show()
                                    self.hide()        

                                elif(cmp(eliminar_tabla,"mobiliaria"))==0:
                                    s = select([mobiliaria]).where(mobiliaria.c.mobiliaria_id==eliminar_id)
                                    result = db.execute(s)
                                    for row in result:
                                        
                                        concepto=row['concepto']
                                        
                                        monto=row['cant']
                                        razon_nom = row['donante_id']
                                        print row
                                    self.modificarDonacionWindow = ModificarDonacion(self)
                                    try:
                                            self.ui.horizontalScrollBar.hide()
                                            self.ui.label.hide()
                                            self.ui.label_2.hide()
                                            self.ui.spinBox.hide()
                                            self.ui.stackedWidget.hide()
                                    except:
                                            pass
                                    #self.ui.razonCombo.setCurrentIndex(self.ui.razonCombo.findText(select_anterior, Qt.MatchExactly))
                                    self.modificarDonacionWindow.closed.connect(self.buscar)
                                    self.modificarDonacionWindow.closed.connect(self.show)
                                    self.modificarDonacionWindow.Rif_Ci = razon_nom
                                    self.modificarDonacionWindow.ui.Rif_Ci.setText(self.modificarDonacionWindow.Rif_Ci)
                                    self.modificarDonacionWindow.ui.tipoMonetaria.setEnabled(False)
                                    self.modificarDonacionWindow.ui.mobiliaria.setChecked(True)
                                    self.modificarDonacionWindow.concepto=concepto
                                    self.modificarDonacionWindow.ui.concepto.setText(self.modificarDonacionWindow.concepto)
                                    self.modificarDonacionWindow.Serial="M"+eliminar_id
                                    self.modificarDonacionWindow.ui.Serial.setText(self.modificarDonacionWindow.Serial)
                                    self.modificarDonacionWindow.cantidad_monto=str(monto)
                                    self.modificarDonacionWindow.ui.cantidad_monto.setText(self.modificarDonacionWindow.cantidad_monto)
                                    self.modificarDonacionWindow.show()
                                    self.hide()        

                                else:
                                    s = select([especie]).where(especie.c.especie_id==eliminar_id)
                                    result = db.execute(s)
                                    for row in result:
                                        
                                        concepto=row['concepto']
                                        
                                        monto=row['cant']
                                        razon_nom = row['donante_id']
                                        print row
                                    self.modificarDonacionWindow = ModificarDonacion(self)
                                    try:
                                            self.ui.horizontalScrollBar.hide()
                                            self.ui.label.hide()
                                            self.ui.label_2.hide()
                                            self.ui.spinBox.hide()
                                            self.ui.stackedWidget.hide()
                                    except:
                                            pass
                                    #self.ui.razonCombo.setCurrentIndex(self.ui.razonCombo.findText(select_anterior, Qt.MatchExactly))
                                    self.modificarDonacionWindow.closed.connect(self.buscar)
                                    self.modificarDonacionWindow.closed.connect(self.show)
                                    self.modificarDonacionWindow.Rif_Ci = razon_nom
                                    self.modificarDonacionWindow.ui.Rif_Ci.setText(self.modificarDonacionWindow.Rif_Ci)
                                    self.modificarDonacionWindow.ui.especie.setChecked(True)
                                    self.modificarDonacionWindow.ui.tipoMonetaria.setEnabled(False)
                                    self.modificarDonacionWindow.concepto=concepto
                                    self.modificarDonacionWindow.ui.concepto.setText(self.modificarDonacionWindow.concepto)
                                    self.modificarDonacionWindow.Serial= "E"+eliminar_id
                                    self.modificarDonacionWindow.ui.Serial.setText(self.modificarDonacionWindow.Serial)
                                    self.modificarDonacionWindow.cantidad_monto=str(monto)
                                    self.modificarDonacionWindow.ui.cantidad_monto.setText(self.modificarDonacionWindow.cantidad_monto)
                                    self.modificarDonacionWindow.show()
                                    self.hide()   
                                
                                
                                
                        elif(columna==7):
                                global eliminar_id, eliminar_tabla
                                eliminar_id = str(item_id.text())
                                eliminar_tabla = str(item_tabla.text())
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
                                self.ui.textEdit_eli.setText("Desea eliminar la donacion de la fila "+str(fila+1)+"?")
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
                if(cmp(eliminar_tabla,"monetaria"))==0:
                        self.delete = monetaria.delete().where(monetaria.c.monetaria_id==eliminar_id)
                elif(cmp(eliminar_tabla,"mobiliaria"))==0:
                        self.delete = mobiliaria.delete().where(mobiliaria.c.mobiliaria_id==eliminar_id)
                else:
                        self.delete = especie.delete().where(especie.c.especie_id==eliminar_id)
                db.execute(self.delete)
                self.ui._dialog.accept()
                self.buscar()

        def atras(self):
                self.hide()
                self.closed.emit()

        def buscar(self):
                var_temp = self.ui.dateEdit.date()
                date1 = str(var_temp.toPyDate())
                var_temp = self.ui.dateEdit_2.date()
                date2 = str(var_temp.toPyDate())
                fecha1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                fecha2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
                temp = datetime.datetime.now()
                date3 = str(temp.year)+"-"+str(temp.month)+"-"+str(temp.day)
                now = datetime.datetime.strptime(date3, "%Y-%m-%d")
                if (fecha1<=fecha2) and (fecha2<=now):
                        self.ui.labelError.hide()
                        if(cmp(str(self.ui.razonCombo.currentText()),"Seleccione")==0):
                                print "hola"
                                s1 = text("SELECT monetaria.monetaria_id, 'monetaria' , donante.razon, monetaria.concepto, monetaria.monto, monetaria.fecha AS col "
                                                "FROM donante NATURAL JOIN monetaria "
                                                "WHERE :fechaI <= monetaria.fecha AND monetaria.fecha <= :fechaF "
                                        "UNION "
                                        "SELECT mobiliaria.mobiliaria_id, 'mobiliaria' , donante.razon, mobiliaria.concepto, mobiliaria.cant, mobiliaria.fecha AS col "
                                                "FROM donante NATURAL JOIN mobiliaria "
                                                "WHERE :fechaI <= mobiliaria.fecha AND mobiliaria.fecha <= :fechaF "
                                        "UNION "
                                        "SELECT especie.especie_id, 'especie' , donante.razon, especie.concepto, especie.cant, especie.fecha AS col "
                                                "FROM donante NATURAL JOIN especie "
                                                "WHERE :fechaI <= especie.fecha AND especie.fecha <= :fechaF "
                                        "ORDER BY col DESC "
                                                )
                                result1 = db.execute(s1, fechaI = fecha1, fechaF = fecha2)
                                result2 = db.execute(s1, fechaI = fecha1, fechaF = fecha2)
                        else:
                                print "hi"
                                s1 = text("SELECT monetaria.monetaria_id, 'monetaria' , donante.razon, monetaria.concepto, monetaria.monto, monetaria.fecha AS col "
                                                "FROM donante NATURAL JOIN monetaria "
                                                "WHERE donante.razon = :razon "
                                                "AND :fechaI <= monetaria.fecha AND monetaria.fecha <= :fechaF "
                                        "UNION "
                                        "SELECT mobiliaria.mobiliaria_id, 'mobiliaria'  ,donante.razon, mobiliaria.concepto, mobiliaria.cant, mobiliaria.fecha AS col "
                                                "FROM donante NATURAL JOIN mobiliaria "
                                                "WHERE donante.razon = :razon "
                                                "AND :fechaI <= mobiliaria.fecha AND mobiliaria.fecha <= :fechaF "
                                        "UNION "
                                        "SELECT especie.especie_id, 'especie', donante.razon ,especie.concepto, especie.cant, especie.fecha AS col "
                                                "FROM donante NATURAL JOIN especie "
                                                "WHERE donante.razon = :razon "
                                                "AND :fechaI <= especie.fecha AND especie.fecha <= :fechaF "
                                        "ORDER BY col DESC "
                                                )
                                result1 = db.execute(s1, razon = str(self.ui.razonCombo.currentText()), fechaI = fecha1, fechaF = fecha2)
                                result2 = db.execute(s1, razon = str(self.ui.razonCombo.currentText()), fechaI = fecha1, fechaF = fecha2)
                        z = 0
                        for row in result1:
                                z+=1

                        if(z==0):
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
                                self.fecha1_ant = fecha1
                                self.fecha2_ant = fecha2
                                self.select_ant = str(self.ui.razonCombo.currentText())
                                #Creacion Tabla
                                self.ui.numColumnas = 8
                                self.ui.numFilas = 5
                                self.ui.numtablas = int(ceil(z/float(self.ui.numFilas)))
                                print self.ui.numtablas
                                self.ui.stackedWidget = QtGui.QStackedWidget(self.ui.centralwidget)
                                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
                                sizePolicy.setHorizontalStretch(0)
                                sizePolicy.setVerticalStretch(0)
                                sizePolicy.setHeightForWidth(self.ui.stackedWidget.sizePolicy().hasHeightForWidth())
                                self.ui.stackedWidget.setSizePolicy(sizePolicy)
                                self.ui.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
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
                                        self.ui.tableWidget.setHorizontalHeaderLabels(('ID','Tabla',u'Razón Solcial', 'Concepto', 'Monto o Cantidad','Fecha','Modificar', 'Eliminar'))
                                        i=0
                                        for row in result2:
                                                if i<self.ui.numFilas:
                                                        for j in range(0,self.ui.numColumnas):
                                                                self.ui.label = QtGui.QLabel()
                                                                if (j==6):
                                                                        self.ui.label.setText("Modificar")
                                                                        self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                                elif (j==7):
                                                                        self.ui.label.setText("Eliminar")
                                                                        self.ui.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(self.ui.label.text()))
                                                                else:
                                                                        self.ui.label.setText(str(row[j]))
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
                                        self.ui.tableWidget.hideColumn(0)
                                        self.ui.tableWidget.hideColumn(1)
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
                else:
                        try:
                                self.ui.horizontalScrollBar.hide()
                                self.ui.label.hide()
                                self.ui.label_2.hide()
                                self.ui.spinBox.hide()
                                self.ui.stackedWidget.hide()
                        except:
                                pass
                        self.ui.labelError.show()
                        if(fecha1>now or fecha2>now):
                                self.ui.labelError.setText("Las fechas deben ser menor a la fecha actual ("+date3+").")
                        else:
                                self.ui.labelError.setText("La fecha \"Desde\" debe ser menor o igual a la fecha \"Hasta\".")

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = GestionarDonaciones()
        myapp.show()
        sys.exit(app.exec_())
