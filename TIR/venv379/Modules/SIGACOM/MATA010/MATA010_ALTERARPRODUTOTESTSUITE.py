import unittest
from MATA010_ALTERARPRODUTOTESTCASE import MATA010_ALTERARPRODUTO

suite = unittest.TestSuite()
suite.addTest(MATA010_ALTERARPRODUTO('test_MATA010_ALTERARPRODUTO_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)