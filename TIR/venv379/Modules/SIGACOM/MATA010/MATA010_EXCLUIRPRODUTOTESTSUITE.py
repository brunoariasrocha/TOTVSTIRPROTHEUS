import unittest
from MATA010_EXCLUIRPRODUTOTESTCASE import MATA010_EXCLUIRPRODUTO

suite = unittest.TestSuite()
suite.addTest(MATA010_EXCLUIRPRODUTO('test_MATA010_EXCLUIRPRODUTO_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)