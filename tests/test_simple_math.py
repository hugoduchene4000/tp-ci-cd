import unittest
from math.simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(3, 4), 7)

if __name__ == "__main__":
    unittest.main()