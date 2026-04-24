import unittest
from MATA020_EXCLUIRFORNECEDORTESTCASE import MATA020_EXCLUIRFORNECEDOR

suite = unittest.TestSuite()
suite.addTest(MATA020_EXCLUIRFORNECEDOR('test_MATA020_EXCLUIRFORNECEDOR_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)