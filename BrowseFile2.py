
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import xml.etree.ElementTree as ET
root=tree.getroot()
ET.dump(tree)

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        self.browse.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self, 'Open file', 'C:/Users/Bisar/OneDrive/Desktop/python/PyQt', 'XML files(*.xml)')
        self.filename.setText(fname[0])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
