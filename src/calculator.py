
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        
        #connect buttons
        self.button_change.clicked.connect(self.swap_style)
        self.button_change.click()

        self.button_ce.clicked.connect(self.clear_pressed)
        self.button_c.clicked.connect(self.clear_pressed)
        self.button_del.clicked.connect(self.clear_pressed)
        
        self.button_zero.clicked.connect(self.digit_pressed)
        self.button_one.clicked.connect(self.digit_pressed)
        self.button_two.clicked.connect(self.digit_pressed)
        self.button_three.clicked.connect(self.digit_pressed)
        self.button_four.clicked.connect(self.digit_pressed)
        self.button_five.clicked.connect(self.digit_pressed)
        self.button_six.clicked.connect(self.digit_pressed)
        self.button_seven.clicked.connect(self.digit_pressed)
        self.button_eight.clicked.connect(self.digit_pressed)
        self.button_nine.clicked.connect(self.digit_pressed)

        self.button_decimal.clicked.connect(self.decimal_pressed)
        self.button_equals.clicked.connect(self.result_pressed)

        self.button_plus.clicked.connect(self.basic_ops_pressed)
        self.button_minus.clicked.connect(self.basic_ops_pressed)
        self.button_multiply.clicked.connect(self.basic_ops_pressed)
        self.button_divide.clicked.connect(self.basic_ops_pressed)

    def swap_style(self):
        if self.buttona.isVisible():
            self.buttona.hide()
            self.buttonb.hide()
            self.buttonc.hide()
            self.buttond.hide()
            self.buttone.hide()
            self.buttonf.hide()
            self.buttong.hide()
            self.buttonh.hide()
            self.buttoni.hide()
            self.buttonj.hide()
            self.buttonk.hide()
            self.label_style.setText("Standard")
        else:
            self.buttona.show()
            self.buttonb.show()
            self.buttonc.show()
            self.buttond.show()
            self.buttone.show()
            self.buttonf.show()
            self.buttong.show()
            self.buttonh.show()
            self.buttoni.show()
            self.buttonj.show()
            self.buttonk.show()
            self.label_style.setText("Scientific")
            
    def clear_pressed(self):
        button = self.sender()
        if button.text() == "CE":
            self.line_result.setText("0")
        elif button.text() == "C":
            self.line_result.setText("0")
            self.line_subresult.setText("")
        elif button.text() == "DEL":
            self.line_result.setText(self.line_result.text()[:-1])
            if not self.line_result.text():
                self.line_result.setText("0")
    
    def digit_pressed(self):
        button = self.sender()
        if "=" in self.line_subresult.text():
            self.button_c.click()
        if self.line_result.text() == "0":
            self.line_result.setText("")     
        self.line_result.setText(self.line_result.text() + button.text())
    
    def decimal_pressed(self):
        button = self.sender() 
        if button.text() not in self.line_result.text():
            self.line_result.setText(self.line_result.text() + button.text())

    def result_pressed(self):
        button = self.sender()
        self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
        self.line_result.setText("výsledek")

    def basic_ops_pressed(self):
        button = self.sender()
        if "=" in self.line_subresult.text():
            self.line_subresult.setText("")
        self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
        self.line_result.setText("0")