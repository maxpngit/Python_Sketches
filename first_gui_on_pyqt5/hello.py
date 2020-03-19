# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(190, 111, 256, 151))
        self.listWidget.setObjectName("listWidget")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(370, 280, 75, 23))
        self.browseButton.setObjectName("browseButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.HelloHere = QtWidgets.QLineEdit(self.centralwidget)
        self.HelloHere.setGeometry(QtCore.QRect(170, 70, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.HelloHere.setFont(font)
        self.HelloHere.setObjectName("HelloHere")
        self.helloButton = QtWidgets.QPushButton(self.centralwidget)
        self.helloButton.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.helloButton.setObjectName("helloButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hello"))
        self.browseButton.setText(_translate("MainWindow", "BROWSE"))
        self.label.setText(_translate("MainWindow", "Файлы в выбранной папке:"))
        self.label_2.setText(_translate("MainWindow", "Нажми на кнопку, получишь результат!!!"))
        self.label_3.setText(_translate("MainWindow", "Результат:"))
        self.helloButton.setText(_translate("MainWindow", "Hello"))
