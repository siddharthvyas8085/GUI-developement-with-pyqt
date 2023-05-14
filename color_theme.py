import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.black)
    qp.setColor(QPalette.Button, Qt.green)
    app.setPalette(qp)

    w = QWidget()

    grid = QGridLayout(w)
    grid.addWidget(QPushButton("Button one"), 0, 0)
    grid.addWidget(QPushButton("Button two"), 0, 1)
    grid.addWidget(QPushButton("Button three"), 1, 0)
    grid.addWidget(QPushButton("Button four"), 1, 1)

    w.show()
    sys.exit(app.exec_())


# class myClass():
#     def method1(self):
#         print("Guru99")
#
#     def method2(self, someString):
#         print("Software Testing:" + someString)
#
#
# def main():
#     # exercise the class methods
#     c = myClass()
#     c.method1()
#     c.method2(" Testing is fun")


if __name__ == "__main__":
    main()