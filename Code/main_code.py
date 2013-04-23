# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys
sys.path.insert(0,'../Pyuic4/')
from main import Ui_main
from registrar_donante_code import RegistrarDonante
from gestionar_donantes_code import GestionarDonantes
from registrar_donacion_code import RegistrarDonacion

class Main(QtGui.QMainWindow):
        def __init__(self,parent=None):
                QtGui.QWidget.__init__(self,parent)
                self.ui= Ui_main()
                self.ui.setupUi(self)

        def goRegistrarDonante(self):
                self.registrarDonanteWindow = RegistrarDonante(self)
                self.registrarDonanteWindow.closed.connect(self.show)
                self.registrarDonanteWindow.show()
                self.hide()

        def goGestionarDonantes(self):
                self.gestionarDonantesWindow = GestionarDonantes(self)
                self.gestionarDonantesWindow.closed.connect(self.show)
                self.gestionarDonantesWindow.show()
                self.hide()

        def goRegistrarDonacion(self):
                self.registrarDonacionWindow = RegistrarDonacion(self)
                self.registrarDonacionWindow.closed.connect(self.show)
                self.registrarDonacionWindow.show()
                self.hide()                

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = Main()
        myapp.show()
        sys.exit(app.exec_())
