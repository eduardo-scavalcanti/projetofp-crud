import gerenciador_dados

ARQUIVO_CONSULTAS = "consultas.json"
ARQUIVO_MEDICOS = "medicos.json" 

def relatorio_medicos():
    banco_consultas = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTAS)
    banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICOS)

    for m in banco_medicos:
        consultas = 0
        for c in banco_consultas:
            if m['id'] == c['medicoid']:
                consultas += 1
        print('-' * 6, "RELATÓRIO", '-' * 6)
        print(f"id: {m['id']}")
        print(f"Médico: {m['nome']}")
        print(f"Consultas agendadas: {consultas}")
        print('-' * 23, '\n')

def relatorio_data():
    ...