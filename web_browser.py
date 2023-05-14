# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:41:13 2022

@author: Bisar
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQtWebEngineWidgets import *#PyQtWebEngine
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python")
        self.browser =QWebEngneView()
        self.browser.setUrl(QUrl('https://google.com'))
        
        self.show()
        nav =QToolBar()
        self.addToolBar(nav)
        
        back_b = QAction('Back',self)
        back_b.triggered.connect(self.browser.back)
        nav.addAction(back_b)
        
        forward_b = QAction('Forward',self)
        forward_b.triggered.connect(self.browser.forward)
        nav.addAction(forward_b)
        
        reload_b = QAction('Reload',self)
        reload_b.triggered.connect(self.browser.reload)
        nav.addAction(reload_b)
        
        home_b = QAction('Home',self)
        home_b.triggered.connect(self.browser.home)
        nav.addAction(home_b)
        
        self.url_bar =QlineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.urlbar)
        
        self.browser.urlChanged.connect(self.url_change)
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        # self.url_bar.setText('a')
    def url_change(self,q):
        self.url_bar.setText(q.toString())
    def navigate_home(self):
         self.browser.setUrl(QUrl('https://funwithdatascience.com'))
    
        
        
        
        
        
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
