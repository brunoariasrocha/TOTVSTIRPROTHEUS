from tir import Webapp
import unittest

class TESTE2MATA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACOM","21/08/2025","01","01011001","02")

    def test_TESTE2MATA010_001(self):

        self.oHelper.Program("MATA010")
        self.oHelper.SetButton("Incluir")
        self.oHelper.WaitShow("Atualizacao de Produtos - Incluir", 20)

        # --- B1_DESC sem espaço na 1ª posição ---
        self.oHelper.SetFocus("B1_DESC")
        self.oHelper.SetValue(
            "B1_DESC",
            "PRODUTO TESTE TIR",
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
        self.oHelper.SetValue("B1_SEGUM","")
        self.oHelper.SetValue("B1_CONV","0,00")
        self.oHelper.SetKey('Tab')
        self.oHelper.SetValue("B1_PESO","0,00000")
        self.oHelper.SetValue("B1_PESBRU","0,00000")
        self.oHelper.SetValue("B1_PROC","")
        self.oHelper.SetValue("B1_LOJPROC","")
        self.oHelper.SetValue("B1_CONTA","")
        self.oHelper.SetValue("B1_ORIGEM","0")
        self.oHelper.SetValue("B1_CODBAR","0000000000000")
        self.oHelper.SetValue("B1_MSBLQL", "2 - Não")
        self.oHelper.SetButton("Confirmar")
		
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()