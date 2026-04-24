from behave import given, when, then
from tir import Webapp

@given(u'que o usuário está logado no Protheus e está na rotina "Eliminação de Resíduos (MATA235)"')
def step_impl(context):
    context.oHelper = Webapp()
    context.oHelper.Setup("SIGACOM", "17/10/2025", "01", "01011001", "02")
    context.oHelper.SetLateralMenu("Atualizações > Pedidos > Eliminar Resíduos")

@when('eu checar o código de usuário que está no campo e na mensagem de alerta')
def step_impl(context):

    context.oHelper.WaitShow("Elim. de resíduos dos Pedidos de Compras", 5)
    context.oHelper.SetButton("Executar")

    # -- Início do verifica se o campo "Código Usuário" contém o login atual
    usuario_campo = context.oHelper.GetValue("MV_PAR09")
    login_atual = "000171"
    context.oHelper.AssertTrue(usuario_campo == login_atual, f"O campo 'Código Usuário' deve estar preenchido com o login atual '{login_atual}', mas encontrou '{usuario_campo}'")
    # -- Fim do verifica se o campo "Código Usuário" contém o login atual

    context.oHelper.SetButton("OK")

    #Verifica se tem o código também imputado na mensagem de confirmação

    mensagem = context.oHelper.WaitShow("Eliminação de Resíduos", 5)

    context.oHelper.AssertTrue(
        "Eliminação de Resíduos" in mensagem and login_atual in mensagem, f"""A mensagem esperada não contém o texto 'Eliminação de Resíduos' e/ou o código '{login_atual}'.
        Mensagem exibida: {mensagem}"""
    )

    context.oHelper.SetButton("Sim")
    

@then('a rotina deverá executar o processo normalmente')
def step_impl(context):
    
    mensagem = context.oHelper.WaitShow("Elim. de Resíduos dos Pedidos de Compras", 5)
    if mensagem:
            raise Exception(f"A mensagem inesperada foi exibida: {mensagem}")