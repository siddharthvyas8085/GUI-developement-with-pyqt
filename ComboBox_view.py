# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:35:23 2022

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
		geek_list = ["Sayian", "Super Saiyan", "Super Sayian 2",
											"Super Sayian B"]

		# making it editable
		self.combo_box.setEditable(True)

		# creating a view
		view = QTreeView()

		# setting view to combo box
		self.combo_box.setView(view)

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# getting view
		get_view = self.combo_box.view()

		# creating label to dhow the view object
		label = QLabel("view = " + str(get_view), self)

		# setting geometry of the label
		label.setGeometry(150, 100, 300, 30)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
