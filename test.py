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

def func2(*args, **kwargs):
    """
    Example method
    """
    return inspector.trace(*args, **kwargs)

def func1(*args, **kwargs):
    """
    Example method
    """
    return func2(*args, **kwargs)

def do_inspect(*args, **kwargs):
    """
    Call this function to test
    """
    return func1(*args, **kwargs)

########################################################
#
#   TEST CASES
#
########################################################


class InspectorTest(unittest.TestCase):
    """
    Unit tests for the Inspector
    """
    def test_full_trace(self):
        """
        Test a simple full trace
        """
        expected = """\
test.py:26 in method func1
\treturn func2(*args, **kwargs)test.py:32 in method do_inspect
\treturn func1(*args, **kwargs)test.py:57 in method test_full_trace
\t(''.join(do_inspect()[:3])).strip(),
"""

        self.assertEqual(
            (''.join(do_inspect()[:3])).strip(),
            expected.strip())

    def test_trace_with_depth(self):
        """
        Test a simple trace with a limited depth
        """
        expected = """\
test.py:26 in method func1
\treturn func2(*args, **kwargs)
"""

        self.assertEqual(
            (''.join(do_inspect(depth=1)[:3])).strip(),
            expected.strip())

    def test_trace_with_one_line_log(self):
        """
        Test a simple trace with a limited depth and one line response
        """
        expected = """\
test.py:26 in method func1: \treturn func2(*args, **kwargs)
"""

        self.assertEqual(
            (''.join(do_inspect(depth=1, one_line_response=True)[:3])).strip(),
            expected.strip())

if __name__ == '__main__':
    SUITE = unittest.TestSuite()
    SUITE.addTest(InspectorTest('test_full_trace'))
    SUITE.addTest(InspectorTest('test_trace_with_depth'))
    SUITE.addTest(InspectorTest('test_trace_with_one_line_log'))
    unittest.TextTestRunner(verbosity=2).run(SUITE)
