import sys
import time
import os
import numpy as np
from bokeh.plotting import *


from PyQt5.QtWidgets import QFileDialog,QMessageBox,QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Epsolapp_main_window import *
from epsol_window2 import *


class epsol_app(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)
        self.second = GraphicsWindow()
        self.dir = "./"
        self.show()

        self.ui.graphic_button.clicked.connect(self.abrir)
        self.ui.load_file_button.clicked.connect(self.loadfiles)

    def abrir(self):
        self.second.show()

    def loadfiles(self):
        archivos = QFileDialog.getOpenFileNames(self,"Abrir Archivos", self.dir, "CSV Files (*.csv)")
        print(archivos)

    def closeEvent(self, event):
        if event:
            self.second.close()


class GraphicsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        #QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.web = QWebEngineView(self.ui.widget)
        self.web.resize(500,500)
        self.graphics()


        # self.show()

    def graphics(self):
        # Directory and names
        initial_dir = "./"

        plot_name = str("plot-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".html")
        plot_file = os.path.join("file:///" + initial_dir, plot_name)


        # prepare some data
        N = 4000
        x = np.random.random(size=N) * 100
        y = np.random.random(size=N) * 100
        radii = np.random.random(size=N) * 1.5
        colors = [
            "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50 + 2 * x, 30 + 2 * y)
        ]

        # output to static HTML file (with CDN resources)
        output_file(plot_name, title="color_scatter.py example", mode="cdn")

        TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

        # create a new plot with the tools above, and explicit ranges
        p = figure(tools=TOOLS, x_range=(0, 100), y_range=(0, 100))

        # add a circle renderer with vectorized colors and sizes
        p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

        # show the results
        save(p)

        self.web.load(QUrl(plot_file))
        self.web.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = epsol_app()
    # my_app.show()
    sys.exit(app.exec_())
