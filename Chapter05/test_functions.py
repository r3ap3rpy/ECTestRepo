import unittest
from functions import *
class TestFunctions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(4,6),10,"4 + 6 should be equal to 10!")
    def test_diff(self):
        self.assertEqual(diff(6,3),3, "6 - 3 should be equal to 3!")
    def test_multiply(self):
        self.assertEqual(multiply(6,6),36,"6 * 6 should be equal to 36")
if __name__ == '__main__':
    unittest.main()