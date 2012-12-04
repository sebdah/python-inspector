#!/usr/bin/env python

"""
Test the Inspector
"""

import unittest
import inspector

########################################################
#
#   Inspector test
#
########################################################

def func2():
	insp = inspector.Inspector()
	return insp.inspect()

def func1():
	return func2()

def do_inspect():
	"""
	"""
	return func1()

########################################################
#
#   TEST CASES
#
########################################################


class InspectorTest(unittest.TestCase):
	"""
	Unit tests for the Inspector
	"""
	def testFullInspection(self):
		"""
		Test a simple full inspection
		"""
		cmp = """\
test.py:18 in method func2
	return insp.inspect()test.py:21 in method func1
	return func2()test.py:26 in method do_inspect
	return func1()
"""

		self.assertEqual(
			(''.join(do_inspect()[:3])).strip(),
			cmp.strip())

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(InspectorTest('testFullInspection'))
	unittest.TextTestRunner(verbosity=2).run(suite)
