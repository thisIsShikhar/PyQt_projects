from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


class Ui_MainWindow(object):
 def setupUi(self, MainWindow):
  MainWindow.setObjectName(_fromUtf8("MainWindow"))
  MainWindow.resize(176, 156)
  self.centralWidget = QtGui.QWidget(MainWindow)
  self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
  self.gridLayout = QtGui.QGridLayout(self.centralWidget)
  self.pushButton = QtGui.QPushButton(self.centralWidget)
  self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

  self.text = QTextEdit()
  self.gridLayout.addWidget(self.text, 1, 0, 1, 1)

  self.pushButton.clicked.connect( self.Out)


  out = 0
  def number(self):
    i = 0
    while True:
        i += 1
        time.sleep(0.5)
        out = str(i)

  def Out(self):
    time.sleep(0.5)
    self.text.append(self.number())
    QtGui.qApp.processEvents()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())