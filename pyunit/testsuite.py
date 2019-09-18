import unittest
from pyunit.setup_teardownCLASS import Setup_TearDown
from pyunit.testcasedemo import TestcaseDemo
from pyunit.assertDemo import AssertDemo

tc1 = unittest.TestLoader().loadTestsFromTestCase(Setup_TearDown)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestcaseDemo)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)

sampletest = unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner(verbosity=2).run(sampletest)