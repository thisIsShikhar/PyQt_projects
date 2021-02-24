import sys
from csv import QUOTE_NONNUMERIC
import pandas as pd
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWebEngine
from PyQt5.QtWebEngineWidgets import QWebEngineView
import cv2



class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(800, 600, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

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

        # self.Worker1 = Worker1()


        self.webView.setUrl(QtCore.QUrl("https://www.google.com"))
        # self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.webView.setObjectName("webView")
        # self.webView.show()
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

    # def ImageUpdateSlot(self, Image):
    #     self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

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
