from tir import Webapp

# Inicializa a conexão com o Protheus
# Altere o ambiente, usuário, senha e endereço do servidor conforme seu Protheus
app = Webapp(
    server="https://lineagroprodutos143570.protheus.cloudtotvs.com.br:2203/webapp",   # URL do Protheus Web
    company='01',                     # Código da empresa
    user='BRUNO.ROCHA',                     # Usuário
    password='123',                  # Senha
    environment='CG7XJ1_HMG'               # Ambiente
)

# Abrir o módulo de exemplo (por exemplo, SIGAFAT)
app.SetModule('SIGAFAT')

# Teste: abrir uma tela de pedidos
app.WaitShow('Pedidos de Venda')  # Espera a tela abrir

# Fecha o Protheus
app.Close()