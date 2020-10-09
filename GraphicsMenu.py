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
    def __init__(self):
        super().__init__()
        self.ui = Ui_graphics_menu()
        self.ui.setupUi(self)
        self.show()

        self.botones = ['PF','HRMA_y','HRMB_y','HRMC_y','I','I0_B','PLTA','PSTA','V','W']
        #Estructura que recibe los datos del dataframe
        self.info = None
        #Lista para almacenar los headers del dataframe
        self.headers = [None]
        #Lista que guarda todas las variables de las categorias existentes
        self.variables = []

        # Listeners de los botones de la interfaz
        self.ui.PF.clicked.connect(self.graficar)
        self.ui.HRMA_y.clicked.connect(self.graficar)
        self.ui.HRMB_y.clicked.connect(self.graficar)
        self.ui.HRMC_y.clicked.connect(self.graficar)
        self.ui.I.clicked.connect(self.graficar)
        self.ui.I0_B.clicked.connect(self.graficar)
        self.ui.PLTA.clicked.connect(self.graficar)
        self.ui.PSTA.clicked.connect(self.graficar)
        self.ui.V.clicked.connect(self.graficar)
        self.ui.W.clicked.connect(self.graficar)
            
    #Metodo que recibe la informacion del merge para saber que graficas estarán disponibles y habilitarlas
    def cargarData(self,data):
        self.info = data

    # Metodo para obtener los headers de las columnas del dataframe
    def recuperarColumnas(self):
        self.headers = self.info.columns.tolist()
        #print ("headers")
        #print(self.headers)

    
    
    def comparar(self):
        self.recuperarColumnas()

        for key in self.botones:
            if key in self.headers:
                self.variables.append(key)
        self.categoriasHabilitadas()
        
    def categoriasHabilitadas(self):
        for value in self.variables:
            if value == "PF":
                self.ui.PF.setStyleSheet("border-color: black")
                self.ui.PF.setEnabled(True)
            if value == "HRMA_y":
                self.ui.HRMA_y.setStyleSheet("border-color: black")
                self.ui.HRMA_y.setEnabled(True)
            if value =="HRMB_y":
                self.ui.HRMB_y.setStyleSheet("border-color: black")
                self.ui.HRMB_y.setEnabled(True)
            if value == "HRMC_y":
                self.ui.HRMC_y.setStyleSheet("border-color: black")
                self.ui.HRMC_y.setEnabled(True)
            if value == "V":
                self.ui.V.setStyleSheet("border-color: black")
                self.ui.V.setEnabled(True)
            if value == "W":
                self.ui.W.setStyleSheet("border-color: black")
                self.ui.W.setEnabled(True)
            if value == "I":
                self.ui.I.setStyleSheet("border-color: black")
                self.ui.I.setEnabled(True)
            if value == "PSTA":
                self.ui.PSTA.setStyleSheet("border-color: black")
                self.ui.PSTA.setEnabled(True)
            if value == "PLTA":
                self.ui.PLTA.setStyleSheet("border-color: black")
                self.ui.PLTA.setEnabled(True)
            if value == "I0_B":
                self.ui.I0_B.setStyleSheet("border-color: black")
                self.ui.I0_B.setEnabled(True)
            
    
   

    #Metodo no operativo.... Se requiere verificar que se puedan graficar disntintas
    #variables
    '''def custom(self):
        self.custom = GraphicsComparison()
        self.custom.setVariables(variables=self.values)
        self.custom.show()'''
    
    
    def graficar(self):
        self.view = GraphicsView()
        self.view.setData(datos=self.info)
        self.view.setName(name=self.sender().objectName())
        self.view.plotitem()
        self.view.show()

    def closeEvent(self, event):
        if event:
            self.view.close()


        


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