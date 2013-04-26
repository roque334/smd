# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
sys.path.insert(0,'../Pyuic4/')
from modificarDonacion import Ui_modificarDonacion
from registrar_donante_code import RegistrarDonante
import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy import *
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignal
from datetime import *

db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')
db.echo = True
metadata = MetaData(db)
donante = Table('donante', metadata, autoload=True)
monetaria = Table('monetaria', metadata, autoload=True)
mobiliaria = Table('mobiliaria', metadata, autoload=True)
especie = Table('especie', metadata, autoload=True)

class ModificarDonacion(QtGui.QMainWindow):
        closed = pyqtSignal()

        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_modificarDonacion()
                self.ui.setupUi(self)
                self.razon_nom= ""
                self.tipo_don = ''
                self.tipo_mon= ''
                self.num=""
                self.cant_monto= 0.0
                self.fecha= ""
                self.rif_ci = ""
                self.concep = ""
                self.text_obs = ""
                self.RC_Malo = 0

        def verified_Rif_Ci(self):
                self.ui.razon_nombre.setText("")
                self.rif_ci = str(self.ui.Rif_Ci.text())
                self.rif_ci = str.upper(self.rif_ci)
                if (re.match("^(V-|E-)[0-9]{8}$", self.rif_ci)):
                        self.RC_Malo = 1
                elif(re.match("^J-[0-9]{8}-[0-9]$",self.rif_ci)):
                        self.RC_Malo = 2
                elif(len(self.rif_ci)==0):
                        self.RC_Malo = 3
                        self.ui.label_registrado.setText("RIF/CI Vacio") 
                else:
                        self.RC_Malo = 3
                        self.razon_nom = ""
                        self.ui.razon_nombre.setText("")
                        self.ui.label_registrado.setText("Rif o CI con formato INCORRECTO")        

                if(self.RC_Malo==1 or self.RC_Malo==2):
                        s = select([donante]).where(donante.c.donante_id==self.rif_ci)
                        result = db.execute(s)
                        i=0
                        razon_nom= ""
                        
                        for row in result:
                                i+=1
                                razon_nom = row['razon']
                                print row
                        if(i!=0):
                                self.razon_nom = razon_nom
                                self.ui.razon_nombre.setText(razon_nom)
                                self.ui.label_tipo_don.setEnabled(True)
                                self.ui.especie.setEnabled(True)
                                self.ui.mobiliaria.setEnabled(True)
                                self.ui.monetaria.setEnabled(True)

                                self.ui.especie.setCheckable(True)
                                self.ui.mobiliaria.setCheckable(True)
                                self.ui.monetaria.setCheckable(True)
                                self.ui.label_registrado.setText("")
                                
                        else:
                                self.ui.label_registrado.setText("Rif o CI no registrado")
                                self.RC_Malo = 0
                                self.razon_nom = ""
                                self.ui.irAgregar.setEnabled(True)
                                self.ui.razon_nombre.setText("")
                               
                                self.ui.especie.setChecked(False)
                                self.ui.mobiliaria.setChecked(False)
                                self.ui.monetaria.setChecked(False)
                                self.ui.label_tipo_don.setEnabled(False)
                                self.ui.especie.setEnabled(False)
                                self.ui.mobiliaria.setEnabled(False)
                                self.ui.monetaria.setEnabled(False)
                                self.ui.tipoMonetaria.setEnabled(False)
                                self.ui.label_cantmon.setEnabled(False)
                                #self.ui.cantidad_monto.setText("")
                                self.ui.cantidad_monto.setEnabled(False)
                                self.ui.label_concep.setEnabled(False)
                                #self.ui.concepto.setText("")
                                self.ui.concepto.setEnabled(False)
                                self.ui.label_fecha.setEnabled(False)
                                self.ui.campoFecha.setEnabled(False)
                                self.ui.label_ayuda_fecha.setEnabled(False)

        def goRegistrarDonante(self):
                self.registrarDonanteWindow = RegistrarDonante(self)
                self.registrarDonanteWindow.ui.Rif_Ci.setText(self.rif_ci)
                self.registrarDonanteWindow.closed.connect(self.show)
                self.registrarDonanteWindow.show()
                self.hide()
                self.ui.irAgregar.setEnabled(False)
                

        def select_especie(self):
                self.ui.numero.setText("")
                self.ui.cantidad_monto.setText("")
                self.ui.concepto.setText("")
                self.ui.tipoMonetaria.setEnabled(False)
                self.ui.label_cantmon.setEnabled(False)
             
                self.ui.numero.setEnabled(False)             
                self.ui.label_num.setEnabled(False)

                self.tipo_don = u'E'
                self.ui.especie.setChecked(True)
                self.ui.mobiliaria.setChecked(False)
                self.ui.monetaria.setChecked(False)

                self.ui.label_cantmon.setEnabled(True)
                self.ui.cantidad_monto.setEnabled(True)
                self.ui.label_concep.setEnabled(True)
                self.ui.concepto.setEnabled(True)                
                self.ui.label_fecha.setEnabled(True)
                self.ui.campoFecha.setEnabled(True)
                self.ui.label_ayuda_fecha.setEnabled(True)
                print "hola"

        def select_mobiliaria(self):
                self.ui.numero.setText("")
                self.ui.cantidad_monto.setText("")
                self.ui.concepto.setText("")
                self.ui.tipoMonetaria.setEnabled(False)
                self.ui.label_cantmon.setEnabled(False)
             
                self.ui.numero.setEnabled(False)             
                self.ui.label_num.setEnabled(False)

                self.tipo_don = u'M'
                self.ui.especie.setChecked(False)
                self.ui.mobiliaria.setChecked(True)
                self.ui.monetaria.setChecked(False)

                self.ui.label_cantmon.setEnabled(True)
                self.ui.cantidad_monto.setEnabled(True)
                self.ui.label_concep.setEnabled(True)
                self.ui.concepto.setEnabled(True)                
                self.ui.label_fecha.setEnabled(True)
                self.ui.campoFecha.setEnabled(True)
                self.ui.label_ayuda_fecha.setEnabled(True)
                print "hola"

        def select_monetario(self):        
                
                self.ui.cantidad_monto.setText("")
                self.ui.concepto.setText("")
                self.tipo_don = u'C'
                self.ui.especie.setChecked(False)
                self.ui.mobiliaria.setChecked(False)
                self.ui.monetaria.setChecked(True)
                
                self.ui.tipoMonetaria.setEnabled(True)
                self.ui.label_cantmon.setEnabled(True)
             
                self.ui.numero.setEnabled(True)             
                self.ui.label_num.setEnabled(True)
                self.ui.cantidad_monto.setEnabled(True)
                self.ui.label_concep.setEnabled(True)
                self.ui.concepto.setEnabled(True)                
                self.ui.label_fecha.setEnabled(True)
                self.ui.campoFecha.setEnabled(True)
                self.ui.label_ayuda_fecha.setEnabled(True)
                print "hola"

        def guardar_tipoMon(self):
                tipo_donacion= str(self.ui.tipoMonetaria.currentText())
                tipo_monetaria= tipo_donacion[0]
                if(tipo_monetaria=='S'):
                        self.ui.textEdit.setText("Seleccione el tipo de Donacion Monetaria")
                else:
                        self.tipo_mon=tipo_monetaria        


        def verifiedAndSave(self):
                _serial= str(self.ui.Serial.text())
                _tipo=_serial[0]
                _idTable=_serial[1:]
                # extraer el primer numero
                self.concep=str(self.ui.concepto.text())
                self.num= str(self.ui.numero.text())
                montofloat= self.ui.cantidad_monto.text()
                if(len(self.rif_ci)!=0 and len(self.razon_nom)!=0 and 
                                len(montofloat)!=0 and len(self.concep)!=0 and self.tipo_mon!=''):
                        
                        self.cant_monto=float(montofloat)
                        
                        vartemp= self.ui.campoFecha.date() 
                        vartemp= str(vartemp.toPyDate())
                        self.fecha= vartemp
                        if(self.tipo_don=='E'and cmp(self.tipo_don,_tipo)==0):
                                ins = especie.update().where(especie.c.especie_id==_serial).values(concepto=self.concep, cant=self.cant_monto, fecha=self.fecha,donante_id=self.rif_ci)
                                ins.compile().params
                                try:
                                        db.execute(ins)
                                        self.ui.textEdit.setText(u"-Donacion modificada con éxito")
                                        self.ui.Rif_Ci.setText("")
                                        self.ui.razon_nombre.setText("")
                                        self.ui.irAgregar.setEnabled(False)
                                        self.ui.especie.setChecked(False)
                                        self.ui.mobiliaria.setChecked(False)
                                        self.ui.monetaria.setChecked(False)
                                        self.ui.label_tipo_don.setEnabled(False)
                                        self.ui.especie.setEnabled(False)
                                        self.ui.mobiliaria.setEnabled(False)
                                        self.ui.monetaria.setEnabled(False)
                                        self.ui.tipoMonetaria.setEnabled(False)
                                        self.ui.label_cantmon.setEnabled(False)
                                        self.ui.cantidad_monto.setText("")
                                        self.ui.cantidad_monto.setEnabled(False)
                                        self.ui.label_concep.setEnabled(False)
                                        self.ui.concepto.setText("")
                                        self.ui.concepto.setEnabled(False)
                                        self.ui.label_fecha.setEnabled(False)
                                        self.ui.campoFecha.setEnabled(False)
                                        self.ui.label_ayuda_fecha.setEnabled(False)
                                   
                                except IntegrityError:
                                        self.ui.textEdit.setText(u"-La donacion ya esta registrada.\n")
                        elif(self.tipo_don=='M' and cmp(self.tipo_don,_tipo)==0):

                                ins = mobiliaria.insert().values(concepto=self.concep, cant=self.cant_monto, fecha=self.fecha,donante_id=self.rif_ci)
                                ins.compile().params
                                try:
                                        db.execute(ins)
                                        self.ui.textEdit.setText(u"-Donacion Registrada con éxito")
                                        self.ui.Rif_Ci.setText("")
                                        self.ui.razon_nombre.setText("")
                                        self.ui.irAgregar.setEnabled(False)
                                        self.ui.especie.setChecked(False)
                                        self.ui.mobiliaria.setChecked(False)
                                        self.ui.monetaria.setChecked(False)
                                        self.ui.label_tipo_don.setEnabled(False)
                                        self.ui.especie.setEnabled(False)
                                        self.ui.mobiliaria.setEnabled(False)
                                        self.ui.monetaria.setEnabled(False)
                                        self.ui.tipoMonetaria.setEnabled(False)
                                        self.ui.label_cantmon.setEnabled(False)
                                        self.ui.cantidad_monto.setText("")
                                        self.ui.cantidad_monto.setEnabled(False)
                                        self.ui.label_concep.setEnabled(False)
                                        self.ui.concepto.setText("")
                                        self.ui.concepto.setEnabled(False)
                                        self.ui.label_fecha.setEnabled(False)
                                        self.ui.campoFecha.setEnabled(False)
                                        self.ui.label_ayuda_fecha.setEnabled(False)

                                except IntegrityError:
                                        self.ui.textEdit.setText(u"-La donacion ya esta registrada.\n\n")
                        elif(self.tipo_don=='C' and cmp(self.tipo_don,_tipo)==0  and len(self.num)!=0):    

                                ins = monetaria.insert().values(concepto=self.concep,nro=self.num,tipo_op=self.tipo_mon, monto=self.cant_monto, fecha=self.fecha, donante_id=self.rif_ci)
                                ins.compile().params
                                try:
                                        db.execute(ins)
                                        self.ui.textEdit.setText(u"-Donacion Registrada con éxito")
                                        self.ui.Rif_Ci.setText("")
                                        self.ui.razon_nombre.setText("")
                                        self.ui.irAgregar.setEnabled(False)
                                        self.ui.especie.setChecked(False)
                                        self.ui.mobiliaria.setChecked(False)
                                        self.ui.monetaria.setChecked(False)
                                        self.ui.label_tipo_don.setEnabled(False)
                                        self.ui.especie.setEnabled(False)
                                        self.ui.mobiliaria.setEnabled(False)
                                        self.ui.monetaria.setEnabled(False)
                                        self.ui.tipoMonetaria.setEnabled(False)
                                        self.ui.numero.setText("")
                                        self.ui.numero.setEnabled(False)             
                                        self.ui.label_num.setEnabled(False)
                                        self.ui.label_cantmon.setEnabled(False)
                                        self.ui.cantidad_monto.setText("")
                                        self.ui.cantidad_monto.setEnabled(False)
                                        self.ui.label_concep.setEnabled(False)
                                        self.ui.concepto.setText("")
                                        self.ui.concepto.setEnabled(False)
                                        self.ui.label_fecha.setEnabled(False)
                                        self.ui.campoFecha.setEnabled(False)
                                        self.ui.label_ayuda_fecha.setEnabled(False)
                                        
                                except IntegrityError:
                                        self.ui.textEdit.setText(u"-La donacion ya esta registrada.\n\n")

                        else:
                                elf.text_obs+=u"-Campo Numero vacio.\n"                                        
                                self.ui.textEdit.setText(self.text_obs)  
                else:
                        #Caso en el que falta algo por llegar o algo esta malo.
                        self.text_obs=""
                        if(len(self.rif_ci)==0):
                                self.text_obs+=u"-Campo de RIF o CI vacío.\n"
                        if(self.tipo_don!='E' and self.tipo_don!='M' and self.tipo_don!='C'):
                                self.text_obs+=u"-Seleccione el tipo de donacion.\n"
                        if(len(self.tipo_mon)==0 and self.tipo_don=='C'):
                                self.text_obs+=u"-Seleccione el tipo de donacion monetario.\n"
                        if(len(self.concep)==0):
                                self.text_obs+=u"-Campo concepto vacío.\n"
                        if(len(montofloat)==0):
                                self.text_obs+=u"-Campo cantidad/monto vacío.\n"
                                                               
                        self.ui.textEdit.setText(self.text_obs)

        def cancel(self):
                self.hide()
                self.closed.emit()
