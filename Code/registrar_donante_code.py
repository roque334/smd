# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
sys.path.insert(0,'../Pyuic4/')
from registrarDonante import Ui_registrarDonante
import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy import *
from PyQt4.QtGui import QPalette, QColor
from PyQt4.QtCore import pyqtSignal

db = create_engine('postgres://postgres:postgres@localhost:5432/db_fundacion')
db.echo = True
metadata = MetaData(db)
donante = Table('donante', metadata, autoload=True)

class RegistrarDonante(QtGui.QMainWindow):
        closed = pyqtSignal()

        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_registrarDonante()
                self.ui.setupUi(self)
                self.rif_ci = ""
                self.razonS = ""
                self.tipo_don = ''
                self.tipoD = ""
                self.direccionD = ""
                self.telefonoD = ""
                self.text_obs = ""
                self.telf_Malo = 0
                self.RC_Malo = 0

        """
        Verificacion de que el Rif o CI este bien escrito, coloca 1 si
        es una cedula, 2 si es un RIF juridico y 3 si el formato esta malo.
        Tambien verifica la existencia del RIF o CI en la base de datos.
        """
        def verified_Rif_Ci(self):
                self.rif_ci = str(self.ui.Rif_Ci.text())
                self.rif_ci = str.upper(self.rif_ci)
                if (re.match("^(V-|E-)[0-9]{8}$", self.rif_ci)):
                        self.RC_Malo = 1
                elif(re.match("^J-[0-9]{8}-[0-9]$",self.rif_ci)):
                        self.RC_Malo = 2
                else:
                        self.RC_Malo = 3
                if(self.RC_Malo==1 or self.RC_Malo==2):
                        s = select([donante.c.donante_id]).where(donante.c.donante_id==self.rif_ci)
                        result = db.execute(s)
                        i=0
                        for row in result:
                                i+=1
                                print row
                        if(i!=0):
                                self.ui.label_registrado.setText("Rif o CI ya existente")
                        else:
                                palette = self.ui.Rif_Ci.palette()
                                palette.setColor(QPalette.Active, QPalette.Text, QColor(0, 0, 0))
                                self.ui.Rif_Ci.setPalette(palette)
                                self.ui.label_registrado.setText("")

        """
        Coloca el valor necesario a el atributo tipo_dom de la clase.
        """
        def select_natural(self):
                self.tipo_don = 'N'
                self.tipoD = "Natural"
                self.ui.juridico.setChecked(False)

        def select_juridico(self):
                self.tipo_don = 'J'
                self.tipoD = "Juridico"
                self.ui.natural.setChecked(False)

        """
        Verifica que el telefono este bien escrito. Coloco al atributo
        telefonoD el valor 0 si es correcto o 1 si no lo es.
        
        """
        def verified_telefono(self):
                self.telefonoD = str(self.ui.telefono.text())
                if not(re.match("^0(212|412|414|416|424|426)-[0-9]{7}$", self.telefonoD)):
                        self.telf_Malo=1
                else:
                        self.tel_Malo=0

        def verifiedAndSave(self):
                self.razonS = str(self.ui.razon.text())
                self.direccionD = str(self.ui.direccion.toPlainText())
                #Caso en el que el formulario esta correcto (No toma en cuenta si el Rif esta o no registrado)
                if(len(self.rif_ci)!=0 and len(self.razonS)!=0 and 
                                len(self.direccionD)!=0 and len(self.telefonoD)!=0 and 
                                self.telf_Malo==0 and 
                                ((self.RC_Malo==1 and self.tipo_don=='N') or (self.RC_Malo==2 and self.tipo_don=='J'))):
                        ins = donante.insert().values(donante_id=self.rif_ci,razon=self.razonS, tipo=self.tipoD, direccion=self.direccionD, telefono=self.telefonoD)
                        try:
                                db.execute(ins)
                                self.ui.obs.setText(u"-Donante Registrado con éxito")
                                self.ui.Rif_Ci.setText("")
                                self.ui.razon.setText("")
                                self.ui.telefono.setText("")
                                self.ui.direccion.setText("")
                                self.ui.juridico.setChecked(False)
                                self.ui.natural.setChecked(False)
                        except IntegrityError:
                                self.ui.obs.setText(u"-El RIF o CI ya se encuentra registrado.\n")
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
