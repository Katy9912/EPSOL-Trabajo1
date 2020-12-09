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

        #Esta variable manda la señal y referencia si esta abierta
        self.parent.parent.setAvailableView(available=True, screen=self)
        
        self.ui.setupUi(self)
        
        #Estas dos lineas siguientes bloquean el boton cerrar de la ventana
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        #Se muestra la pantalla (interfaz)
        self.show()
        self.init_dir = "../"
        self.save_dir = parent.parent.getPath() #Esta variable hace referencia al directorio raiz donde se guardaran las graficas
        self.info = None #Esta variable almacena la informacion del dataframe que se usa para graficar
        self.key = "" #Esta variable guarda el nombre de la "variable" que se quiere graficar
        self.label = "" #Esta variable guarda la etiqueta del boton para que funja como titulo
        

        #Listeners de los botones "Regresar" e "Inicio"
        self.ui.backButton.clicked.connect(self.back)
        self.ui.homeButton.clicked.connect(self.home)

        #Se inicializa la vista Web para las graficas y la logica del programa
        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(1040,500)
        self.web.setZoomFactor(0.8)

        self.data = Graphic_Data()
        self.data.setPath(path=self.save_dir)

    #Metodo que obtiene el dataframe para generar las graficas
    def setData(self,datos):
        self.info = datos
    #Metodo que obtiene el nombre de la categoria que se graficara (Nombre del boton)
    def setName(self,name, label_title, month):
        self.key = name
        self.label = label_title
        self.month_selected = month

    #Metodo que genera la grafica
    def plotitem(self):
        plot_name = self.data.plot(dataframe=self.info, key=self.key, label_title=self.label, month_used=self.month_selected)
        self.parent.parent.setFiles(files=plot_name) #Este método almacena una lista de los archivos html generados
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