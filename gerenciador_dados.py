import os
import json

CAMINHOABSOLUTO_DADOS = os.path.join(
    os.path.dirname(__file__),
    "dados")


def carregar_dados(nomearquivo):
    caminho_completo = os.path.join(CAMINHOABSOLUTO_DADOS, nomearquivo)
    
    with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados


def salvar_dados(nomearquivo, dicionario):
    caminho_completo = os.path.join(CAMINHOABSOLUTO_DADOS, nomearquivo)
    tabela = carregar_dados(nomearquivo)
    
    tabela.append(dicionario)
    
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        json.dump(tabela, arquivo, ensure_ascii=False, indent=4)