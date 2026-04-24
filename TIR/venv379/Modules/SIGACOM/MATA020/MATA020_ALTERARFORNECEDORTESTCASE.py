from tir import Webapp
import unittest
import time

class MATA020_ALTERARFORNECEDOR(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","08/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA020")

	def test_MATA020_ALTERARFORNECEDOR_001(self):
		
		self.oHelper.SearchBrowse("11067500")
		self.oHelper.SetKey("Enter")
		time.sleep(8)
		self.oHelper.SetButton("Alterar")
		self.oHelper.WaitShow("Fornecedores - Alterar", 20)
		#self.oHelper.SetValue("A2_CGC","492.294.331-52")
		self.oHelper.SetValue("A2_NOME","TEST INTERFACE ROBOT 3")
		self.oHelper.SetValue("A2_NREDUZ","TEST INTERFACE ROBOT 3")
		self.oHelper.SetValue("A2_END","RUA DAS GRACAS, 123")
		self.oHelper.SetValue("A2_BAIRRO","VILA CARLOTA")
		self.oHelper.SetFocus("A2_EST")
		self.oHelper.SetValue("A2_EST","MT")
		self.oHelper.SetValue("A2_COD_MUN","03403")
		self.oHelper.SetValue("A2_CEP","79051-230")
		self.oHelper.SetValue("A2_INSCR","ISENTO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()