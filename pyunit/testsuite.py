import unittest

#imported all the files
from pyunit.setup_teardownCLASS import Setup_TearDown
from pyunit.testcasedemo import TestcaseDemo
from pyunit.assertDemo import AssertDemo

#loaded all the class in respective variable
tc1 = unittest.TestLoader().loadTestsFromTestCase(Setup_TearDown)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestcaseDemo)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)

#running the suite
sampletest = unittest.TestSuite([tc1,tc2,tc3])
unittest.TextTestRunner(verbosity=2).run(sampletest)
