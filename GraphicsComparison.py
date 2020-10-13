import pandas as pd
import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

from Scripts.App_V3.Graficas_Comparacion import * 
from Scripts.App_V3.Graphic_Data import Graphic_Data


class GraphicsComparison(QtWidgets.QMainWindow):

    def __init__(self,parent,variables):
        super(GraphicsComparison, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Esta variable guarda referencia a la interfaz "parent" de esta interfaz
        # Es necesaria para la interaccion de los botones 
        self.parent=parent

        #Esta variable almacena una lista de las variables que se pueden graficar 
        self.values = variables
        
        self.init_dir = "../" #Esta variable hace referencia al directorio raiz donde se guardaran las graficas
        self.info = None #Esta variable almacena la informacion del dataframe que se usa para graficar
        self.vData = None #Esta variable almacena la data de la "variable" que se va a graficar
        self.key = "" #Esta variable guarda el nombre de la "variable" que se quiere graficar
        self.plot_list = [] #Esta variable almacena una lista de los archivos html generados
        
        #Estas dos lineas siguientes bloquean el boton cerrar de la ventana
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        
        self.ui.list_options.addItems(self.values) #Agrega las variables a la lista para ser seleccionadas
        self.ui.list_options.itemClicked.connect(self.plotVariable) #Listener de la seleccion de variables

        #Se inicializa la vista Web para las graficas y la logica del programa
        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(1040,500)
        self.web.setZoomFactor(0.8)
        self.data = Graphic_Data()

        #Se muestra la pantalla (interfaz)
        self.show()

        #Listeners de los botones "Regresar" e "Inicio"
        self.ui.backButton.clicked.connect(self.back)
        self.ui.homeButton.clicked.connect(self.home) 

    #Metodo que genera la gráfica y la muestra
    # Para este metodo se necesita comporbar que el metodo "plot" genera la grafica
    def plotVariable(self):
        self.variableData()
        '''plot_name = self.data.plot(dataframe=self.variableData, key=self.key)
        self.plot_list.append(plot_name)
        plot_file = os.path.join("file:///" + self.init_dir, plot_name)
        self.web.load(QUrl(plot_file))'''
        self.web.show()

    #Metodo para obtener el dataframe 
    def setData(self,data):
        self.info = data
        
    #Metodo para obtener de todo el dataframe solo la información de la variable seleccionada
    # En la lista
    def variableData(self):
        self.key = self.ui.list_options.currentItem().text()
        self.vData = self.info[self.key]
        

    # Metodo del boton "Regresar"
    def back(self):
        #Cierra la interfaz actual
        self.close()
        #Muestra la interfaz padre (Menu)
        self.parent.raise_()
    
    #Metodo del boton "Inicio"
    def home(self):
        #Cierra interfaz actual
        self.close()
        #Cierra la interfaz padre (Menu)
        self.parent.close()
        #Muestra la interfaz padre.padre(Menu Principal)
        self.parent.parent.raise_()

    #Metodo que elimina los archivos html generados al momento de cerrar la ventana
    def closeEvent(self, event):
        if event:
            if self.plot_list:
                for file in self.plot_list:
                    os.remove(file)
                    self.plot_list.remove(file)
    
    
    


'''if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    #app = QtWidgets.QApplication(sys.argv)
    #sys.exit(app.exec_())'''