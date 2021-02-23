import sys
from csv import QUOTE_NONNUMERIC
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView, QWidget
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

a = pd.read_csv('report1feb.csv')
df=a[['name']]
names = df.values
names = [name[-1] for name in names]


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(740, 296)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 701, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setColumnWidth(1,500)
        # self.tableWidget.setRowCount(2)
        row=0
        self.tableWidget.setRowCount(len(a))

        for i in names:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i))

            row=row+1

        self.horizontalLayout.addWidget(self.tableWidget)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        # self.tableWidget_2.setColumnCount(0)
        # self.tableWidget_2.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget_2)
        # self.loaddata()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
