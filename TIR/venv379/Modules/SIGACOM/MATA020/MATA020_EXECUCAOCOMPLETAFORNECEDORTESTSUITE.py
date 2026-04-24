import unittest
from MATA020_INCLUIRFORNECEDORTESTCASE import MATA020_INCLUIRFORNECEDOR

suite = unittest.TestSuite()
suite.addTest(MATA020_INCLUIRFORNECEDOR('test_MATA020_INCLUIRFORNECEDOR_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)