import json
import os

CAMINHO_ABSOLUTO_DADOS = os.path.join(
    os.path.dirname(__file__),
    "dados")

def carregar_dados(nome_arquivo):
    if not os.path.exists(CAMINHO_ABSOLUTO_DADOS):
        os.mkdir("dados")

    caminho_completo = os.path.join(CAMINHO_ABSOLUTO_DADOS, nome_arquivo)
    
    if os.path.exists(caminho_completo):
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    else:
        return []
    

def salvar_dados(nome_arquivo, tabela):
    caminho_completo = os.path.join(CAMINHO_ABSOLUTO_DADOS, nome_arquivo)

    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        json.dump(tabela, arquivo, ensure_ascii=False, indent=4)