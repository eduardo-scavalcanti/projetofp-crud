import gerenciador_dados
from . import mensagens

ARQUIVO_MEDICOS = "medicos.json"
ARQUIVO_PACIENTES = "pacientes.json"
ARQUIVO_CONSULTAS = "consultas.json"

def relatorio_medicos():
    banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICOS)

    if len(banco_medicos) == 0:
        mensagens.erro("ERRO! Não há médicos cadastrados.")
        return
    
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        mensagens.erro("ERRO! Não há pacientes cadastrados.")
        return
    
    banco_consultas = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTAS)

    if len(banco_consultas) == 0:
        mensagens.erro("ERRO! Não há consultas agendadas.")
        return
    
    for m in banco_medicos:
        consultas = 0
        for c in banco_consultas:
            if m['crm'] == c['crm']:
                consultas += 1
        mensagens.info(f"ID: {m['id']}")
        mensagens.info(f"Médico: {m['nome']}")
        mensagens.info(f"CRM: {m['crm']}")
        mensagens.info(f"Consultas agendadas: {consultas}\n")
        

def relatorio_data():
    banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICOS)

    if len(banco_medicos) == 0:
        mensagens.erro("ERRO! Não há médicos cadastrados.")
        return
    
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        mensagens.erro("ERRO! Não há pacientes cadastrados.")
        return
    
    banco_consultas = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTAS)

    if len(banco_consultas) == 0:
        mensagens.erro("ERRO! Não há consultas agendadas.")
        return

    datas_consultas = set()

    for c in banco_consultas:
        datas_consultas.add(c['data'])

    datas = list(datas_consultas)
    datas.sort()

    for d in datas:
        consultas = 0
        for c in banco_consultas:
            if d == c['data']:
                consultas += 1
        mensagens.info(f"Data: {d}")
        mensagens.info(f"Consultas agendadas: {consultas}\n")