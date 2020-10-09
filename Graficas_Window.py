# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graficas_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1266, 715)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/EPSOL_ICO/LogoEpsol.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"                        background-color: rgb(255,255,255);\n"
"                        }\n"
"\n"
"QPushButton{\n"
"                            \n"
"                            border-style: solid;\n"
"                            border-width: 1px;\n"
"                            border-color: rgb(0, 0, 0);\n"
"                            color: rgb(0, 0, 0);\n"
"                            border-radius: 5px;\n"
"                               background-color: qlineargradient(spread:pad, x1:0.965909, y1:0, x2:1, y2:1, stop:0                                                     rgba(252, 252, 252, 255), stop:0.573864 rgba(226, 226, 226, 255));\n"
"                        }\n"
"\n"
"QPushButton:hover {\n"
"                           background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 \n"
"                       #fff, stop: 1 #bbb  );\n"
"                                    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 80, 1040, 500))
        self.widget.setObjectName("widget")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(60, 570, 161, 91))
        self.logo_label.setStyleSheet("border-image: url(:/EPSOL/LogoEpsolCMYK.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(20, 30, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(32, 112, 137);")
        self.homeButton.setIconSize(QtCore.QSize(16, 16))
        self.homeButton.setObjectName("homeButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(140, 30, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("border-radius:10px;\n"
"border-color: rgb(32, 112, 137);")
        self.backButton.setIconSize(QtCore.QSize(16, 16))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EPSOL Soluciones en Sistemas de Potencia y Energía SA de CV"))
        self.homeButton.setText(_translate("MainWindow", "INICIO"))
        self.backButton.setText(_translate("MainWindow", "REGRESAR"))
import Epsol_Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
