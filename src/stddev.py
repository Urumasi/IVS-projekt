"""Standard deviation calculator

Takes numbers from stdin and outputs the standard deviation of the given data set.
"""

# File: profiling.py
# Author: OkayChamps, Petr Salaba (xsalab00), FIT BUT
# Date: 2020-Apr-30

from mathlib import MathLib
from functools import reduce
from sys import stdin, stderr


def calculate_standard_deviation(values):
	"""Calculates standard deviation.

	Args:
		values (list): Data set to use in the calculation.

	Returns:
		float: Standard deviation of the data set.
	"""
	n = len(values)
	s = MathLib.root(
		MathLib.divide(MathLib.subtract(
			reduce(MathLib.add, map(lambda a: MathLib.power(a, 2), values)),
			MathLib.multiply(n, MathLib.power(MathLib.divide(reduce(MathLib.add, values), n), 2))
		), MathLib.subtract(n, 1)), 2)
	return s


def read_and_calculate():
	"""Reads values from stdin and calculates standard deviation.

	Returns:
		float: Standard deviation of the data set read through stdin.
	"""
	numbers = list()
	for line in stdin:
		try:
			line_numbers = list(map(float, line.split()))
			numbers += line_numbers
		except ValueError:
			print("Attempted to parse a number with an invalid format.\n", file=stderr)
			exit(1)

	if len(numbers) <= 1:
		print("Standard deviation can't be calculated or makes no sense for 1 or 0 numbers.\n", file=stderr)
		exit(1)

	return calculate_standard_deviation(numbers)


if __name__ == '__main__':
	print(read_and_calculate())
