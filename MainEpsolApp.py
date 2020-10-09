#Se importan las librerias requeridas para la ejecución de la clase
import pandas as pd
import numpy as np
import os
import docx
from docx import Document

from datetime import datetime
import csv

from Main_Window import *

from GraphicsMenu import *
from Graphic_Data import *

class MainEpsolApp (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        self.show()        
        self.files = None
        self.initial_dir = "../"        
        self.data = None
        self.band=False

        
        #Listeners de los botones de la interfaz principal
        self.ui.load_file_button.clicked.connect(self.loadFiles)
        self.ui.download_file_button.clicked.connect(self.download)
        self.ui.graphic_button.clicked.connect(self.availableGraphics)
        self.ui.report_button.clicked.connect(self.word)
        #self.ui.report_button.clicked.connect(self.word)
        self.ui.menuHelp.triggered.connect(self.info)
        

    #Declaracion de métodos relacionados a los botones de la interfaz principal

    #Método para cargar los datos a procesas   
    def loadFiles(self):
        self.files = QFileDialog.getOpenFileNames(self, "Abrir Archivos", self.initial_dir, "CSV Files (*.csv)") 
        if self.files[0]:
            graph = Graphic_Data()
            self.data = graph.merge(self.files[0],False)
            

      #Metodo que descarga el csv de la informacion procesada
    def download(self):

        if self.data is None:
            self.warning()
        else:
            graph = Graphic_Data()
            self.data=graph.merge(self.files[0],True)
            self.download = pd.DataFrame(self.data)
            self.nombre = datetime.now().strftime('Dataframe_usado__%H_%M_%d_%m_%Y.csv')
            self.download.to_csv(str(self.nombre), header=True, index=False)
            self.nota = "Descarga de reporte CSV completa" 
            self.information(anuncio=self.nota)
            
            
    def word(self):
        
        
        path = './Imagenes'       
        lstFiles = []        
        lstDir = os.walk(path)        
 
        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                if(extension == ".png"):
                    lstFiles.append(nombreFichero+extension)
        for f in lstFiles:            
            try:
                doc = docx.Document('test.docx')
                #doc.add_picture(str(path+'\\'+f),width=docx.shared.Inches(10), height=docx.shared.Cm(5))
                doc.add_picture(str(path+'\\'+f))
                doc.save('test.docx')
            except Exception as e: 
    
                print(e,"Generando archivo .docx")            
                document = Document()
                document.save('test.docx')
                doc = docx.Document('test.docx')
                doc.add_picture(str(path+'\\'+f))
                
                doc.save('test.docx')    
        print("Archivo finalizado")        

    def availableGraphics(self):
        if self.files:
            if self.files[0]:
                #Se crea una instancia de GraphicsMenu
                self.menu = GraphicsMenu()
                #Se manda el merge que se genera con los datos cargados
                graph = Graphic_Data()
                self.data = graph.merge(self.files[0],False)
            
                self.menu.cargarData(data=self.data)
                #Se establecen las opciones de gráficas que estan disponibles
                #A partir de los archivos cargados
                self.menu.comparar()
                #Se muestra interfaz
                self.menu.show()
               
            else:
                #Se muestra señal de emergencia
                self.warning()
        else:
            #Se muestra señal de emergencia
            self.warning()
    

    def closeEvent(self, event):
        if event:
            self.menu.close()

    #Metodo que miestra información de desarrollo
    def info(self):
        QMessageBox.about(self, "Informacion del programa",
                          "Programa Diseñado por:\nErick Rodriguez Orduña y\nCarlos " +
                          "Ramirez Rendon" + "\nPara: EPSOL SA de CV")

    #Metodo que muestra el mensaje de advertencia sobre datos inexistentes
    def warning(self):
        QMessageBox.warning(self, "Advertencia!", "No existen archivos cargados", buttons=QMessageBox.Ok)

    def information(self, anuncio):
        aviso = anuncio
        QMessageBox.information(self, "Aviso!",
                                        str(aviso))

#Main
if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *


    app = QtWidgets.QApplication(sys.argv)
    my_app = MainEpsolApp()
    sys.exit(app.exec_())