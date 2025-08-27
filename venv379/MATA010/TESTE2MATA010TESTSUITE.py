import unittest
from TESTE2MATA010TESTCASE import TESTE2MATA010

suite = unittest.TestSuite()
suite.addTest(TESTE2MATA010('test_TESTE2MATA010_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)