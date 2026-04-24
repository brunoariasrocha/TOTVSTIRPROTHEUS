import unittest
from MATA020_ALTERARFORNECEDORTESTCASE import MATA020_ALTERARFORNECEDOR

suite = unittest.TestSuite()
suite.addTest(MATA020_ALTERARFORNECEDOR('test_MATA020_ALTERARFORNECEDOR_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)