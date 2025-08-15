import unittest

from PRIMEIROTESTECASE import PrimeiroTesteCase

suite = unittest.TestSuite()
suite.addTest(PrimeiroTesteCase('test_incluir'))
              
runner = unittest.TextTestRunner(verbosity=2)
ruuner.run(suite)