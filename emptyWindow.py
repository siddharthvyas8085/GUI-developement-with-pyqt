import sys
from PyQt5.QtWidgets import QApplication, QWidget,QToolButton,QMenu,QComboBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__() # create default constructor for QWidget
        self.button = QToolButton(self)
        self.initializeUI()
        # model = QStandardItemModel (4, 4)
        # # view = QStandardItemModel (4, 4)
        # for row in range(4):
        #     for column in range(4):
        #         item = QStandardItem("row %d, column %d" % (row, column))
        #         model.setItem(row, column, item)
    
        # # self.tableView.setModel(model)
        # for row in range(4):
        #     c = QComboBox()
        #     c.addItems(['cell11','cell12','cell13','cell14','cell15',])
            # i = self.tableView.model().index(row,2)
            # self.tableView.setIndexWidget(i,c)
    def initializeUI(self):
         """
         Initialize the window and display its contents to the screen.
         """
         self.setGeometry(100, 100, 400, 300)
         self.setWindowTitle('Empty Window in PyQt')
         self.show()
         
         # d = {'a': [1,2,3], 'b': [4,5,6], 'c': [7,8,9]}
         # def callback_factory(k, v):
         #     return lambda: self.button.setText('{0}_{1}'.format(k, v))
      
         # self.menu = QMenu(self)
         # for k, vals in d.items():
         #     sub_menu = self.menu.addMenu(k)
         #     for v in vals:
         #         action = sub_menu.addAction(str(v))
         #         action.triggered.connect(callback_factory(k, v))

         # self.button.setMenu(self.menu)
# Run program
if __name__ == '__main__':
     app = QApplication(sys.argv)
     window = EmptyWindow()
     sys.exit(app.exec_())