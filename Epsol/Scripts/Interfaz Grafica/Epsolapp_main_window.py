# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Epsolapp_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(800, 600)
        root.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/EPSOL_ICO/LogoEpsol.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        root.setWindowIcon(icon)
        root.setStyleSheet("QMainWindow{\n"
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
        root.setWindowFilePath("")
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(120, 30, 590, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.load_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_file_button.setGeometry(QtCore.QRect(320, 150, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.load_file_button.setFont(font)
        self.load_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_file_button.setObjectName("load_file_button")
        self.download_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_file_button.setGeometry(QtCore.QRect(320, 220, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.download_file_button.setFont(font)
        self.download_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_file_button.setToolTip("")
        self.download_file_button.setObjectName("download_file_button")
        self.graphic_button = QtWidgets.QPushButton(self.centralwidget)
        self.graphic_button.setGeometry(QtCore.QRect(320, 290, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.graphic_button.setFont(font)
        self.graphic_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphic_button.setObjectName("graphic_button")
        self.report_button = QtWidgets.QPushButton(self.centralwidget)
        self.report_button.setGeometry(QtCore.QRect(320, 360, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.report_button.setFont(font)
        self.report_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.report_button.setObjectName("report_button")
        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(60, 430, 161, 91))
        self.logo_label.setStyleSheet("border-image: url(:/EPSOL/LogoEpsolCMYK.png);")
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 140, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        root.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        root.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(root)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "EPSOL Soluciones en Sistemas de Potencia y EnergíaSA de CV"))
        self.title_label.setText(_translate("root", "<html><head/><body><p align=\"center\">Aplicacion para limpiar datos de los Load Profiles del Equipo</p><p align=\"center\">SEL-735</p></body></html>"))
        self.load_file_button.setToolTip(_translate("root", "Carga los archivos .csv"))
        self.load_file_button.setText(_translate("root", "Cargar Archivos"))
        self.download_file_button.setText(_translate("root", "Descargar Archivo"))
        self.graphic_button.setToolTip(_translate("root", "Muestra las gráficas"))
        self.graphic_button.setText(_translate("root", "Graficar"))
        self.report_button.setToolTip(_translate("root", "Genera reporte en word"))
        self.report_button.setText(_translate("root", "Generar Reporte Word"))
        self.label.setText(_translate("root", "<html><head/><body><p align=\"center\">Nota: Solo son Aceptados los datos</p><p align=\"center\">del Equipo SEL735 y exportados</p><p align=\"center\">desde Quickset en formato CSV</p></body></html>"))
        self.menuHelp.setTitle(_translate("root", "Help"))
        self.actionAbout.setText(_translate("root", "About"))
import Epsol_Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())
