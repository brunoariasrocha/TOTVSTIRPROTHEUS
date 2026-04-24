import pyodbc
import msal

# Configurações do Microsoft Entra e SQL Server
tenant_id = "d8cbd03e-a88a-42db-9260-8f2201f516d7"  # Ex.: "yourdomain.onmicrosoft.com"
client_id = "seu_client_id"  # ID do aplicativo registrado no Entra
authority_url = f"https://login.microsoftonline.com/{tenant_id}"
username = "bruno.rocha@agroline.com.br"
server = "agroops.database.windows.net"
database = "axiapool"  # Substitua pelo nome real do seu banco

# Criar aplicação MSAL para autenticação com MFA
app = msal.PublicClientApplication(
    client_id=client_id,
    authority=authority_url
)

# Obter token com MFA (abre janela de navegador para autenticação)
result = app.acquire_token_interactive(scopes=["https://database.windows.net/.default"])
if "access_token" not in result:
    raise Exception("Falha na autenticação: " + result.get("error_description"))

access_token = result["access_token"]

# Conectar ao SQL Server usando o token
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Authentication=ActiveDirectoryPassword;"
    f"UID={username};"
    f"AccessToken={access_token}"
)

try:
    # Estabelecer conexão
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Definir e executar a query
    query = """
    SELECT A1_COD, A1_NOME
    FROM SA1010
    WHERE D_E_L_E_T_ <> '*'
    """
    cursor.execute(query)

    # Obter e exibir resultados
    rows = cursor.fetchall()
    for row in rows:
        print(f"Código: {row.A1_COD}, Nome: {row.A1_NOME}")

except Exception as e:
    print(f"Erro ao conectar ou executar a query: {e}")

finally:
    # Fechar conexão
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()