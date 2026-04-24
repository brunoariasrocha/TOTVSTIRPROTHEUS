from tir import Webapp
import unittest
import time

class MATA020_EXCLUIRFORNECEDOR(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","08/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA020")

	def test_MATA020_EXCLUIRFORNECEDOR_001(self):
		
		self.oHelper.SearchBrowse("11067500")
		self.oHelper.SetKey("Enter")
		time.sleep(8)
		self.oHelper.SetButton("Outras Ações"),
		self.oHelper.ClickMenuPopUpItem("Excluir")
		self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?", 20)
		self.oHelper.SetButton("Confirmar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()