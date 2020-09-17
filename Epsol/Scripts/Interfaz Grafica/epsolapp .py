'''Autor: Carlos Ramirez Rendon, Erick Rodriguez Orduña
Para: EPSOL SA de CV
Program: Prosessing data and visualization for a SEL Device'''

from Epsolapp_main_window import *
from epsol_window2 import *

#Se importa la ventana "Graficas_menu"
from Graficas_menu import *

from Data import *
import pandas as pd
import os

#Declaración de la clase principal, EPSOLAPP que contiene la ventana inicial
class EpsolApp(QtWidgets.QMainWindow):
    
    #Inicializacion de los componentes de la Interfaz Gráfica
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)

        self.files = None
        self.initial_dir = "../EPSOL_APP/Scripts/ErickXD"
        self.pd = None
        

        self.second = GraphicsWindow(init_dir=self.initial_dir)
        
        #Referencia a objeto de clase GraficsMenu
        self.third = GraphicsMenu()

        #Se modifica la conexión de graphics_button para llamar a la nueva ventana
        self.ui.graphic_button.clicked.connect(self.menu)
        
        self.ui.load_file_button.clicked.connect(self.loadfiles)
        self.ui.menuHelp.triggered.connect(self.winfo)

        self.show()

    def loadfiles(self):
        self.files = QFileDialog.getOpenFileNames(self, "Abrir Archivos", self.initial_dir, "CSV Files (*.csv)")

        if self.files[0]:
            data = Graphic_Data()
            self.pd = data.merge(self.files[0])

    #Este método no esta en uso porque se está usando el método menu
    '''def open(self):

        if self.files:
            if self.files[0]:
                self.second.pd = self.pd
                self.second.show()

            else:
                self.warninfo()
        else:
            self.warninfo()'''

    def menu (self):
        if self.files:
            if self.files[0]:
                self.second.pd = self.pd
                self.third.show()

            else:
                self.warninfo()
        else:
            self.warninfo()

        

    def warninfo(self):
        QMessageBox.warning(self, "Advertencia!", "No existen archivos cargados", buttons=QMessageBox.Ok)


    def winfo(self):
        QMessageBox.about(self, "Informacion del programa",
                          "Programa Diseñado por:\nErick Rodriguez Orduña y\nCarlos " +
                          "Ramirez Rendon" + "\nPara: EPSOL SA de CV")

    def closeEvent(self, event):
        if event:
            self.second.close()


#Clase de la ventana secundaria, usada para la visualización de las gráficas
class GraphicsWindow(QtWidgets.QMainWindow):
    def __init__(self, init_dir):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(600, 600)
        self.web.setZoomFactor(0.8)

        self.dir = init_dir
        self.pd = None
        self.plot_list = []

        self.list = self.ui.graph_options
        self.data = Graphic_Data()
        self.ui.graph_options.addItems(self.data.mediciones_dict)

        self.ui.graph_options.itemClicked.connect(self.plotitem)

    def plotitem(self):

        var = self.ui.graph_options.currentItem().text()
        plot_name = self.data.plot(self.pd, var)
        self.plot_list.append(plot_name)

        plot_file = os.path.join("file:///" + self.dir, plot_name)
        self.web.load(QUrl(plot_file))
        self.web.show()

    #Funcion que elimina los archivos .html generados al hacer las graficas, para limpiar memoria
    def closeEvent(self, event):
        if event:
            if self.plot_list:
                for file in self.plot_list:
                    os.remove(file)
                    self.plot_list.remove(file)

# Clase de la venta del menu de gráficas
class GraphicsMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_graphics_menu()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    app = QtWidgets.QApplication(sys.argv)
    my_app = EpsolApp()
    # my_app.show()
    sys.exit(app.exec_())
