from tir import Webapp
import unittest

class MATA020_INCLUIRFORNECEDOR(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","08/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA020")

	def test_MATA020_INCLUIRFORNECEDOR_001(self):
		
	 #INCLUIR FORNECEDOR
		self.oHelper.SetButton("Incluir")
		self.oHelper.WaitShow("Fornecedores - Incluir", 20)
		self.oHelper.SetValue("A2_CGC","492.294.331-52")
		self.oHelper.SetValue("A2_NOME","TEST INTERFACE ROBOT")
		self.oHelper.SetValue("A2_NREDUZ","TEST INTERFACE ROBOT")
		self.oHelper.SetValue("A2_END","RUA DAS GRACAS, 621")
		self.oHelper.SetValue("A2_BAIRRO","CENTRO")
		self.oHelper.SetValue("A2_EST","MS")
		self.oHelper.SetValue("A2_COD_MUN","02704")
		self.oHelper.SetValue("A2_CEP","79051-550")
		self.oHelper.SetValue("A2_INSCR","ISENTO")
		self.oHelper.SetValue("A2_EMAIL","TESTETIR@OUTLOOK.COM")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

	 #ALTERAR FORNECEDOR
		time.sleep(10)
		self.oHelper.SetButton("Alterar")
		self.oHelper.WaitShow("Fornecedores - Alterar", 20)
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

	 #EXCLUIR FORNECEDOR
		self.oHelper.SetButton("Outras Ações"),
		self.oHelper.ClickMenuPopUpItem("Excluir")
		self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?", 20)
		self.oHelper.SetButton("Confirmar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()