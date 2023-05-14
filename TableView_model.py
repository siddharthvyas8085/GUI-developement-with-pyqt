# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:02:04 2022

@author: Bisar
"""

import sys
import time

from typing import Union, Any

import PyQt5 as PySide6
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTableView,
                               QPushButton, QFontComboBox)
from PyQt5.QtCore import (Qt, QAbstractTableModel)
from PyQt5.QtGui import (QColor)


class TableModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.values = [["Hello", 2, 5],
                       [22, 55, 6],
                       [2.3, "Kion", time.time()],
                       [2.22, "widget-here", "another-widget-here"]]
        self.initUI()

    def initUI(self):
        pass

    def rowCount(self, index):
        return len(self.values)

    def columnCount(self, index):
        return len(self.values[0])

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        if role == Qt.DisplayRole:
            return self.values[index.row()][index.column()]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableView = QTableView()
        self.tableModel = TableModel()
        self.tableView.setModel(self.tableModel)
        self.tableView.setIndexWidget(self.tableView.model().index(3, 1), QPushButton("Kill"))
        self.tableView.setIndexWidget(self.tableView.model().index(3, 2), QFontComboBox())

        self.setCentralWidget(self.tableView)
        # print(self.tableModel.rowCount(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()