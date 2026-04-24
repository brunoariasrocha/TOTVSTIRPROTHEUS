# language: pt

Funcionalidade: Filtro de comprador na rotina Eliminação de Resíduos

  Cenário: Filtrar pedidos por comprador
    Dado que o usuário está logado no Protheus e está na rotina "Eliminação de Resíduos (MATA235)"
    Quando eu checar o código de usuário que está no campo e na mensagem de alerta
    Então a rotina deverá executar o processo normalmente