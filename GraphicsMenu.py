#Se importan las librerias requeridas para la ejecución de la clase
import pandas as pd
import numpy as np
import os

# Se importa el .py de la interfaz gráfica
from Scripts.App_V2.Graphics_menu import *

from Scripts.App_V2.GraphicsComparison import *
from Scripts.App_V2.Graphic_Data import *


class GraphicsMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_graphics_menu()
        self.ui.setupUi(self)
        self.show()
        
        #Estructura que recibe los datos del dataframe
        self.info = None
        #Lista para almacenar los headers del dataframe
        self.headers = [None]
        #Diccionario para almacenar la estructura de mediciones
        self.diccionario = {None} 
        #Lista para almacenar las "keys" provenientes del diccionario
        self.keys = [None]
        #Lista que guarda todas las variables de las categorias existentes
        self.variables = []

        # Listeners de los botones de la interfaz
        '''self.ui.energy_Q_button.clicked.connect()
        self.ui.harmonics_button.clicked.connect()
        self.ui.potency_button.clicked.connect()
        self.ui.potency_factor_button.clicked.connect()
        self.ui.thd_button.clicked.connect()
        self.ui.energy_U_button.clicked.connect()
        self.ui.energy_VAR_button.clicked.connect()
        self.ui.energy_W_button.clicked.connect()
        self.ui.voltage_button.clicked.connect()
        self.ui.voltage_history_button.clicked.connect()
        self.ui.voltage_unbalance_button.clicked.connect()
        self.ui.current_angle_button.clicked.connect()
        self.ui.current_button.clicked.connect()
        self.ui.current_history_button.clicked.connect()
        self.ui.current_magnitude_button.clicked.connect()
        self.ui.current_unbalance_button.clicked.connect()
        self.ui.frecuency_button.clicked.connect()
        self.ui.harmonic_distortion_button.clicked.connect()
        self.ui.k_factor_button.clicked.connect()
        self.ui.potency_distortion_factor_button.clicked.connect()
        self.ui.potency_history_buttonclicked.connect()
        self.ui.flicker_button.clicked.connect()'''
        self.ui.custom_button.clicked.connect(self.custom)

        
        

    
    #Metodo que recibe la informacion del merge para saber que graficas estarán disponibles y habilitarlas
    def cargarData(self,data):
        self.info = data

    # Metodo para obtener los headers de las columnas del dataframe
    def recuperarColumnas(self):
        self.headers = self.info.columns.tolist()

    def obtenerParaComparar(self):
        self.graphicData = Graphic_Data()
        self.diccionario = self.graphicData.mediciones_dict
        
    def activarOpciones(self):
        #Se recuperan los headers del dataframe generado
        self.recuperarColumnas()
        #Se obtiene el diccionario de variables
        self.obtenerParaComparar()
        #Se obtiene la lista de las llaves del diccionario
        self.keys = list(self.diccionario.keys())
        #Se inicializa contador
        found = 0
        #Se recorre el diccionario
        for key in self.diccionario:
            #Se obtiene la lista de los valores relacionados con la "key" actual
            values = list(self.diccionario[key])
            #Se obtiene el numero de valores relacionados a la "key" actual
            elements = len(values)
            #Se recorre la lista de valores 
            for item in values:
                #Se compara si los elementos de la lista "values" están en la lista de "headers"
                if item in self.headers:
                    #Se lleva la cuenta de elementos encontrados en los "headers"
                    found += 1
                    self.variables.append(item)
            #Si no se encuentran todas las variables todas las variables relacionadas con la "key" actual en "headers"       
            if found == elements:
                #Se remueve la llave de la lista "keys"
                self.keys.remove(key)
            #Se reinicia contador de elementos encontrados
            found = 0
        print(self.variables)
        self.categoriasDeshabilitadas()

    def categoriasDeshabilitadas(self):
        for value in self.keys:
            if value == "PF":
                self.ui.potency_factor_button.setStyleSheet("background-color: gray")
                self.ui.potency_factor_button.setEnabled(False)
            if value == "HRMA" or "HRMB" or "HRMC":
                self.ui.harmonics_button.setStyleSheet("background-color: gray")
                self.ui.harmonics_button.setEnabled(False)
            if value == "Voltages":
                self.ui.voltage_button.setStyleSheet("background-color: gray")
                self.ui.voltage_button.setEnabled(False)
            if value == "Freq":
                self.ui.frecuency_button.setStyleSheet("background-color: gray")
                self.ui.frecuency_button.setEnabled(False)
            if value == "Power":
                self.ui.energy_Q_button.setStyleSheet("background-color: gray")
                self.ui.energy_Q_button.setEnabled(False)
                self.ui.energy_U_button.setStyleSheet("background-color: gray")
                self.ui.energy_U_button.setEnabled(False)
                self.ui.energy_W_button.setStyleSheet("background-color: gray")
                self.ui.energy_W_button.setEnabled(False)
            if value == "Current":
                self.ui.current_button.setStyleSheet("background-color: gray")
                self.ui.current_button.setEnabled(False)
            if value == "LT_Flicker" or "ST_Flicker":
                self.ui.flicker_button.setStyleSheet("background-color: gray")
                self.ui.flicker_button.setEnabled(False)
            if value == "Desvalance":
                self.ui.current_unbalance_button.setStyleSheet("background-color: gray")
                self.ui.current_unbalance_button.setEnabled(False)
            if value == "Angulo":
                self.ui.current_angle_button.setStyleSheet("background-color: gray")
                self.ui.current_angle_button.setEnabled(False)

    def custom(self):
        self.custom = GraphicsComparison()
        self.values = list(self.diccionario.values())
        self.custom.setVariables(variables=self.values)
        self.custom.show()

        


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