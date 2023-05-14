import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog,QToolButton,QMenu
from PyQt5.uic import loadUi
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)
        
        # d = {'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}
        # button = QToolButton()
        # def callback_factory(k, v):
        #     return lambda: button.setText('{0}_{1}'.format(k, v))
        # menu = QMenu()
        # for k, vals in d.items():
        #     sub_menu = menu.addMenu(k)
        #     for v in vals:
        #         action = sub_menu.addAction(str(v))
        #         # action.triggered.connect(callback_factory(k, v))
        # button.setMenu(menu)
        
    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/Bisar/OneDrive/Desktop/python/PyQt', 'XML files(*.xml)')
        self.filename.setText(fname[0])

app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()
sys.exit(app.exec_())