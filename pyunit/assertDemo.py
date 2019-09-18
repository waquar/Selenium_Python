
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        b = False
        self.assertTrue(a, "a is not false")
        self.assertFalse(b, 'b is not true')

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a,b,msg = "a is not b")

if __name__ == "__main__":
    unittest.main(verbosity=2)
