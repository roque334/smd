# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
sys.path.insert(0,'../Pyuic4/')
from modificarDonante import Ui_modificarDonante
import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy import *
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtCore import pyqtSignal

db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')
db.echo = True
metadata = MetaData(db)
donante = Table('donante', metadata, autoload=True)

class ModificarDonante(QtGui.QMainWindow):
        closed = pyqtSignal()

        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_modificarDonante()
                self.ui.setupUi(self)
                self.rif_ci = ""
                self.razonS = ""
                self.tipoD = ""
                self.tipo_don = ''
                self.direccionD = ""
                self.telefonoD = ""
                self.text_obs = ""
                self.telf_Malo = 0
                self.RC_Malo = 0

        def verified_Rif_Ci(self):
                self.rif_ci = str(self.ui.Rif_Ci.text())
                self.rif_ci = str.upper(self.rif_ci)
                if (re.match("^(V-|E-)[0-9]{8}$", self.rif_ci)):
                        self.RC_Malo = 1
                elif(re.match("^J-[0-9]{8}-[0-9]$",self.rif_ci)):
                        self.RC_Malo = 2

                if(self.RC_Malo==1 or self.RC_Malo==2):
                        s = select([donante]).where(donante.c.donante_id==self.rif_ci)
                        result = db.execute(s)
                        i=0
                        razonS = ""
                        telf = ""
                        tipoD = ''
                        direccion = ""
                        for row in result:
                                i+=1
                                razonS = row['razon']
                                telf = row['telefono']
                                tipoD = row['tipo']
                                direccion = row['direccion']
                                print row
                        if(i!=0):
                                self.razonS = razonS
                                self.ui.razon.setText(razonS)

                                self.telefonoD = telf
                                self.ui.telefono.setText(telf)

                                self.direccionD = direccion
                                self.ui.direccion.setText(direccion)

                                self.tipoD = tipoD
                                if(cmp(tipoD,u'Natural')==0):
                                        self.tipo_don = u'N'
                                        self.ui.natural.setChecked(True)
                                        self.ui.juridico.setChecked(False)
                                else:
                                        self.tipo_don = u'J'
                                        self.ui.juridico.setChecked(True)
                                        self.ui.natural.setChecked(False)

        def select_natural(self):
                if(self.tipo_don!=''):
                        self.tipoD = "Natural"
                        self.tipo_don = u'N'
                        self.ui.natural.setChecked(True)
                        self.ui.juridico.setChecked(False)
                        print "hola"

        def select_juridico(self):
                if(self.tipo_don!=''):
                        self.tipoD = "Juridico"
                        self.tipo_don = u'J'
                        self.ui.natural.setChecked(True)
                        self.ui.juridico.setChecked(False)
                        print "hola"

        def verified_telefono(self):
                self.telefonoD = str(self.ui.telefono.text())
                if not(re.match("^0(212|412|414|416|424|426)-[0-9]{7}$", self.telefonoD)):
                        self.telf_Malo=1
                else:
                        self.tel_Malo=0

        def verifiedAndSave(self):
                if(self.tipo_don=='' and (self.RC_Malo==1 or self.RC_Malo==2)):
                        self.ui.obs.setText("El RIF/CI no se encuentra registrado por lo que no se puede modificar.")
                elif(self.RC_Malo!=1 and self.RC_Malo!=2 and len(self.rif_ci)!=0):
                        self.ui.obs.setText("El formato del RIF/CI es incorrecto.")
                elif(self.RC_Malo!=1 and self.RC_Malo!=2 and len(self.rif_ci)==0):
                        self.ui.obs.setText(u"Campo de RIF/CI vacío, debe ingresar uno válido para que pueda modificar los datos del donante.")
                else:
                        self.razonS = str(self.ui.razon.text())
                        self.direccionD = str(self.ui.direccion.toPlainText())
                        #Caso en el que el formulario esta correcto (No toma en cuenta si el Rif esta o no registrado)
                        if(len(self.rif_ci)!=0 and len(self.razonS)!=0 and 
                                        len(self.direccionD)!=0 and len(self.telefonoD)!=0 and 
                                        self.telf_Malo==0 and 
                                        ((self.RC_Malo==1 and self.tipo_don=='N') or (self.RC_Malo==2 and self.tipo_don=='J'))):
                                ins = donante.update().where(donante.c.donante_id==self.rif_ci).values(razon=self.razonS, tipo=self.tipoD, direccion=self.direccionD, telefono=self.telefonoD)
                                db.execute(ins)
                                self.ui.obs.setText(u"-Donante modificado con éxito")
                        else:
                                #Caso en el que falta algo por llegar o algo esta malo.
                                self.text_obs=""
                                if(len(self.rif_ci)!=0 and self.RC_Malo==1 and self.tipo_don=='J'):
                                        self.text_obs+=u"-El donante es tipo Jurídico, pero su RIF no sigue el formato indicado.\n"
                                elif(len(self.rif_ci)!=0 and self.RC_Malo==2 and self.tipo_don=='N'):
                                        self.text_obs+=u"-El donante es tipo Natural, pero su CI no sigue el formato indicado.\n"
                                else:
                                        if(len(self.rif_ci)==0):
                                                self.text_obs+=u"-Campo de RIF o CI vacío.\n"
                                        else:
                                                if(self.RC_Malo==3):
                                                        self.text_obs+=u"-Formato de RIF o CI incorrecto\n"
                                        if(self.tipo_don!='N' and self.tipo_don!='J'):
                                                self.text_obs+=u"-Seleccione el tipo de donante.\n"
                                if(len(self.razonS)==0):
                                        self.text_obs+=u"-Campo de Razón Social vacío.\n"
                                if(len(self.direccionD)==0):
                                        self.text_obs+=u"-Campo Dirección vacío.\n"
                                if(len(self.telefonoD)==0):
                                        self.text_obs+=u"-Campo Teléfono vacío.\n"
                                else:
                                        if self.telf_Malo==1:
                                                self.text_obs+=u"-Formato de teléfono incorrecto.\n"
                                self.ui.obs.setText(self.text_obs)

        def cancel(self):
                self.hide()
                self.closed.emit()
