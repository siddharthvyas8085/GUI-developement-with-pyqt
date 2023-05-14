import sys
from PyQt5.QtWidgets import QApplication, QWidget


def dialog():
    mbox = QMessageBox()
    #mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    wi=QWidget()
    wi.statusBar().showMessage("3")
    mbox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setFixedWidth(400)
    w.setFixedHeight(300)
    w.setWindowTitle("Guru99")
    w.show()
    sys.exit(app.exec_())