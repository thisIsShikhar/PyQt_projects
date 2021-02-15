from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 378)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combox = QtWidgets.QComboBox(self.centralwidget)
        self.combox.setGeometry(QtCore.QRect(40, 90, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.combox.setFont(font)
        self.combox.setObjectName("combox")
        self.combox.addItem("")
        self.combox.addItem("")
        self.comboy = QtWidgets.QComboBox(self.centralwidget)
        self.comboy.setGeometry(QtCore.QRect(350, 90, 181, 101))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.comboy.setFont(font)
        self.comboy.setObjectName("comboy")
        self.comboy.addItem("")
        self.comboy.addItem("")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(210, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Rasa SemiBold")
        font.setPointSize(18)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combox.setItemText(0, _translate("MainWindow", "0"))
        self.combox.setItemText(1, _translate("MainWindow", "1"))
        self.comboy.setItemText(0, _translate("MainWindow", "0"))
        self.comboy.setItemText(1, _translate("MainWindow", "1"))
        self.button.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "X XOR Y ="))

    def pressed(self):
        x=int(self.combox.currentText())
        y=int(self.combox.currentText())

        xor = (x and not y) or (not x and y)
        
        if xor == True:
            xor=1
        else:
            xor=0

        self.label.setText(" X OR Y ="+ str(xor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
