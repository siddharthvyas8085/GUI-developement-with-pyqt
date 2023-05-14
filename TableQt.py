# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:04:12 2022

@author: Bisar
"""
import sys
from PyQt5.QtWidgets import (QApplication,QApplication, QComboBox,QMainWindow, QWidget, QTableView,
                               QPushButton,QCheckBox, QFontComboBox,QTableWidget,QTableWidgetItem)
from PyQt5.QtCore import (Qt, QAbstractTableModel)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import (QColor)
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.setCentralWidget(self.table)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']
        data3 = ['0','0','0','0']
        combo_box_options = ["Option 1","Option 2","Option 3"]
        self.combo1,self.combo2,self.combo3,self.combo4 = QCheckBox(),QCheckBox(),QCheckBox(),QCheckBox()
        self.table.setRowCount(4)

        for index in range(4):
            item1 = QTableWidgetItem(data1[index])
            self.table.setItem(index,0,item1)
            item2 = QTableWidgetItem(data2[index])
            self.table.setItem(index,1,item2)
            item3 = QTableWidgetItem(data3[index])
            self.table.setItem(index,3,item3)
        self.table.setCellWidget(0,2,self.combo1)
        self.table.setCellWidget(1,2,self.combo2)
        self.table.setCellWidget(2,2,self.combo3)
        self.table.setCellWidget(3,2,self.combo4)
        self.cbox = [self.combo1,self.combo2,self.combo3,self.combo4]
        # for item in self.cbox:
        self.combo1.stateChanged.connect(self.table_setup1)
        self.combo2.stateChanged.connect(self.table_setup2)
        self.combo3.stateChanged.connect(self.table_setup3)
        self.combo4.stateChanged.connect(self.table_setup4)
    def table_setup1(self,state):
        if state == QtCore.Qt.Checked:
            i=0
            item = QTableWidgetItem(str(i+1))
            self.table.setItem(0,3,item)
    def table_setup2(self,state):
        if state == QtCore.Qt.Checked:
            i=0
            item = QTableWidgetItem(str(i+1))
            self.table.setItem(1,3,item)
    def table_setup3(self,state):
        if state == QtCore.Qt.Checked:
            i=0
            item = QTableWidgetItem(str(i+1))
            self.table.setItem(2,3,item)
    def table_setup4(self,state):
        if state == QtCore.Qt.Checked:
            i=0
            item = QTableWidgetItem(str(i+1))
            self.table.setItem(3,3,item)
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()