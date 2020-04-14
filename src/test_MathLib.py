import unittest
from unittest import TestCase

from MathLib import MathLib


class MathLibTests(TestCase):
	def setUp(self):
		self.math = MathLib()

	# Tests for add function
	def test_add_positive(self):
		self.assertEqual(self.math.add(1, 3), 4)
		self.assertEqual(self.math.add(13, 19), 32)
		self.assertEqual(self.math.add(0, 1), 1)
		self.assertEqual(self.math.add(1, 0), 1)
		self.assertEqual(self.math.add(0, 0), 0)

	def test_add_negative(self):
		self.assertEqual(self.math.add(-1, -3), -4)
		self.assertEqual(self.math.add(-25, -56), -81)
		self.assertEqual(self.math.add(-1, 0), -1)
		self.assertEqual(self.math.add(0, -1), -1)

	def test_add_both(self):
		self.assertEqual(self.math.add(-1, 2), 1)
		self.assertEqual(self.math.add(1, -2), -1)
		self.assertEqual(self.math.add(-23, 56), 33)
		self.assertEqual(self.math.add(20, -20), 0)
		self.assertEqual(self.math.add(-1, 1), 0)

	def test_add_float(self):
		self.assertAlmostEqual(self.math.add(-1.5, -3.5), -5, 1)
		self.assertAlmostEqual(self.math.add(5.3, 10.4), 15.7, 1)
		self.assertAlmostEqual(self.math.add(5.4, -5.3), 0.1, 1)
		self.assertAlmostEqual(self.math.add(-1.3, 3.3), 2, 1)

	# Tests for sub function
	def test_sub_positive(self):
		self.assertEqual(self.math.subtract(7, 3), 4)
		self.assertEqual(self.math.subtract(3, 7), -4)
		self.assertEqual(self.math.subtract(0, 3), -3)
		self.assertEqual(self.math.subtract(3, 0), 3)
		self.assertEqual(self.math.subtract(0, 0), 0)
		self.assertEqual(self.math.subtract(10, 10), 0)
		self.assertEqual(self.math.subtract(54, 22), 32)

	def test_sub_negative(self):
		self.assertEqual(self.math.subtract(-4, -3), -1)
		self.assertEqual(self.math.subtract(-3, -4), 1)
		self.assertEqual(self.math.subtract(0, -3), 3)
		self.assertEqual(self.math.subtract(-3, 0), -3)
		self.assertEqual(self.math.subtract(-56, -45), -11)

	def test_sub_both(self):
		self.assertEqual(self.math.subtract(7, -3), 10)
		self.assertEqual(self.math.subtract(-7, 3), -10)
		self.assertEqual(self.math.subtract(54, -10), 64)
		self.assertEqual(self.math.subtract(-54, 10), -64)

	def test_sub_float(self):
		self.assertEqual(self.math.subtract(5.5, 3.3), 2.2)
		self.assertEqual(self.math.subtract(-7.4, -2.4), -5)
		self.assertEqual(self.math.subtract(10.5, -2.4), 12.9)
		self.assertEqual(self.math.subtract(-5.2, 10), -15.2)

	# Tests for multiply function
	def test_multiply_positive(self):
		self.assertEqual(self.math.multiply(3, 2), 6)
		self.assertEqual(self.math.multiply(2, 3), 6)
		self.assertEqual(self.math.multiply(0, 2), 0)
		self.assertEqual(self.math.multiply(4, 0), 0)
		self.assertEqual(self.math.multiply(0, 0), 0)
		self.assertEqual(self.math.multiply(45, 23), 1035)

	def test_multiply_negative(self):
		self.assertEqual(self.math.multiply(-3, -2), 6)
		self.assertEqual(self.math.multiply(0, -2), 0)
		self.assertEqual(self.math.multiply(-2, 0), 0)
		self.assertEqual(self.math.multiply(-12, -34), 408)

	def test_multiply_both(self):
		self.assertEqual(self.math.multiply(3, -2), -6)
		self.assertEqual(self.math.multiply(-3, 2), -6)
		self.assertEqual(self.math.multiply(-12, 2), -24)
		self.assertEqual(self.math.multiply(2, -12), -24)

	def test_multiply_float(self):
		self.assertAlmostEqual(self.math.multiply(3.3, 2.2), 7.26, 2)
		self.assertAlmostEqual(self.math.multiply(-6.2, -2.1), 13.02, 2)
		self.assertAlmostEqual(self.math.multiply(-3.3, 2.2), -7.26, 2)
		self.assertAlmostEqual(self.math.multiply(6.2, -2.1), -13.02, 2)

	# Tests for divide function
	def test_divide_positive(self):
		self.assertEqual(self.math.divide(5, 1), 5)
		self.assertEqual(self.math.divide(1, 2), 0.5)
		self.assertEqual(self.math.divide(0, 1), 0)
		self.assertEqual(self.math.divide(55, 2), 27.5)

	def test_divide_negative(self):
		self.assertEqual(self.math.divide(-10, -2), 5)
		self.assertEqual(self.math.divide(-1, -2), 0.5)
		self.assertEqual(self.math.divide(0, -2), 0)
		self.assertEqual(self.math.divide(-55, -11), 5)

	def test_divide_both(self):
		self.assertAlmostEqual(self.math.divide(-10, 2), -5, 1)
		self.assertAlmostEqual(self.math.divide(10, -2), -5, 1)
		self.assertAlmostEqual(self.math.divide(-55, 2), -27.5, 1)
		self.assertAlmostEqual(self.math.divide(55, -11), -5, 1)

	def test_divide_float(self):
		self.assertAlmostEqual(self.math.divide(5.5, 1.1), 5, 1)
		self.assertAlmostEqual(self.math.divide(-3.2, -0.5), 6.4, 1)
		self.assertAlmostEqual(self.math.divide(10.3, -2), -5.15, 2)
		self.assertAlmostEqual(self.math.divide(-10, 2.5), -4, 1)

	def test_divide_zero(self):
		with self.assertRaises(ValueError):
			self.math.divide(2, 0)

	# Tests for power function
	def test_power_even(self):
		self.assertEqual(self.math.power(1, 4), 1)
		self.assertEqual(self.math.power(2, 2), 4)
		self.assertEqual(self.math.power(-5, 2), 25)
		self.assertEqual(self.math.power(2.5, 2), 6.25)

		with self.assertRaises(ValueError):
			self.math.power(0, 0)

	def test_power_odd(self):
		self.assertEqual(self.math.power(1, 3), 1)
		self.assertEqual(self.math.power(2, 3), 8)
		self.assertEqual(self.math.power(-2, 3), -8)
		self.assertEqual(self.math.power(2.5, 3), 15.625)

	def test_power_base(self):  # Base need to be natural number
		with self.assertRaises(ValueError):
			self.math.power(2, 0)
			self.math.power(3, -5)
			self.math.power(-4, 1.5)
			self.math.power(5.5, -1)

	# Tests for root function
	def test_root_even(self):
		self.assertEqual(self.math.root(1, 2), 1)
		self.assertEqual(self.math.root(4, 2), 2)
		self.assertAlmostEqual(self.math.root(2, 2), 1.41, 2)

	def test_root_odd(self):
		self.assertEqual(self.math.root(1, 3), 1)
		self.assertEqual(self.math.root(27, 3), 3)
		self.assertEqual(self.math.root(8, 3), 2)

	def test_root_number(self):
		with self.assertRaises(ValueError):
			self.math.root(-5, 2)
			self.math.root(-1.5, 2)

	# Tests for sin function
	def test_sin(self):
		self.assertAlmostEqual(self.math.sin(1), 0.8415, 4)
		self.assertAlmostEqual(self.math.sin(5), -0.9589, 4)
		self.assertAlmostEqual(self.math.sin(-1), -0.8415, 4)
		self.assertAlmostEqual(self.math.sin(1.6), 0.9996, 4)

	# Tests for cos function
	def test_cos(self):
		self.assertAlmostEqual(self.math.cos(1), 0.5403, 4)
		self.assertAlmostEqual(self.math.cos(2), -0.4161, 4)
		self.assertAlmostEqual(self.math.cos(-4), -0.6536, 4)
		self.assertAlmostEqual(self.math.cos(1.5), 0.0707, 4)

	# Tests for tan function
	def test_tan(self):
		self.assertAlmostEqual(self.math.tan(1), 1.5574, 4)
		self.assertAlmostEqual(self.math.tan(0.8), 1.0296, 4)
		self.assertAlmostEqual(self.math.tan(4), 1.1578, 4)
		self.assertAlmostEqual(self.math.tan(3.5), 0.3746, 4)

	# Tests for exp function
	def test_exp(self):
		self.assertAlmostEqual(self.math.exp(1), 2.7183, 4)
		self.assertAlmostEqual(self.math.exp(2), 7.3891, 4)
		self.assertAlmostEqual(self.math.exp(-2), 0.1353, 4)
		self.assertAlmostEqual(self.math.exp(1.5), 4.4817, 4)

	# Tests for natural_log function
	def test_natural_log(self):
		self.assertEqual(self.math.natural_log(1), 0)
		self.assertAlmostEqual(self.math.natural_log(2), 0.6931, 4)
		self.assertAlmostEqual(self.math.natural_log(3.5), 1.2528, 4)

	def test_negative_natural_log(self):
		with self.assertRaises(ValueError):
			self.math.natural_log(0)
			self.math.natural_log(-5)
			self.math.natural_log(-2.5)

	# Tests for log function
	def test_log(self):
		self.assertAlmostEqual(self.math.log(1), 0, 1)
		self.assertAlmostEqual(self.math.log(100), 2, 1)
		self.assertAlmostEqual(self.math.log(2), 0.3010, 4)

	def test_negative_log(self):
		with self.assertRaises(ValueError):
			self.math.log(0)
			self.math.log(-1)
			self.math.log(-2.5)
