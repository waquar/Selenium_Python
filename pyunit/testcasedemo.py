import unittest

class TestcaseDemo(unittest.TestCase):

    def setUp(self):
        print("will run once for each test method")

    def test_methodA(self):                               #mandatory to use test before method name
        print("Running from method A")

    def test_methodB(self):
        print("Running from method B")

    def tearDown(self):
        print("i will run after every test method")

if __name__ == "__main__":
    unittest.main(verbosity=2)