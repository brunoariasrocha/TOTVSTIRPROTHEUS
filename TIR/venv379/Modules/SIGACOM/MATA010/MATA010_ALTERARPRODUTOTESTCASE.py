from tir import Webapp
import time
import unittest

class MATA010_ALTERARPRODUTO(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","03/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA010")

	def test_MATA010_ALTERARPRODUTO_001(self):
		self.oHelper.SearchBrowse("000049") #No Produção, são 5 dígitos
		#self.oHelper.SetKey("Enter")
		time.sleep(5)
		self.oHelper.SetButton("Alterar")
		self.oHelper.WaitShow("Atualizacao de Produtos - Alterar", 20)
		self.oHelper.SetValue("B1_DESC","PRODUTO TESTE TIR 3")
		self.oHelper.SetValue("B1_UM","UN")
		self.oHelper.SetValue("B1_XAPRES","")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()