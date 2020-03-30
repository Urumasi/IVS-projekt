
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from ui_calculator import Ui_Calculator

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.swap_style()
        self.keyPressed.connect(self.on_key)

        #connect buttons
        self.connect_buttons(self.swap_style, self.button_change)
        self.connect_buttons(self.digit_pressed, self.button_zero, self.button_one, self.button_two, self.button_three, self.button_four, self.button_five, self.button_six, self.button_seven, self.button_eight, self.button_nine)
        self.connect_buttons(self.decimal_pressed, self.button_decimal)
        self.connect_buttons(self.result_pressed, self.button_equals)
        self.connect_buttons(self.basic_ops_pressed, self.button_plus, self.button_minus, self.button_multiply, self.button_divide)
        self.connect_buttons(self.clear_pressed, self.button_ce, self.button_c, self.button_del)


    def keyPressEvent(self, event):
        super(CalculatorWindow, self).keyPressEvent(event)
        self.keyPressed.emit(event) 

    def connect_keys(self, pressed_key, button, *keys):
        for key in keys:
            if pressed_key == key:
                button.animateClick()

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
        self.connect_keys(event.key(), self.button_equals, QtCore.Qt.Key_Enter, QtCore.Qt.Key_Equal, QtCore.Qt.Key_Return)
        self.connect_keys(event.key(), self.button_del, QtCore.Qt.Key_Backspace, QtCore.Qt.Key_Delete)
        self.connect_keys(event.key(), self.button_plus, QtCore.Qt.Key_Plus)
        self.connect_keys(event.key(), self.button_minus, QtCore.Qt.Key_Minus)
        self.connect_keys(event.key(), self.button_multiply, QtCore.Qt.Key_Asterisk)
        self.connect_keys(event.key(), self.button_divide, QtCore.Qt.Key_Slash)


    def connect_buttons(self, function, *buttons):
        for button in buttons:
            button.clicked.connect(function)

    def hide_buttons(self, *buttons):
        for button in buttons:
            button.hide()

    def show_buttons(self, *buttons):
        for button in buttons:
            button.show()

    def swap_style(self):
        if self.label_style.text() == "Scientific":
            self.hide_buttons(self.buttona, self.buttonb, self.buttonc, self.buttond, self.buttone, self.buttonf, self.buttong, self.buttonh, self.buttoni, self.buttonj, self.buttonk)
            self.label_style.setText("Standard")
        else:
            self.show_buttons(self.buttona, self.buttonb, self.buttonc, self.buttond, self.buttone, self.buttonf, self.buttong, self.buttonh, self.buttoni, self.buttonj, self.buttonk)
            self.label_style.setText("Scientific")
    
    def clear(self, case):
        if case == "CE":
            self.line_result.setText("0")
        elif case == "C":
            self.line_result.setText("0")
            self.line_subresult.setText("")
        elif case == "CS":
            self.line_subresult.setText("")
        elif case == "DEL":
            if "=" in self.line_subresult.text():
                self.line_subresult.setText("")
            else: 
                self.line_result.setText(self.line_result.text()[:-1])
                if not self.line_result.text():
                    self.line_result.setText("0")

    def clear_pressed(self):
        button = self.sender()
        self.clear(button.text())
    
    def digit_pressed(self):
        button = self.sender()
        if "=" in self.line_subresult.text():
            self.clear("C")
        if self.line_result.text() == "0":
            self.line_result.setText("")     
        self.line_result.setText(self.line_result.text() + button.text())
    
    def decimal_pressed(self):
        button = self.sender() 
        if "=" in self.line_subresult.text():
            self.clear("C")
        if button.text() not in self.line_result.text():
            self.line_result.setText(self.line_result.text() + button.text())

    def result_pressed(self):
        button = self.sender()
        if "=" not in self.line_subresult.text():
            self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
            self.line_result.setText("výsledek")

    def basic_ops_pressed(self):
        button = self.sender()
        if "=" in self.line_subresult.text():
            self.clear("CS")
        self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
        self.line_result.setText("0")

