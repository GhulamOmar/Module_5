import unittest
from input_loops import average_input_scores
import unittest.mock as result


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with result.patch('builtins.input', side_effect=[90, 95, 85]):
            self.assertEquals(90, average_input_scores.average(list))

    if __name__ == '__main__':
        unittest.main()
