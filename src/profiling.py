"""Math library profiling module

Calculates standard deviation from the numbers provided to stdin and
measures the speed of all function calls during the calculation.
"""

# File: profiling.py
# Author: OkayChamps, Petr Salaba (xsalab00), FIT BUT
# Date: 2020-Apr-29

from sys import stdin, stderr
from functools import reduce
import cProfile
import pstats

from mathlib import MathLib

__package__ = "calcchamp"


# More precise time measurement for cProfile
def f8(x):
	if x > 10:  # s
		return "%7.1fs"
	if x > 0.01:  # ms
		return "%6.1fms" % (x * 1e3)
	return "%6.1fµs" % (x * 1e6)  # µs otherwise


pstats.f8 = f8


def calculate_standard_deviation(values):
	n = len(values)
	s = MathLib.root(
		MathLib.divide(MathLib.subtract(
			reduce(MathLib.add, map(lambda a: MathLib.power(a, 2), values)),
			MathLib.multiply(n, MathLib.power(MathLib.divide(reduce(MathLib.add, values), n), 2))
		), MathLib.subtract(n, 1)), 2)
	return s


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

cProfile.run('print(calculate_standard_deviation(numbers))')
