from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    key_pressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.change_style()
        self.key_pressed.connect(self.on_key)
        
        #connect buttons to funcion
        #operation buttons
        self.connect_buttons(self.buttons_update, self.button_equals, self.button_plus, 
                            self.button_minus, self.button_multiply, self.button_divide, 
                            self.button_log, self.button_ln, self.button_sin, self.button_cos, 
                            self.button_tan, self.button_cot, self.button_factorial, self.button_negation, 
                            self.button_divide_by_x, self.button_random, self.button_sqr, 
                            self.button_pow, self.button_exp, self.button_sqrt, self.button_root)
        #change style button
        self.connect_buttons(self.change_style, self.button_change)
        #digits
        self.connect_buttons(self.digit_pressed, self.button_zero, self.button_one, 
                            self.button_two, self.button_three, self.button_four, 
                            self.button_five, self.button_six, self.button_seven, 
                            self.button_eight, self.button_nine)
        #decimal
        self.connect_buttons(self.decimal_pressed, self.button_decimal)
        #equals/result
        self.connect_buttons(self.result_pressed, self.button_equals)
        #basic operations (+ - * /)
        self.connect_buttons(self.basic_ops_pressed, self.button_plus, self.button_minus, 
                            self.button_multiply, self.button_divide)
        #advanced operations (log, ln, sin, cos, tan)
        self.connect_buttons(self.advanced_ops_pressed, self.button_log, self.button_ln,
                            self.button_sin, self.button_cos, self.button_tan, self.button_cot)
        #advamced operations
        self.connect_buttons(self.factorial_pressed, self.button_factorial)
        self.connect_buttons(self.negation_pressed, self.button_negation)
        self.connect_buttons(self.divide_by_x_pressed, self.button_divide_by_x)     
        self.connect_buttons(self.pow_pressed, self.button_sqr, self.button_pow)
        self.connect_buttons(self.exp_pressed, self.button_exp)
        self.connect_buttons(self.root_pressed, self.button_sqrt, self.button_root)
        #random
        self.connect_buttons(self.random_pressed, self.button_random)
        #clear buttons
        self.connect_buttons(self.clear_result, self.button_ce)
        self.connect_buttons(self.clear_all, self.button_c)
        self.connect_buttons(self.clear_last, self.button_del)



    def connect_buttons(self, function, *buttons):
        for button in buttons:
            button.clicked.connect(function)

    def keyPressEvent(self, event):
        super(CalculatorWindow, self).keyPressEvent(event)
        self.key_pressed.emit(event) 

    def connect_keys(self, pressed_key, button, *keys):
        for key in keys:
            if pressed_key == key:
                button.animateClick()

    #connect keyboard to buttons
    def on_key(self, event):
        self.connect_keys(event.key(), self.button_zero, QtCore.Qt.Key_0)
        self.connect_keys(event.key(), self.button_one, QtCore.Qt.Key_1)
        self.connect_keys(event.key(), self.button_two, QtCore.Qt.Key_2)
        self.connect_keys(event.key(), self.button_three, QtCore.Qt.Key_3)
        self.connect_keys(event.key(), self.button_four, QtCore.Qt.Key_4)
        self.connect_keys(event.key(), self.button_five, QtCore.Qt.Key_5)
        self.connect_keys(event.key(), self.button_six, QtCore.Qt.Key_6)
        self.connect_keys(event.key(), self.button_seven, QtCore.Qt.Key_7)
        self.connect_keys(event.key(), self.button_eight, QtCore.Qt.Key_8)
        self.connect_keys(event.key(), self.button_nine, QtCore.Qt.Key_9)
        self.connect_keys(event.key(), self.button_decimal, QtCore.Qt.Key_Comma)
        self.connect_keys(event.key(), self.button_equals, QtCore.Qt.Key_Enter, 
                        QtCore.Qt.Key_Equal, QtCore.Qt.Key_Return)
        self.connect_keys(event.key(), self.button_del, QtCore.Qt.Key_Backspace, 
                        QtCore.Qt.Key_Delete)
        self.connect_keys(event.key(), self.button_plus, QtCore.Qt.Key_Plus)
        self.connect_keys(event.key(), self.button_minus, QtCore.Qt.Key_Minus)
        self.connect_keys(event.key(), self.button_multiply, QtCore.Qt.Key_Asterisk)
        self.connect_keys(event.key(), self.button_divide, QtCore.Qt.Key_Slash)


    #hides buttons from scientific version
    def hide_buttons(self, *buttons):
        for button in buttons:
            button.hide()

    def show_buttons(self, *buttons):
        for button in buttons:
            button.show()

    #function to check and update subresult and result text
    #every operation button is connected to this function
    def buttons_update(self):
        if self.is_result_set():
            self.clear_subresult()

    def change_style(self):
        if self.label_style.text() == "Scientific":
            self.hide_buttons(self.button_factorial, self.button_random, self.button_root, 
                            self.button_pow, self.button_exp, self.button_log, self.button_ln, 
                            self.button_sin, self.button_cos, self.button_tan, self.button_cot)
            self.label_style.setText("Standard")
        else:
            self.show_buttons(self.button_factorial, self.button_random, self.button_root, 
                            self.button_pow, self.button_exp, self.button_log, self.button_ln, 
                            self.button_sin, self.button_cos, self.button_tan, self.button_cot)
            self.label_style.setText("Scientific")

    #checks if result is set
    def is_result_set(self):
        return ("=" in self.line_subresult.text())

    #checks if number is set (0 = unset)
    def is_number_zero(self):
        return (self.line_result.text() == "0")

    #clear functions
    def clear_result(self):
        self.line_result.setText("0")
    
    def clear_subresult(self):
        self.line_subresult.setText("")
    
    def clear_all(self):
        self.line_result.setText("0")
        self.line_subresult.setText("")

    def clear_last(self):
        if self.is_result_set():
            self.line_subresult.setText("")
        else: 
            self.line_result.setText(self.line_result.text()[:-1])
            if not self.line_result.text():
                self.line_result.setText("0")

    #digits
    def digit_pressed(self):
        button = self.sender()
        if self.is_result_set():
            self.clear_all()
        if self.is_number_zero():
            self.line_result.setText("")     
        self.line_result.setText(self.line_result.text() + button.text())
    
    def decimal_pressed(self):
        button = self.sender() 
        if self.is_result_set():
            self.clear_all()
        if button.text() not in self.line_result.text():
            self.line_result.setText(self.line_result.text() + button.text())

    #calculating result
    def result_pressed(self):
        button = self.sender()
        if not self.is_result_set():
            self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())

            #TODO 
            self.line_result.setText("result")

    #basic operations (+ - * /)
    def basic_ops_pressed(self):
        button = self.sender()
        if self.is_number_zero() and self.line_subresult.text():
            self.line_subresult.setText(self.line_subresult.text()[:-1] + button.text())
        else:
            self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
            self.line_result.setText("0")

    #advanced operations (ln, log, sin, cos, tan)
    def advanced_ops_pressed(self):
        button = self.sender()
        self.line_result.setText(button.text() + "(" + self.line_result.text() + ")")

    #other advanced operations
    def factorial_pressed(self):
        print("TODO")

    def negation_pressed(self):
        print("TODO")

    def divide_by_x_pressed(self):
        print("TODO")

    def pow_pressed(self):
        print("TODO")

    def exp_pressed(self):
        print("TODO")

    def root_pressed(self):
        print("TODO")
    
    #random number
    def random_pressed(self):
        print("TODO")

