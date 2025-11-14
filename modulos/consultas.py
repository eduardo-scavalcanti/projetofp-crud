from datetime import datetime
import gerenciador_dados
from . import mensagens
from . import validacoes

ARQUIVO_MEDICO = "medicos.json"
ARQUIVO_PACIENTE = "pacientes.json"
ARQUIVO_CONSULTA = "consultas.json"

def cadastrar_consulta():
    banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTE)

    if len(banco_medicos) == 0:
        mensagens.erro("ERRO! Não há médicos cadastrados.")
        return
    elif len(banco_pacientes) == 0:
        mensagens.erro("ERRO! Não há pacientes cadastrados.")

    crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
    while validacoes.validar_crm(crm_medico) == False:
        crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
    
    medico_encontrado = False

    for m in banco_medicos:
        if m['crm'] == crm_medico:
            medico_encontrado = True
            nome_medico = m['nome']

    if not medico_encontrado:
        mensagens.erro("ERRO! Médico não encontrado.")
        return

    cpf_paciente = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
    while validacoes.validar_cpf(cpf_paciente) == False: 
        cpf_paciente = input("CPF (XXXXXXXXXXX): ").replace(" ", "")

    paciente_encontrado = False

    for p in banco_pacientes:
        if p['cpf'] == cpf_paciente:
            paciente_encontrado = True
            nome_paciente = p['nome']

    if not paciente_encontrado:
        mensagens.erro("ERRO! Paciente não encontrado.")
        return

    queixa = input('Queixa: ').strip().capitalize()
    while validacoes.validar_queixa(queixa) == False:
        queixa = input('Queixa: ').strip().capitalize()

    data_consulta = input("Data da consulta (DD/MM/AAAA): ").replace(" ", "")
    while validacoes.validar_data_consulta(data_consulta) == False:
        data_consulta = input("Data da consulta (DD/MM/AAAA): ").replace(" ", "")

    consulta = {}
    
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        consulta['id'] = 1
    else:
        consulta['id'] = banco_consulta[len(banco_consulta) - 1]['id'] + 1

    consulta['medico'] = nome_medico
    consulta['crm'] = crm_medico
    consulta['paciente'] = nome_paciente
    consulta['cpf'] = cpf_paciente
    consulta['queixa'] = queixa
    consulta['data'] = data_consulta

    banco_consulta.append(consulta)

    banco_consulta = gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA, banco_consulta)

    mensagens.sucesso(f"Consulta agendada com sucesso.\nID: {consulta['id']}")


def info_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        mensagens.erro("ERRO! Não há consultas agendadas.")
        return
    else:
        id_busca = input("Digite o ID da consulta que você quer verificar: ").replace(" ", "")
        while validacoes.validar_id(id_busca) == False:
            id_busca = input("Digite o ID da consulta que você quer verificar: ").replace(" ", "")

        for consulta in banco_consulta:
            if consulta['id'] == int(id_busca):
                print(f"ID: {consulta['id']}")
                print(f"Médico: {consulta['medico']}")
                print(f"CRM: {consulta['crm']}")
                print(f"Paciente: {consulta['paciente']}")
                print(f"CPF: {consulta['cpf']}")
                print(f"Queixa: {consulta['queixa']}")
                print(f"Data: {consulta['data']}")
                return
    
    mensagens.erro("ERRO! Consulta não encontrada.")


def alterar_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        mensagens.erro("ERRO! Não há consultas agendadas.")
        return

    id_alterado = input("Digite o ID da consulta que você quer alterar: ").replace(" ", "")
    while validacoes.validar_id(id_alterado) == False:
        id_alterado = input("Digite o ID da consulta que você quer alterar: ").replace(" ", "")
        
    for consulta in banco_consulta:
        if consulta['id'] == int(id_alterado):

            banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

            novo_crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
            while validacoes.validar_crm(novo_crm_medico) == False:
                novo_crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
                
                medico_encontrado = False

                for m in banco_medicos:
                    if m['crm'] == novo_crm_medico:
                        medico_encontrado = True
                        novo_nome_medico = m['nome']                
                
                if medico_encontrado:
                    break
                else:
                    mensagens.erro("ERRO! Médico não encontrado. Tente novamente.")

            banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTE)

            novo_cpf_paciente = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
            while validacoes.validar_cpf(novo_cpf_paciente) == False: 
                novo_cpf_paciente = input("CPF (XXXXXXXXXXX): ").replace(" ", "")

                paciente_encontrado = False

                for p in banco_pacientes:
                    if p['cpf'] == novo_cpf_paciente:
                        paciente_encontrado = True
                        novo_nome_paciente = p['nome']

                if paciente_encontrado:
                    break
                else:
                    mensagens.erro("ERRO! Paciente não encontrado.")

            nova_queixa = input('Queixa: ').strip().capitalize()
            while validacoes.validar_queixa(nova_queixa) == False:
                nova_queixa = input('Queixa: ').strip().capitalize()

            nova_data = input("Data da consulta (DD/MM/AAAA): ").replace(" ", "")
            while validacoes.validar_data_consulta(nova_data) == False:
                nova_data = input("Data da consulta (DD/MM/AAAA): ").replace(" ", "")

            consulta['medico'] = novo_nome_medico
            consulta['crm'] = novo_crm_medico
            consulta['paciente'] = novo_nome_paciente
            consulta['cpf'] = novo_cpf_paciente
            consulta['queixa'] = nova_queixa
            consulta['data'] = nova_data

            gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA, banco_consulta)

            mensagens.sucesso("Consulta alterada com sucesso.")
            return
        
    mensagens.erro("ERRO! Consulta não encontrada.")


def excluir_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        mensagens.erro("ERRO! Não há consultas agendadas.")
        return
    else:
        id_excluido = input("Digite o ID que você quer excluir: ").replace(" ", "")
        while validacoes.validar_id(id_excluido) == False:
            id_excluido = input("Digite o ID que você quer excluir: ").replace(" ", "")

        for consulta in banco_consulta:
            if consulta['id'] == int(id_excluido):

                banco_consulta.remove(consulta)

                banco_consulta = gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA, banco_consulta)

                mensagens.sucesso("Consulta agendada com sucesso.")
                return

        mensagens.erro("ERRO! Consulta não encontrada.")