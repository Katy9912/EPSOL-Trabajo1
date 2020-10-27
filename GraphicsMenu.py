#Se importan las librerias requeridas para la ejecución de la clase
import pandas as pd
import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

# Se importa el .py de la interfaz gráfica
from Graficas_menu import *

from GraphicsComparison import *
from Graphic_Data import *
from GraphicsView import *


class GraphicsMenu(QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(GraphicsMenu,self).__init__()

        #Esta variable guarda referencia a la interfaz "parent" de esta interfaz
        # Es necesaria para la interaccion de los botones 
        self.parent = parent

        self.ui = Ui_graphics_menu()
        self.ui.setupUi(self)
        
        #Estas dos lineas siguientes bloquean el boton cerrar de la ventana
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        
        #Se muestra la pantalla (interfaz)
        self.show()

        #Lista con el nombre de las categorias que actualmente estan definidas
        self.botones = ['PF','THDI','THDV','KF','DP','PST','PLT','WH','UH','QH','VARH','FR','MAG','ANG','IMB','MX','MN','HRMA','HRMB','HRMC','I','V','P']
        
        
        self.info = None #Estructura que recibe los datos del dataframe
        self.headers = [None] #Lista para almacenar los headers del dataframe
        self.variables = [] #Lista que guarda todas las variables de las categorias existentes 
       

        # Listeners de los botones de la interfaz
        self.ui.PF.clicked.connect(self.graficar)
        self.ui.THDI.clicked.connect(self.graficar)
        self.ui.THDV.clicked.connect(self.graficar)
        self.ui.KF.clicked.connect(self.graficar)
        self.ui.DP.clicked.connect(self.graficar)
        self.ui.PST.clicked.connect(self.graficar)
        self.ui.PLT.clicked.connect(self.graficar)
        self.ui.WH.clicked.connect(self.graficar)
        self.ui.UH.clicked.connect(self.graficar)
        self.ui.QH.clicked.connect(self.graficar)
        self.ui.VARH.clicked.connect(self.graficar)
        self.ui.FR.clicked.connect(self.graficar)
        self.ui.MAG.clicked.connect(self.graficar)
        self.ui.ANG.clicked.connect(self.graficar)
        self.ui.IMB.clicked.connect(self.graficar)
        self.ui.MX.clicked.connect(self.graficar)
        self.ui.MN.clicked.connect(self.graficar)
        self.ui.HRMA.clicked.connect(self.graficar)
        self.ui.HRMB.clicked.connect(self.graficar)
        self.ui.HRMC.clicked.connect(self.graficar)
        self.ui.I.clicked.connect(self.graficar)
        self.ui.V.clicked.connect(self.graficar)
        self.ui.P.clicked.connect(self.graficar)
        
        #El boton "Perzonalizado..." se coloca activo
        self.ui.custom_button.setStyleSheet("border-color: black") 
        self.ui.custom_button.setEnabled(True)
        self.ui.custom_button.clicked.connect(self.custom)
        
        self.ui.backButton.clicked.connect (self.back)

    
    #Metodo que recibe la informacion del merge para saber que graficas estarán disponibles y habilitarlas
    def cargarData(self,data):
        self.info = data

    # Metodo para obtener los headers de las columnas del dataframe
    def recuperarColumnas(self):
        self.recupedor = Graphic_Data()
        self.recuperados = self.recupedor.new_gra(self.info)
        self.headers = self.recuperados.columns.tolist()
       
    # Metodo que evalua que graficas estaran disponibles
    def comparar(self):
        self.recuperarColumnas()

        for key in self.botones:
            if key in self.headers:
                self.variables.append(key)            
        self.categoriasHabilitadas()
    
    #Metodo que se encarga de habilitar las categorias de graficas disponibles
    def categoriasHabilitadas(self):
        for value in self.variables:
            if value == "PF":
                self.ui.PF.setStyleSheet("border-color: black")
                self.ui.PF.setEnabled(True)
            if value == "HRMA":
                self.ui.HRMA.setStyleSheet("border-color: black")
                self.ui.HRMA.setEnabled(True)
            if value =="HRMB":
                self.ui.HRMB.setStyleSheet("border-color: black")
                self.ui.HRMB.setEnabled(True)
            if value == "HRMC":
                self.ui.HRMC.setStyleSheet("border-color: black")
                self.ui.HRMC.setEnabled(True)
            if value == "V":
                self.ui.V.setStyleSheet("border-color: black")
                self.ui.V.setEnabled(True)
            if value == "P":
                self.ui.P.setStyleSheet("border-color: black")
                self.ui.P.setEnabled(True)
            if value == "I":
                self.ui.I.setStyleSheet("border-color: black")
                self.ui.I.setEnabled(True)
            if value == "PST":
                self.ui.PST.setStyleSheet("border-color: black")
                self.ui.PST.setEnabled(True)
            if value == "PLT":
                self.ui.PLT.setStyleSheet("border-color: black")
                self.ui.PLT.setEnabled(True)
            if value == "IMB":
                self.ui.IMB.setStyleSheet("border-color: black")
                self.ui.IMB.setEnabled(True)
            if value == "THDI":
                self.ui.THDI.setStyleSheet("border-color: black")
                self.ui.THDI.setEnabled(True)
            if value == "THDV":
                self.ui.THDV.setStyleSheet("border-color: black")
                self.ui.THDV.setEnabled(True)
            if value == "KF":
                self.ui.KF.setStyleSheet("border-color: black")
                self.ui.KF.setEnabled(True)
            if value == "DP":
                self.ui.DP.setStyleSheet("border-color: black")
                self.ui.DP.setEnabled(True)
            if value == "WH":
                self.ui.WH.setStyleSheet("border-color: black")
                self.ui.WH.setEnabled(True)
            if value == "UH":
                self.ui.UH.setStyleSheet("border-color: black")
                self.ui.UH.setEnabled(True)
            if value == "QH":
                self.ui.QH.setStyleSheet("border-color: black")
                self.ui.QH.setEnabled(True)
            if value == "VARH":
                self.ui.VARH.setStyleSheet("border-color: black")
                self.ui.VARH.setEnabled(True)
            if value == "FR":
                self.ui.FR.setStyleSheet("border-color: black")
                self.ui.FR.setEnabled(True)
            if value == "MAG":
                self.ui.MAG.setStyleSheet("border-color: black")
                self.ui.MAG.setEnabled(True)
            if value == "ANG":
                self.ui.ANG.setStyleSheet("border-color: black")
                self.ui.ANG.setEnabled(True)
            if value == "MX":
                self.ui.MX.setStyleSheet("border-color: black")
                self.ui.MX.setEnabled(True)
            if value == "MN":
                self.ui.MN.setStyleSheet("border-color: black")
                self.ui.MN.setEnabled(True)    
    
    #Metodo que llama a la ventana del boton "Personalizado..."
    def custom(self):
        #En el constructor de la clase se pasan como argumento: Esta clase como "parent" y
        # La lista de headers como "variables"
        self.custom = GraphicsComparison(parent=self,variables=self.headers)
        
        #Se pasa el dataframe generado para graficar
        self.custom.setData(data=self.info)
        self.custom.show()
    
    #Metodo que llama a la interfaz para ver las grafica generada de la categoria seleccionada
    def graficar(self):
        self.view = GraphicsView(parent=self) #En el constructor se pasa esta clase como "parent"
  
        self.view.setData(datos=self.info) #Se envia como argumento: dataframe como "info"

        #Se envia como argumento: El nombre del boton clickeado para saber qué categoria se va agraficar 
        self.view.setName(name=self.sender().objectName())
        
        self.view.plotitem() #Se llama al metodo que genera la grafica
        self.view.show() #Se muestra la interfaz con la visualizacion de la grafica

    # Metodo del boton "Regresar"
    def back(self):
        #Cierra la interfaz actual
        self.close()
        #Muestra la interfaz padre (Menu Principal)
        self.parent.raise_()



'''if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    app = QtWidgets.QApplication(sys.argv)
    my_app = GraphicsMenu()
    my_app.setData(data="Hola")
    #print("Data")
    #print(my_app.getData())
    sys.exit(app.exec_())'''