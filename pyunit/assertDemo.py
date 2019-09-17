
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        b = False
        self.assertTrue(a, "a is not false")
        self.assertFalse(b, 'b is not true')

if __name__ == "__main__":
    unittest.main(verbosity=2)
