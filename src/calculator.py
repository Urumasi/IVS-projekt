"""Calculator module that solves the internal logic of the calculator.

Module links PyQt5 GUI buttons to custom functions that set the result text
accordingly. This modules also solves the expression in result text.
"""

# File: calculator.py
# Author: OkayChamps, Martin Kneslík (xknesl00), Karel Norek (xnorek01) FIT BUT
# Date: 2020-Apr-22

__package__ = "calcchamp"

from PyQt5 import QtCore, QtGui, QtWidgets
from .ui_calculator import Ui_Calculator
from PyQt5.QtWidgets import QApplication
from random import randint
__package__ = 'calcchamp'
from .mathlib import MathLib

class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    key_pressed = QtCore.pyqtSignal(QtCore.QEvent)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.change_style()
        self.key_pressed.connect(self.on_key)

        # Connect buttons to functions.
        # operation buttons
        self.connect_buttons(self.buttons_update, self.button_equals, self.button_plus,
                            self.button_minus, self.button_multiply, self.button_divide,
                            self.button_log, self.button_ln, self.button_sin, self.button_cos,
                            self.button_tan, self.button_cot, self.button_factorial, self.button_negation,
                            self.button_divide_by_x, self.button_random, self.button_sqr,
                            self.button_pow, self.button_exp, self.button_sqrt, self.button_root)
        # change style button
        self.connect_buttons(self.change_style, self.button_change)
        #digits
        self.connect_buttons(self.digit_pressed, self.button_zero, self.button_one,
                            self.button_two, self.button_three, self.button_four,
                            self.button_five, self.button_six, self.button_seven,
                            self.button_eight, self.button_nine)
        # decimal
        self.connect_buttons(self.decimal_pressed, self.button_decimal)
        # equals/result
        self.connect_buttons(self.result_pressed, self.button_equals)
        # basic operations (+ - * /)
        self.connect_buttons(self.basic_ops_pressed, self.button_plus, self.button_minus,
                            self.button_multiply, self.button_divide)
        # advanced operations (log, ln, sin, cos, tan)
        self.connect_buttons(self.advanced_ops_pressed, self.button_log, self.button_ln,
                            self.button_sin, self.button_cos, self.button_tan, self.button_cot)
        # advanced operations
        self.connect_buttons(self.factorial_pressed, self.button_factorial)
        self.connect_buttons(self.negation_pressed, self.button_negation)
        self.connect_buttons(self.divide_by_x_pressed, self.button_divide_by_x)
        self.connect_buttons(self.pow_pressed, self.button_pow)
        self.connect_buttons(self.sqr_pressed, self.button_sqr)
        self.connect_buttons(self.exp_pressed, self.button_exp)
        self.connect_buttons(self.root_pressed, self.button_root)
        self.connect_buttons(self.sqrt_pressed, self.button_sqrt)
        #random
        self.connect_buttons(self.random_pressed, self.button_random)
        # clear buttons
        self.connect_buttons(self.clear_result, self.button_ce)
        self.connect_buttons(self.clear_all, self.button_c)
        self.connect_buttons(self.clear_last, self.button_del)



    def connect_buttons(self, function, *buttons):
        """Connect buttons to a specified functions.

        Args:
            function (function): Function to be linked with buttons.
            *buttons (button): Buttons that are linked to function.
        """
        for button in buttons:
            button.clicked.connect(function)

    def keyPressEvent(self, event):
        """Emits event when key is pressed.
        Buttons can be pressed via keyboard input.

        Args:
            event (event): Key press.
        """
        super(CalculatorWindow, self).keyPressEvent(event)
        self.key_pressed.emit(event)

    def connect_keys(self, pressed_key, button, *keys):
        """Connect keyboard keys to specified buttons.

        Args:
            pressed_key (event): Pressed key event.
            button (button): Buttons that are linked to the pressed keys.
            *keys (key): Keyboard keys.
        """
        for key in keys:
            if pressed_key == key:
                button.animateClick()

    def on_key(self, event):
        """Connect keyboard keys to buttons.

        Args:
            event (event): Keyboard press event.
        """
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

    def hide_buttons(self, *buttons):
        """Hides buttons specified buttons. Used for scientific mode switching.

        Args:
            *buttons (button): Buttons to hide.
        """
        for button in buttons:
            button.hide()

    def show_buttons(self, *buttons):
        """Shows buttons specified buttons. Used for scientific mode switching.

        Args:
            *buttons (button): Buttons to show.
        """
        for button in buttons:
            button.show()

    def buttons_update(self):
        """Checks and updates subresult and result text. Every operation button
        is connected to this function.
        """
        if self.is_result_set():
            self.clear_subresult()

    def change_style(self):
        """Change style to scientific or otherwise.
        Shows and hides scientific buttons.
        """
        scientificButtons = [self.button_factorial, self.button_random, self.button_root,
                            self.button_pow, self.button_exp, self.button_log, self.button_ln,
                            self.button_sin, self.button_cos, self.button_tan, self.button_cot]
        if self.label_style.text() == "Scientific":
            self.hide_buttons(*scientificButtons)
            self.label_style.setText("Standard")
        else:
            self.show_buttons(*scientificButtons)
            self.label_style.setText("Scientific")

    def is_result_set(self):
        """Checks if result is set.

        Returns:
            bool: True if result set, false otherwise.
        """
        return "=" in self.line_subresult.text()

    def is_result_zero(self):
        """Checks if result text is zero, (0 = unset).

        Returns:
            bool: True if result text equals zero, false otherwise.
        """
        return (self.line_result.text() == "0")

    """Clear functions."""
    def clear_result(self):
        """Clears result."""
        self.line_result.setText("0")

    def clear_subresult(self):
        """Clears subresult."""
        self.line_subresult.setText("")

    def clear_all(self):
        """Clears both result and subresult."""
        self.clear_result()
        self.clear_subresult()

    def clear_last(self):
        """Deletes last number in result text."""
        if self.is_result_set():
            self.line_subresult.setText("")
        else:
            self.line_result.setText(self.line_result.text()[:-1])
            if not self.line_result.text():
                self.line_result.setText("0")

    def set_result(self, result):
        self.line_subresult.setText(self.line_subresult.text() + " " + "=")
        self.line_result.setText(str(result))

    #digits
    def digit_pressed(self):
        if len(self.line_result.text()) < 15:
            button = self.sender()
            if self.is_result_set():
                self.clear_all()
            if self.is_number_zero():
                self.line_result.setText("")
            self.line_result.setText(self.line_result.text() + button.text())

    def decimal_pressed(self):
        """Called when decimal point is pressed."""
        button = self.sender()
        if self.is_result_set():
            self.clear_all()
        if "." not in self.line_result.text():
            self.line_result.setText(self.line_result.text() + ".")

    def calculate_result(self):
        try:
            result = self.line_subresult.text()
            string = str(result)
            result = string.split()
            try:
                res = int(result[0])
            except ValueError:
                res = float(result[0])
            for x in range(1, len(result), 2):
                number = result[x + 1]
                try:
                    number = int(number)
                except ValueError:
                    number = float(number)
                if "+" in result[x]:
                    res = round(MathLib.add(res, number), 9)
                if "-" in result[x]:
                    res = round(MathLib.subtract(res, number), 9)
                if "*" in result[x]:
                    res = round(MathLib.multiply(res, number), 9)
                if "/" in result[x]:
                    res = round(MathLib.divide(res, number), 9)

            try:
                res = int(res)
            except ValueError:
                res = float(res)
            self.line_result.setText(str(res))
            self.line_subresult.setText(self.line_subresult.text() + " " + "=")
        except ValueError:
            self.line_result.setText("Math Error")
        except OverflowError:
            self.line_result.setText("Overflow Error")

    #calculating result
    def result_pressed(self):
        """Sets the result text for pressing result button."""
        if "^" in self.line_result.text():
            try:
                string = str(self.line_result.text())
                string = string.split("^")
                try:
                    base = int(string[0])
                except ValueError:
                    base = float(string[0])
                exponent = int(string[1])

                result = round(MathLib.power(base, exponent))
                self.line_result.setText(str(result))

            except ValueError:
                self.line_result.setText("Math Error")

        elif "√" in self.line_result.text():
            try:
                string = str(self.line_result.text())
                string = string.split("√")
                n = int(string[0])
                base = int(string[1])
                result = round(MathLib.root(base, n))
                self.line_result.setText(str(result))

            except ValueError:
                self.line_result.setText("Math Error")

        if not self.is_result_set():
            self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text())
            self.calculate_result()


    def basic_ops_pressed(self):
        r"""Set the result text for basic operations buttons (+, -, \*, /)."""
        button = self.sender()
        if self.is_result_zero() and self.line_subresult.text():
            self.line_subresult.setText(self.line_subresult.text()[:-1] + button.text())
        else:
            self.line_subresult.setText(self.line_subresult.text() + " " + self.line_result.text() + " " + button.text())
            self.line_result.setText("0")

    def advanced_ops_pressed(self):
        try:
            button = (self.sender())
            number = float(self.line_result.text())
            if "ln" in str(button.text()):
                result = round(MathLib.natural_log(number), 9)
                self.line_result.setText(str(result))
            elif "log" in str(button.text()):
                result = round(MathLib.log(number), 9)
                self.line_result.setText(str(result))
            elif "sin" in str(button.text()):
                result = round(MathLib.sin(number), 9)
                self.line_result.setText(str(result))
            elif "cos" in str(button.text()):
                result = round(MathLib.cos(number), 9)
                self.line_result.setText(str(result))
            elif "tan" in str(button.text()):
                result = round(MathLib.tan(number), 9)
                self.line_result.setText(str(result))
            elif "cot" in str(button.text()):
                result = round(MathLib.cot(number), 9)
                self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")
        except OverflowError:
            self.line_result.setText("Overflow Error")

    def factorial_pressed(self):
        try:
            number = int(self.line_result.text())
            result = MathLib._fact(number)
            self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")

    def negation_pressed(self):
        string = self.line_result.text()
        try:
            number = int(string)
        except ValueError:
            number = float(string)
        number = number * -1
        string = str(number)
        self.line_result.setText(string)

    def divide_by_x_pressed(self):
        try:
            number = float(self.line_result.text())
            result = round(MathLib.divide(1, number), 9)
            self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")
        except OverflowError:
            self.line_result.setText("Overflow Error")

    def sqr_pressed(self):
        try:
            number = float(self.line_result.text())
            result = round(MathLib.power(number, 2), 9)
            self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")

    def pow_pressed(self):
        self.line_result.setText(self.line_result.text() + "^")

    def exp_pressed(self):
        try:
            try:
                number = int(self.line_result.text())
            except ValueError:
                number = float(self.line_result.text())
            result = round(MathLib.exp(number), 9)
            self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")

    def sqrt_pressed(self):
        try:
            try:
                number = int(self.line_result.text())
            except ValueError:
                number = float(self.line_result.text())
            result = round(MathLib.root(number, 2), 9)
            self.line_result.setText(str(result))
        except ValueError:
            self.line_result.setText("Math Error")
        except OverflowError:
            self.line_result.setText("Overflow Error")

    def root_pressed(self):
        self.line_result.setText(self.line_result.text() + "√")

    #random number
    def random_pressed(self):
        button = randint(0, 1000)
        string = str(button)
        self.line_result.setText(string)
