from tir import Webapp
import unittest

class PrimeiroTesteCase(unittest.TestCase):
    def setUp(self):
        self.test_helper = Webapp()
        self.test_helper.Setup('SIGAFAT', '20/12/2021', '99', '01', '05')
        self.test_helper.Program('MATA030')

    def test_incluir(self):
        self.test_helper.SetButton('Incluir')
        self.test_helper.SetValue('A1_COD', '900009')
        self.test_helper.SetValue('A1_LOJA', '01')
        self.test_helper.SetValue('A1_NOME', 'FABIO CAZARINI')
        self.test_helper.SetButton('Confirmar')

    def tearDown(self):
        self.test_helper.TearDown()