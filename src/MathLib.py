def taylor(fn):
	"""
	Decorator for creating Taylor series, waits until the last 3 terms are below EPS
	or until max number of iterations is reached
	"""

	def wrapper(x):
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
	"""
	Decorator for creating a Taylor series with modulo, useful for periodic functions
	:param lower_bound: Lower bound of the modulo window
	:param upper_bound: Upper bound of the modulo window, must be greater than lower_bound
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
	"""
	Decorator for creating a Taylor series with modulo (-PI, PI), useful for trigonometric functions
	This exists since you must pass constants to decorators
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
		"""
		Get the factorial of n
		:param n: Input number
		:return: n!
		"""
		if not isinstance(n, int) or n < 0:
			raise ValueError
		value = 1
		for x in range(1, n + 1):
			value *= x
		return value

	@staticmethod
	def add(a, b):
		"""
		Adds two numbers
		:param a: First number
		:param b: Second number
		:return: a+b
		"""
		return a + b

	@staticmethod
	def subtract(a, b):
		"""
		Subtracts one number from another number
		:param a: Number to subtract from
		:param b: Number to subtract
		:return: a-b
		"""
		return a - b

	@staticmethod
	def multiply(a, b):
		"""
		Multiplies two numbers
		:param a: First number
		:param b: Second number
		:return: a*b
		"""
		return a * b

	@staticmethod
	def divide(a, b):
		"""
		Divides one number by another number
		:param a: Numerator
		:param b: Denominator
		:return: a/b
		:raises: ValueError if denominator is 0
		"""
		if b == 0:
			raise ValueError
		return a / b

	@staticmethod
	def power(base, exponent):
		"""
		Raises a number to a power based on the exponent
		:param base: Number to raise to a power
		:param exponent: Natural number (int), which power to raise the base to
		:return: base ^ exponent
		"""
		if not isinstance(exponent, int):
			raise ValueError
		if base == 0 and exponent == 0:
			raise ValueError
		return base ** exponent

	@staticmethod
	def root(x, n):
		"""
		Takes the n-th root of a number
		:param x: Number to take n-th root of
		:param n: Order of the root
		:return: n√x
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
		"""
		Take the sine function of x
		:param x: Input in radians
		:return: sin(x)
		"""
		return MathLib.power(-1, i) * MathLib.power(x, 2 * i + 1) / MathLib._fact(2 * i + 1)

	@staticmethod
	@taylor
	def cos(x, i):
		"""
		Take the cosine function of x
		:param x: Input in radians
		:return: cos(x)
		"""
		return MathLib.power(-1, i) * MathLib.power(x, 2 * i) / MathLib._fact(2 * i)

	@staticmethod
	def tan(x):
		"""
		Take the tangent function of x
		:param x: Input in radians
		:return: tan(x)
		"""
		return MathLib.divide(MathLib.sin(x), MathLib.cos(x))

	@staticmethod
	@taylor
	def exp(x, i):
		"""
		Take the exponential function of x
		:param x: Input number
		:return: e^x
		"""
		return MathLib.divide(MathLib.power(x, i), MathLib._fact(i))

	@staticmethod
	@taylor
	def natural_log(x, i):
		"""
		Take the natural logarithm of x
		:param x: Input number
		:return: ln(x)
		"""
		if x <= 0:
			raise ValueError
		return 2 * MathLib.power((x - 1) / (x + 1), 2 * i + 1) / (2 * i + 1)

	@staticmethod
	def log(x):
		"""
		Take the base 10 logarithm of x
		:param x: Input number
		:return: log10(x)
		"""
		return MathLib.natural_log(x) / MathLib.LN10
