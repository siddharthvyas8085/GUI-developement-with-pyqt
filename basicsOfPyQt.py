import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton,QGridLayout
# from Qbox_layout impot *
class MyForms():
     def __init__(self):
        super(MyForms, self).__init__()
        #super().__init__()
        #self.ui=Ui.Dialog()
        self.setupUi(self)
        self.show()
if __name__ == '_main_':
    app = QApplication(sys.argv)
    w = MyForms(sys.argv)
    w.show()
    sys.exit(app.exec_())
