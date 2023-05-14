# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:23:00 2022

@author: Bisar
"""

# Import necessary modules

import sys

from PyQt5 import QtCore, QtWidgets

from PyQt5.QtWidgets import QMainWindow, QCheckBox, QLabel, QVBoxLayout, QDesktopWidget

# Define class for creating the form with single checkbox

class SingleCheckbox(QMainWindow):

    def __init__(self):

        super().__init__()


        # Create the label text for the user

        lb = QLabel("Do you like programming?", self)

        lb.setGeometry(20, 20, 200, 20)

        lb.move(20, 20)


        # Create a checkbox with the label

        cb = QCheckBox('Yes', self)

        cb.stateChanged.connect(self.Check_Answer)

        cb.move(20, 50)


        # Set the vertical Qt Layout

        vbox = QVBoxLayout()

        vbox.addWidget(lb)

        vbox.addWidget(cb)


        # Set the window title and size

        self.setWindowTitle('Form with Single Checkbox')

        self.setGeometry(60, 60, 300, 100)


        # Display the window in the center of the screen

        win = self.frameGeometry()

        pos = QDesktopWidget().availableGeometry().center()

        win.moveCenter(pos)

        self.move(win.topLeft())

        self.show()


    # Define function to check the user's input

    def Check_Answer(self, state):


        if state == QtCore.Qt.Checked:

            print("Wow! You like programming.")

        else:

            print("Oh no!, You don't like programming.")

# Create app object and execute the app

app = QtWidgets.QApplication(sys.argv)

form = SingleCheckbox()

app.exec()