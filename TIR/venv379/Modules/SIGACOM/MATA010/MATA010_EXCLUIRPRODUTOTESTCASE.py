from tir import Webapp
import time
import unittest

class MATA010_EXCLUIRPRODUTO(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","05/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA010")
		
	def test_MATA010_EXCLUIRPRODUTO_001(self):

		self.oHelper.SearchBrowse("000049")
		time.sleep(5)
		self.oHelper.SetButton("Outras Ações")
		self.oHelper.ClickMenuPopUpItem("Excluir")
		self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?", 20)
		self.oHelper.SetButton("Confirmar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()