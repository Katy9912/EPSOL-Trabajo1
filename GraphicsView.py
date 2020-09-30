import pandas as pd
import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from Scripts.App_V2.Graficas_Window import *
from Scripts.App_V2.Graphic_Data import * 

class GraphicsView (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.init_dir = "../"
        self.info = None 
        self.key = ""
        self.plot_list = []

        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(1266, 578)
        self.web.setZoomFactor(0.8)

        self.data = Graphic_Data()
    
    def setData(self,datos):
        self.info = datos
    
    def setName(self,name):
        self.key = name

    def plotitem(self):

        plot_name = self.data.plot(dataframe=self.info, key=self.key)
        self.plot_list.append(plot_name)
        plot_file = os.path.join("file:///" + self.init_dir, plot_name)
        self.web.load(QUrl(plot_file))
        self.web.show()
    
    def closeEvent(self, event):
        if event:
            if self.plot_list:
                for file in self.plot_list:
                    os.remove(file)
                    self.plot_list.remove(file)