"""Mathematical library module serves for defining mathematical functions.

Uses taylor decorator for functions that need Taylor series.
Mathlib module is used in our calculator to compute pressed numbers.
"""

# File: mathlib.py
# Author: Okaychamps, Petr Salaba (xsalab00), FIT BUT
# Date: 2020-Apr-22

def taylor(fn):
	"""	Decorator for creating Taylor series, waits until the last 3 terms
	are below EPS or until max number of iterations is reached.

	Args:
		fn (function): Decorated function.

	Returns:
		wrapper: Wrapper.
	"""

	def wrapper(x):
		"""Wrapper function.

		Args:
			x (float): Input number.

		Returns:
			float: Result of called function.
		"""
		last_3 = list()
		result = 0
		for i in range(MathLib.MAX_ITERATIONS):
			next_term = fn(x, i)
			result += next_term

			last_3.append(next_term)
			while len(last_3) > 3:
				last_3.pop(0)

			if len(last_3) == 3 and all(map(lambda x: x < MathLib.EPS, last_3)):
				return result
		return result

	return wrapper


def taylor_mod(fn, lower_bound, upper_bound):
	"""Decorator for creating a Taylor series with modulo,
	useful for periodic functions.

	Args:
		fn (function): Decorated function.
		lower_bound (int): Lower bound of the modulo window.
		upper_bound (int): Upper bound of the modulo window,
						   must be greater than lower_bound.

	Returns:
		wrapper: Wrapper.
	"""

	def wrapper(x):
		difference = upper_bound - lower_bound
		if x < lower_bound:
			off_by = lower_bound - x
			x += difference * (1 + off_by // difference)
		if x > upper_bound:
			off_by = x - upper_bound
			x -= difference * (1 + off_by // difference)
		return taylor(fn)(x)

	return wrapper


def taylor_mod_pi(fn):
	"""Decorator for creating a Taylor series with modulo (-PI, PI), useful for
	trigonometric functions.
	This exists since you must pass constants to decorators.

	Args:
		fn (function): Decorated function.
	"""

	def wrapper(x):
		return taylor_mod(fn, -MathLib.PI, MathLib.PI)(x)

	return wrapper


class MathLib:
	PI = 3.141592653589793
	E = 2.718281828459045
	LN10 = 2.302585092994046

	PRECISION = 12
	EPS = 0.1 ** PRECISION

	MAX_ITERATIONS = 256

	# Used for Taylor series
	@staticmethod
	def _fact(n):
		"""Get the factorial of a number.

		Args:
			n (int): Input number.

		Raises:
			ValueError: Number is not an integer.

		Returns:
			int: n!
		"""
		if not isinstance(n, int) or n < 0:
			raise ValueError
		value = 1
		for x in range(1, n + 1):
			value *= x
		return value

	@staticmethod
	def abs(x):
		r"""Get the absolute value of a number.

		Args:
			x (float): Input number.

		Returns:
			float: Absolute value of x, \|x\|.
		"""
		return x if x > 0 else -x

	@staticmethod
	def add(a, b):
		"""Adds two numbers,

		Args:
			a (float): First number,
			b (float): Second number,

		Returns:
			float: a + b.
		"""
		return a + b

	@staticmethod
	def subtract(a, b):
		"""Substracts one number from another number.

		Args:
			a (float): Number to subtract from.
			b (float): Number to subtract.

		Returns:
			float: a - b.
		"""
		return a - b

	@staticmethod
	def multiply(a, b):
		"""Multiplies two numbers.

		Args:
			a (float): First number.
			b (float): Second number.

		Returns:
			float: a * b.
		"""
		return a * b

	@staticmethod
	def divide(a, b):
		"""Divides one number by another number.

		Args:
			a (float): Numerator.
			b (float): Denominator

		Raises:
			ValueError: Denominator is 0, division by zero.

		Returns:
			float: a / b.
		"""
		if b == 0:
			raise ValueError
		return a / b

	@staticmethod
	def power(base, exponent):
		"""Raises a number to a power based on the exponent.

		Args:
			base (float): Number to raise to a power.
			exponent (int): Natural number, which power to raise the base to.

		Raises:
			ValueError: Exponent is not an integer.
			ValueError: Both base and exponent are zeros.

		Returns:
			float: base ^ exponent.
		"""
		if not isinstance(exponent, int):
			raise ValueError
		if base == 0 and exponent == 0:
			raise ValueError
		return base ** exponent

	@staticmethod
	def root(x, n):
		"""Takes the n-th root of a number.

		Args:
			x (float): Number to take n-th root of.
			n (n): Order of the root.

		Raises:
			ValueError: Order of the root equals zero.
			ValueError: Order of the root is not an integer.
			ValueError: Even Root of a negative number.
						Result is in complex numbers.

		Returns:
			float: n√x.
		"""
		if n == 0:
			raise ValueError
		if not isinstance(n, int):
			raise ValueError
		if n % 2 == 0 and x < 0:
			raise ValueError
		return x ** (1 / n)

	@staticmethod
	@taylor_mod_pi
	def sin(x, i):
		"""Take the sine function of a number.

		Args:
			x (float): Input in radians.
			i (int): Index of a member in the Taylor's series. TODO: remove?

		Returns:
			float: sin(x).
		"""
		return MathLib.power(-1, i) * MathLib.power(x, 2 * i + 1) / MathLib._fact(2 * i + 1)

	@staticmethod
	@taylor
	def cos(x, i):
		"""Take the cosine function of a number.

		Args:
			x (float): Input in radians.
			i (int): Index of a member in the Taylor's series. TODO: remove?

		Returns:
			float: cos(x).
		"""
		return MathLib.power(-1, i) * MathLib.power(x, 2 * i) / MathLib._fact(2 * i)

	@staticmethod
	def tan(x):
		"""Take the tangent function of a number.

		Args:
			x (float): Input in radians.

		Raises:
			ValueError: Input number is zero.

		Returns:
			float: tan(x).
		"""
		cos_x = MathLib.cos(x)
		if MathLib.abs(cos_x) < MathLib.EPS:
			raise ValueError
		return MathLib.divide(MathLib.sin(x), cos_x)

	@staticmethod
	def cot(x):
		"""Take the cotangent function of x.

		Args:
			x (float): Input in radians.

		Raises:
			ValueError: Input number is zero.

		Returns:
			float: cot(x).
		"""
		sin_x = MathLib.sin(x)
		if MathLib.abs(sin_x) < MathLib.EPS:
			raise ValueError
		return MathLib.divide(MathLib.cos(x), sin_x)

	@staticmethod
	@taylor
	def exp(x, i):
		"""The exponential function of a number.

		Args:
			x (float): Input number.
			i (int): Index of a member in the Taylor's series. TODO: remove?

		Returns:
			float: e ^ x.
		"""
		return MathLib.divide(MathLib.power(x, i), MathLib._fact(i))

	@staticmethod
	@taylor
	def natural_log(x, i):
		"""Take the natural logarithm of a number.

		Args:
			x (float): Input number.
			i (int): Index of a member in the Taylor's series. TODO: remove?

		Raises:
			ValueError: Input number is less than zero.

		Returns:
			float: ln(x).
		"""
		if x <= 0:
			raise ValueError
		return 2 * MathLib.power((x - 1) / (x + 1), 2 * i + 1) / (2 * i + 1)

	@staticmethod
	def log(x):
		"""Take the base 10 logarithm of a number.

		Args:
			x (float): Input number.

		Returns:
			float: log10(x).
		"""
		return MathLib.natural_log(x) / MathLib.LN10
