from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import glob
import os
import csv

class Ui_Rule_Priority_test(object):
    def setupUi(self, Rule_Priority_test):
        Rule_Priority_test.setObjectName("Rule_Priority_test")
        Rule_Priority_test.resize(577, 531)
        self.gridLayout = QtWidgets.QGridLayout(Rule_Priority_test)
        self.gridLayout.setObjectName("gridLayout")
        self.OpenCsv = QtWidgets.QPushButton(Rule_Priority_test)
        self.OpenCsv.setObjectName("OpenCsv")
        self.gridLayout.addWidget(self.OpenCsv, 0, 0, 1, 1)
        self.OpenCsv.clicked.connect(self.file_open)
        self.tableView = QtWidgets.QTableView(Rule_Priority_test)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.Refresh = QtWidgets.QPushButton(Rule_Priority_test)
        self.Refresh.setObjectName("Refresh")
        self.gridLayout.addWidget(self.Refresh, 2, 0, 1, 1)

        self.retranslateUi(Rule_Priority_test)
        self.Refresh.clicked.connect(self.tableView.clearSpans)
        QtCore.QMetaObject.connectSlotsByName(Rule_Priority_test)

    def retranslateUi(self, Rule_Priority_test):
        _translate = QtCore.QCoreApplication.translate
        Rule_Priority_test.setWindowTitle(_translate("Rule_Priority_test", "Dialog"))
        self.OpenCsv.setText(_translate("Rule_Priority_test", "Browse Csv and Get Score"))
        self.Refresh.setText(_translate("Rule_Priority_test", "Refresh"))


    def file_open(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(Rule_Priority_test, 'Open csv' , QtCore.QDir.rootPath() , '*.csv')
        #df1 = pd.DataFrame()
        #df1 = pd.concat([pd.read_csv(f) for f in glob.glob('*.csv')] , ignore_index=True)
        print(filename)
        path = self.lineEdit.text(fileName)
        df1 = pd.read_csv(path)
        df2 = pd.read_csv('export.csv')
        df = pd.merge(df2, df1, how='inner').dropna(axis="columns")
        model = pd(df)
        self.tableView.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rule_Priority_test = QtWidgets.QDialog()
    ui = Ui_Rule_Priority_test()
    ui.setupUi(Rule_Priority_test)
    Rule_Priority_test.show()
    sys.exit(app.exec_())
