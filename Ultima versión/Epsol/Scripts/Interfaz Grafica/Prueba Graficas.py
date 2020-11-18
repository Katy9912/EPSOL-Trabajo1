import sys
import time
import os

import numpy as np
from bokeh.plotting import *


from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
import PyQt5.QtWidgets


#Directory and names
initial_dir = "./"

plot_name = str("plot-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".html")
plot_file =  os.path.join("file:///"+initial_dir,plot_name)
print(plot_file)

from bokeh.plotting import figure, output_file, show

# prepare some data
N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
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


#Qt App

app = QApplication(sys.argv)

web=QWebEngineView()
web.load(QUrl(plot_file))
web.show()

sys.exit(app.exec_())



