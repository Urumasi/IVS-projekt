import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from calculator import CalculatorWindow


if __name__ == '__main__':
	app = QApplication(sys.argv)
	calculator = CalculatorWindow()
	sys.exit(app.exec_())	
