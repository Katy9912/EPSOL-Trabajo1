# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graficas_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_graphics_menu(object):
    def setupUi(self, graphics_menu):
        graphics_menu.setObjectName("graphics_menu")
        graphics_menu.resize(800, 600)
        graphics_menu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/EPSOL_ICO/LogoEpsol.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        graphics_menu.setWindowIcon(icon)
        graphics_menu.setStyleSheet("QMainWindow{\n"
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
        graphics_menu.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(graphics_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.titte_label = QtWidgets.QLabel(self.centralwidget)
        self.titte_label.setGeometry(QtCore.QRect(120, 30, 590, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.titte_label.setFont(font)
        self.titte_label.setAlignment(QtCore.Qt.AlignCenter)
        self.titte_label.setObjectName("titte_label")
        self.potency_factor_button = QtWidgets.QPushButton(self.centralwidget)
        self.potency_factor_button.setGeometry(QtCore.QRect(320, 130, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.potency_factor_button.setFont(font)
        self.potency_factor_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.potency_factor_button.setObjectName("potency_factor_button")
        self.harmonics_button = QtWidgets.QPushButton(self.centralwidget)
        self.harmonics_button.setGeometry(QtCore.QRect(320, 200, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.harmonics_button.setFont(font)
        self.harmonics_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.harmonics_button.setToolTip("")
        self.harmonics_button.setObjectName("harmonics_button")
        self.thd_button = QtWidgets.QPushButton(self.centralwidget)
        self.thd_button.setGeometry(QtCore.QRect(320, 270, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.thd_button.setFont(font)
        self.thd_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.thd_button.setObjectName("thd_button")
        self.potency_button = QtWidgets.QPushButton(self.centralwidget)
        self.potency_button.setGeometry(QtCore.QRect(320, 340, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.potency_button.setFont(font)
        self.potency_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.potency_button.setObjectName("potency_button")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(60, 430, 161, 91))
        self.logo_label.setStyleSheet("border-image: url(:/EPSOL/LogoEpsolCMYK.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.energy_button = QtWidgets.QPushButton(self.centralwidget)
        self.energy_button.setGeometry(QtCore.QRect(320, 410, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.energy_button.setFont(font)
        self.energy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.energy_button.setObjectName("energy_button")
        graphics_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(graphics_menu)
        self.statusbar.setObjectName("statusbar")
        graphics_menu.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(graphics_menu)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(graphics_menu)
        QtCore.QMetaObject.connectSlotsByName(graphics_menu)

    def retranslateUi(self, graphics_menu):
        _translate = QtCore.QCoreApplication.translate
        graphics_menu.setWindowTitle(_translate("graphics_menu", "EPSOL Soluciones en Sistemas de Potencia y EnergíaSA de CV"))
        self.titte_label.setText(_translate("graphics_menu", "Gráficas Disponibles"))
        self.potency_factor_button.setToolTip(_translate("graphics_menu", "Carga los archivos .csv"))
        self.potency_factor_button.setText(_translate("graphics_menu", "Factor de Potencia"))
        self.harmonics_button.setText(_translate("graphics_menu", "Armónicos"))
        self.thd_button.setToolTip(_translate("graphics_menu", "Muestra las gráficas"))
        self.thd_button.setText(_translate("graphics_menu", "THD"))
        self.potency_button.setToolTip(_translate("graphics_menu", "Genera reporte en word"))
        self.potency_button.setText(_translate("graphics_menu", "Potencia"))
        self.energy_button.setToolTip(_translate("graphics_menu", "Genera reporte en word"))
        self.energy_button.setText(_translate("graphics_menu", "Energía"))
        self.actionAbout.setText(_translate("graphics_menu", "About"))
import Epsol_Logo_rc
