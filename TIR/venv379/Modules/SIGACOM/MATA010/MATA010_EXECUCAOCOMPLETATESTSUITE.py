import unittest
from MATA010_EXECUCAOCOMPLETATESTCASE import MATA010_EXECUCAOCOMPLETA

suite = unittest.TestSuite()
suite.addTest(MATA010_EXECUCAOCOMPLETA('test_MATA010_EXECUCAOCOMPLETA_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)