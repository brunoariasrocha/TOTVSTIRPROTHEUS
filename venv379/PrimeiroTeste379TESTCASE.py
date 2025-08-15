from tir import Webapp
import time

# Inicializa o TIR
oHelper = Webapp()

# Setup básico: SIGAFAT, data, filial e ambiente
#oHelper.Setup("SIGAFAT", "11/04/2019", "T1", "D MG 01")

# Abre o navegador com a URL do JSON
oHelper.Start()  # Start já usa a URL e Browser do JSON

# Espera um pouco pra ver a página
time.sleep(30)

# Fecha o navegador
oHelper.TearDown()
