"""
This a tet file for input_loops import.py
"""
import unittest
from input_loops import average_input_scores
import unittest.mock as result


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with result.patch('builtins.input', side_effect=[44, 60, 88]):
            self.assertRaises(Exception)

    if __name__ == '__main__':
        unittest.main()
