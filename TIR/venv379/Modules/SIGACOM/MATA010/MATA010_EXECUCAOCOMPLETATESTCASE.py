from tir import Webapp
import time
import unittest

		#ESTE TESTCASE TEM POR FINALIDADE CRIAR, ALTERAR E EXCLUIR O MESMO PRODUTO, SEM PRECISAR FECHAR O PROTHEUS, OU SEJA, TUDO NA MESMA TELA.
class MATA010_EXECUCAOCOMPLETA(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM","05/09/2025","01","01011001","02")
		inst.oHelper.Program("MATA010")

	def test_MATA010_EXECUCAOCOMPLETA_001(self):

	#INCLUSÃO DO PRODUTO:
		self.oHelper.SetButton("Incluir")
		self.oHelper.WaitShow("Atualizacao de Produtos - Incluir", 20)

        # --- B1_DESC sem espaço na 1ª posição ---
		self.oHelper.SetFocus("B1_DESC")
		self.oHelper.SetValue(
            "B1_DESC",
            "PRODUTO TESTE TIR 3",
            name_attr=True,
            check_value=False
        )
		self.oHelper.SetValue("B1_UM","UN")
		self.oHelper.SetValue("B1_XMARCA","0412")
		self.oHelper.SetValue("B1_XCAT1","07")
		self.oHelper.SetValue("B1_XCAT2","28")
		self.oHelper.SetValue("B1_XGRP1","000")
		self.oHelper.SetValue("B1_XGRP2","00")
		self.oHelper.SetValue("B1_GRUPO","0728")
		self.oHelper.SetValue("B1_XPERREA","0,00")
		self.oHelper.SetValue("B1_TIPO","ME")
		self.oHelper.SetValue("B1_LOCPAD","01")
		self.oHelper.SetValue("B1_CONV","0,00")
		self.oHelper.SetKey('Tab')
		self.oHelper.SetValue("B1_PESO","0,00000")
		self.oHelper.SetValue("B1_PESBRU","0,00000")
		self.oHelper.SetValue("B1_ORIGEM","0")
		self.oHelper.SetValue("B1_CODBAR","0000000000000")
		self.oHelper.SetValue("B1_MSBLQL", "2 - Não")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.WaitShow("Registro inserido com sucesso", 1000)
		self.oHelper.SetButton("Fechar")

		#ALTERAÇÃO DO PRODUTO
		time.sleep(5)
		self.oHelper.SetButton("Alterar")
		self.oHelper.WaitShow("Atualizacao de Produtos - Alterar", 20)
		self.oHelper.SetValue("B1_DESC","PRODUTO TESTE TIR 4")
		self.oHelper.SetValue("B1_UM","UN")
		self.oHelper.SetValue("B1_XAPRES","")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		time.sleep(10)

		#EXCLUSÃO DO PRODUTO
		self.oHelper.SetButton("Outras Ações")
		self.oHelper.ClickMenuPopUpItem("Excluir")
		self.oHelper.WaitShow("Tem certeza que deseja excluir o item abaixo?", 20)
		self.oHelper.SetButton("Confirmar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()