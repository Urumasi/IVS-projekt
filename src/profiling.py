"""Math library profiling module

Calculates standard deviation from the numbers provided to stdin and
measures the speed of all function calls during the calculation.
"""

# File: profiling.py
# Author: OkayChamps, Petr Salaba (xsalab00), FIT BUT
# Date: 2020-Apr-29

import cProfile
import pstats
from stddev import read_and_calculate


def f8(x):
	"""More precise time measurement for cProfile.
	This function is used for formatting elapsed time in the profiling output table.

	Args:
		x (float): Elapsed time in seconds to format.

	Returns:
		string: Formatted time, should be 8 characters long.
	"""
	if x > 10:  # s
		return "%7.1fs"
	if x > 0.01:  # ms
		return "%6.1fms" % (x * 1e3)
	return "%6.1fµs" % (x * 1e6)  # µs otherwise


pstats.f8 = f8

cProfile.run('print(read_and_calculate())')
