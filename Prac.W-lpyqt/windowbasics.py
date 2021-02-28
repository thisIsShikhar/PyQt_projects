from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)

        self.setWindowTitle("My Window")
        self.setGeometry(100,100,800,600)

        label=QLabel("HELLO! KAKA")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)


        button_action = QAction("Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction("Button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()
        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())


        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self,s):
        print('clicked',s)

app=QApplication(sys.argv)
win=MainWindow()
win.show()
app.exec_()
