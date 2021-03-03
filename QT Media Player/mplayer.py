from PyQt5 import QtGui, QtCore, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys

class VideoWindow(QMainWindow):
    
    def __init__(self):
        super(VideoWindow,self).__init__()

        self.setWindowTitle("Py MediaPlayer")

        self.mp=QMediaPlayer(None,QMediaPlayer.VideoSurface)
        VideoWidget=QVideoWidget()

        self.play=QPushButton()
        self.play.setEnabled(True)
        self.play.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play.clicked.connect(self.start)

        self.stop=QPushButton()
        self.stop.setEnabled(True)
        self.stop.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stop.clicked.connect(self.stopb)

        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.setPosition)
        
        

        self.volume = 10000
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMaximum(32767)
        self.volumeSlider.setPageStep(1024)
        self.volumeSlider.setValue(self.volume)
        self.volumeSlider.valueChanged.connect(self.changeVolume)
        self.volumeSlider.setFixedSize(120, 20) 



        self.errorLabel=QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        openAction=QAction('&Open',self)
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.openFile)

        exitAction=QAction('&Exit',self)
        exitAction.triggered.connect(self.exitApp)

        menubar=self.menuBar()
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(openAction)
        filemenu.addAction(exitAction)


        wid=QWidget(self)
        self.setCentralWidget(wid)
        
        cLayout=QHBoxLayout()
        cLayout.setContentsMargins(0, 0, 0, 0)
        cLayout.addWidget(self.play)
        cLayout.addWidget(self.stop)
        cLayout.addWidget(self.slider)
        cLayout.addWidget(self.volumeSlider)
        

        layout=QVBoxLayout()
        layout.addWidget(VideoWidget)
        layout.addLayout(cLayout)
        layout.addWidget(self.errorLabel)

        wid.setLayout(layout)

        self.mp.setVideoOutput(VideoWidget)
        self.mp.stateChanged.connect(self.stateC)
        self.mp.positionChanged.connect(self.positionC)
        self.mp.durationChanged.connect(self.durationC)
        self.mp.error.connect(self.errorHandle)


    def start(self):
        if self.mp.state()==QMediaPlayer.PlayingState:
            self.mp.pause()
        else: self.mp.play()

    def setPosition(self,position):
        self.mp.setPosition(position)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.mp.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play.setEnabled(True)
            self.mp.play()

    def exitApp(self):
        sys.exit(app.exec_())

    def stateC(self,state):
        if self.mp.state() == QMediaPlayer.PlayingState:
            self.play.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))


    def positionC(self,position):
        self.slider.setValue(position)

    def stopb(self):
        self.mp.stop()

    def durationC(self,duration):
        self.slider.setRange(0,duration)
    
    def errorHandle(self):
        self.play.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mp.errorString())

    def changeVolume(self,value):

        self.mp.setVolume(value / self.volumeSlider.maximum() * 100)


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=VideoWindow()
    window.resize(800,600)
    window.show()
    sys.exit(app.exec_())