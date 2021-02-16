# from PyQt5.QtWebEngineWidgets import *
# from PyQt5 import QApplication, QWidget, QMainWindow
# import sys

# app=QApplication(sys.argv)
# web=QWebView()
# web.load(QUrl("https://google.com"))
# web.show()


# import inspect
# from PyQt5 import Qt

# vers = ['%s = %s' % (k,v) for k,v in vars(Qt).items() if k.lower().find('version') >= 0 and not inspect.isbuiltin(v)]
# print('\n'.join(sorted(vers)))


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl("https://google.com"))
web.show()

sys.exit(app.exec_())