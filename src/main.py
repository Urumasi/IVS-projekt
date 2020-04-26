#!/usr/bin/env python3

"""Main module for running the calculator as a whole application."""

# File: main.py
# Author: Okaychamps, FIT BUT
# Date: 2020-Apr-22

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow


if __name__ == '__main__':
	app = QApplication(sys.argv)
	calculator = CalculatorWindow()
	sys.exit(app.exec_())
