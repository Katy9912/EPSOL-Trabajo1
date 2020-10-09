from Graficas_Comparacion import * 

class GraphicsComparison(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_comparation_options()
        self.ui.setupUi(self)
        self.show()

        self.values = [None]
        self.ui.cancel_button.clicked.connect(self.exit)
    
    def exit(self):
        self.close()

    def setVariables(self,variables):
        self.values = variables


'''if __name__ == "__main__":
    import sys, time, os
    from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWidgets import *
    from PyQt5 import QtWidgets
    from PyQt5.QtCore import *

    #app = QtWidgets.QApplication(sys.argv)
    #sys.exit(app.exec_())'''