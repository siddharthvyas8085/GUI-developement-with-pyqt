# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:40:40 2022

@author: Bisar
"""

# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a combo box widget
		self.combo_box = QComboBox(self)

		# setting geometry of combo box
		self.combo_box.setGeometry(200, 150, 150, 30)

		# geek list
		geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]

		# making it editable
		self.combo_box.setEditable(True)

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# tool tip
		tip = "Drop down tool tip"

		# getting view part of combo box
		view = self.combo_box.view()

		# setting tool tip to view object of the combo box
		view.setToolTip(tip)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
