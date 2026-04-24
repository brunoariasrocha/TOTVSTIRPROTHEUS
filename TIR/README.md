# 📌 Instalação e Configuração do TOTVS TIR Record Protheus 1.0.0 no VSCode

Este guia resume os passos necessários para configurar o **TOTVS TIR Record** no **Visual Studio Code**, com suporte ao **Python 3.7.9** e demais bibliotecas essenciais.

---

## 🔹 1. Requisitos Iniciais

### 🦊 Mozilla Firefox
- Necessário para compatibilidade com o **TIR Record**.  
- Instalar a extensão **TIR RECORD**:
  - Gera automaticamente arquivos **CASE** (casos de teste individuais) e **SUITE** (coleção de testes).  
  - Útil para automação de cliques, cadastros, inclusões, etc.  
- Configurar a extensão em `Setup`.

📖 [Documentação Oficial TIR Record](https://totvs.github.io/tir-docs/tir-record/ComoUsar/)

---

## 🔹 2. Visual Studio Code
- Baixar a versão mais recente: [VSCode Download](https://code.visualstudio.com/download)
- Extensões necessárias:
  - **Python**  
  - **TOTVS Developer Studio for VSCode** (para conexão com ambiente Protheus)

⚙️ Configurar TOTVS Developer Studio:
- Nome do servidor: livre escolha  
- Endereço/IP: fornecido pelo responsável técnico  
- Porta: a mesma do **Debug/WebAgent** (exemplo: `2203`)

---

## 🔹 3. Python

> ⚠️ **Atenção:** O TIR funciona melhor com o **Python 3.7.9**.

- Instale a **versão mais recente** do Python (com PATH habilitado).  
- Instale também a versão **3.7.9** (sem adicionar ao PATH).  
- Download: [Python 3.7.9](https://www.python.org/downloads/release/python-379/)

---

## 🔹 4. Configuração Inicial

### 📂 Estrutura de Pastas

```bash

Workspace/
  ├── venv379/
  └── rotinas/

---

5. Criar ambiente virtual</span
py -3.7 -m venv venv379

---

6. Ativar ambiente
.\venv379\Scripts\Activate

---

7. Instalação de Bibliotecas
pip install pandas==1.0.1
pip install debugpy==1.6.6
pip install numpy==1.21.6
pip install selenium==3.141.0
pip install tir-framework==1.20.30
pip install opencv-python-headless==4.5.5.64

---

8. config.json

{
  "Url": "https://servidor:2203/webapp/",            
  "Browser": "FireFox",
  "Environment": "HMG",
  "Language": "pt-br",
  "POUILogin": true,
  "User": "SEU.LOGIN",
  "Password": "SUA.SENHA",
  "CSVPath": "CAMINHO_CSV",
  "DebugLog": true,
  "TimeOut": 90,
  "Headless": false
}

---

9. 📌 launch.json

{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Rodar sem debug - venv379",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/venv379/MATA010/teste.py",
      "console": "integratedTerminal",
      "python": "${workspaceFolder}/venv379/Scripts/python.exe",
      "noDebug": true
    }
  ]
}

---

📌 Arquivos .py

Gerados pelo TIR Record (Firefox) → exportados como CASE e SUITE.

Devem ser movidos para dentro da pasta do ambiente virtual.

🔹 10. Considerações Finais

Cada máquina pode apresentar variações → ajustes podem ser necessários.

Requer noções básicas de programação Python.

Repositórios e docs úteis:

TOTVS TIR GitHub

Documentação TIR

Repositório Bruno Arias Rocha