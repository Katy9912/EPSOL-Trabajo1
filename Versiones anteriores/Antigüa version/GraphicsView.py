import pandas as pd
import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *


from Graficas_menu import *
from Graficas_Window import *
from Graphic_Data import * 

class GraphicsView (QtWidgets.QMainWindow):
    def __init__(self,parent):
        super(GraphicsView, self).__init__()
        self.ui = Ui_MainWindow()
        
        #Esta variable guarda referencia a la interfaz "parent" de esta interfaz
        # Es necesaria para la interaccion de los botones 
        self.parent = parent
        
        self.ui.setupUi(self)
        
        #Estas dos lineas siguientes bloquean el boton cerrar de la ventana
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        #Se muestra la pantalla (interfaz)
        self.show()

        self.init_dir = "../" #Esta variable hace referencia al directorio raiz donde se guardaran las graficas
        self.info = None #Esta variable almacena la informacion del dataframe que se usa para graficar
        self.key = "" #Esta variable guarda el nombre de la "variable" que se quiere graficar
        self.plot_list = [] #Esta variable almacena una lista de los archivos html generados

        #Listeners de los botones "Regresar" e "Inicio"
        self.ui.backButton.clicked.connect(self.back)
        self.ui.homeButton.clicked.connect(self.home)

        #Se inicializa la vista Web para las graficas y la logica del programa
        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(1040,500)
        self.web.setZoomFactor(0.8)

        self.data = Graphic_Data()

    #Metodo que obtiene el dataframe para generar las graficas
    def setData(self,datos):
        self.info = datos
    #Metodo que obtiene el nombre de la categoria que se graficara (Nombre del boton)
    def setName(self,name):
        self.key = name

    #Metodo que genera la grafica
    def plotitem(self):
        plot_name = self.data.plot(dataframe=self.info, key=self.key)
        self.plot_list.append(plot_name)
        plot_file = os.path.join("file:///" + self.init_dir, plot_name)
        self.web.load(QUrl(plot_file))
        self.web.show()
    
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
    '''def closeEvent(self, event):
        if event:
            if self.plot_list:
                for file in self.plot_list:
                    os.remove(file)
                    self.plot_list.remove(file)'''