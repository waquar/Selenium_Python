import unittest

import unittest

class Setup_TearDown(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("@" * 20)
        print("i will run once before all tests")
        print("@"*21)

    def setUp(self):
        print("will run once for each test method")

    def test_methodA(self):
        print("Running from method A")

    def test_methodB(self):
        print("Running from method B")

    def tearDown(self):
        print("i will run after every test method")

    @classmethod
    def tearDownClass(cls):
        print("#" * 20)
        print("i will run once after all tests")
        print("#" * 21)


if __name__ == "__main__":
    unittest.main(verbosity=2)