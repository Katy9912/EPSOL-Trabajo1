import pandas as pd
import numpy as np
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *

from Graficas_Comparacion import * 
from Graphic_Data import Graphic_Data


class GraphicsComparison(QtWidgets.QMainWindow):

    def __init__(self,parent):
        super(GraphicsComparison, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Esta variable guarda referencia a la interfaz "parent" de esta interfaz
        # Es necesaria para la interaccion de los botones 
        self.parent=parent

        #Esta variable manda la señal y referencia si esta abierta
        self.parent.parent.setAvailableCustomized(available=True, screen=self)

        #Esta variable guarda el path de la carpeta generada por el programa
        self.save_dir = parent.parent.getPath()
        
        self.init_dir = "../"
        self.info=None
        
        #Estas dos lineas siguientes bloquean el boton cerrar de la ventana
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        

        #Se inicializa la vista Web para las graficas y la logica del programa
        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(1040,500)
        self.web.setZoomFactor(0.8)
        self.data = Graphic_Data()
        self.data.setPath(path=self.save_dir)

        #Se muestra la pantalla (interfaz)
        self.show()

        self.ui.graphicButton.clicked.connect(self.plot)

        #Listeners de los botones "Regresar" e "Inicio"
        self.ui.backButton.clicked.connect(self.back)
        self.ui.homeButton.clicked.connect(self.home) 

    
    #Metodo para obtener el dataframe 
    def setData(self,data):
        self.info = data
    
    #Metodo que permite generar la lista de opciones que se pueden graficar
    def createList(self):
        self.checkbox = list(self.data.optionsToGraph(dataframe=self.info))
        self.formLayout = QFormLayout()
        self.groupBox = QGroupBox()
        self.comboList = []
        
        for i, v in enumerate(self.checkbox):
            self.checkbox[i] = QCheckBox(v)
            self.comboList.append(self.checkbox[i])
            self.formLayout.addRow(self.comboList[i])
        
        self.groupBox.setLayout(self.formLayout)
        self.ui.area.setWidget(self.groupBox)
    
    #Metodo que verifica las opciones seleccionadas
    def checkedOptions(self):
        checked = []
        for opt in self.comboList:
            if opt.isChecked():
                checked.append(opt.text())
        return checked

    #Metodo que genera la grafica con las variables seleccionadas
    def plot(self):
        variables = self.checkedOptions()
        plot_name = self.data.plotVariable(dataframe=self.info, variables=variables)
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

'''if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    #app = QtWidgets.QApplication(sys.argv)
    #sys.exit(app.exec_())'''