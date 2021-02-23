import sys
from csv import QUOTE_NONNUMERIC
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QWidget
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
# from PyQt5 import QtCore,QtGui,QtWidgets
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# import cv2
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5 import QtWebEngine

a = pd.read_csv('report1feb.csv')
df=a[['name']]
names = df.values
names = [name[-1] for name in names]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("iAttendance")
        Form.resize(767, 530)
        self.webView = QWebEngineView(Form)
        self.webView.setGeometry(QtCore.QRect(10, 30, 491, 471))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(510, 30, 251, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Present till now'])
        self.tableWidget.setColumnWidth(0,230)


        row=0
        self.tableWidget.setRowCount(len(a))

        for i in names:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i))
            row=row+1

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
