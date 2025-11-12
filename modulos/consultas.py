from datetime import datetime
from .. import gerenciador_dados

ARQUIVO_MEDICO = "medicos.json"
ARQUIVO_PACIENTE = "pacientes.json"
ARQUIVO_CONSULTA = "consultas.json"

def cadastrar_consulta():
    banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTE)

    if len(banco_medicos) == 0:
        print("Não há médicos cadastrados.")
        return
    elif len(banco_pacientes) == 0:
        print("Não há pacientes cadastrados.")

    crm_medico = input("CRM do médico (apenas números): ").strip()
    while (crm_medico.isdigit() == False):
        print("INVÁLIDO. Insira apenas números.")
        crm_medico = input("CRM do médico (apenas números): ").strip()
    
    medico_encontrado = False

    for m in banco_medicos:
        if m['crm'] == crm_medico:
            medico_encontrado = True
            nome_medico = m['nome']

    if not medico_encontrado:
        print("Médico não encontrado.")
        return

    cpf_paciente = input("CPF do paciente (apenas números): ").strip()
    while (cpf_paciente.isdigit() == False or len(cpf_paciente) != 11):
        print("CPF INVÁLIDO! Insira apenas números e verifique novamente.")
        cpf_paciente = input("CPF do paciente (apenas números): ").strip()

    paciente_encontrado = False

    for p in banco_pacientes:
        if p['cpf'] == cpf_paciente:
            paciente_encontrado = True
            nome_paciente = p['nome']

    if not paciente_encontrado:
        print("Paciente não encontrado.")
        return

    hoje = datetime.now().date()

    while True:
        data_consulta = input('Digite a data da consulta (DD/MM/AAAA): ').strip()

        try:
            data_datetime = datetime.strptime(data_consulta, "%d/%m/%Y").date()

            if data_datetime >= hoje:
                break
            else:
                print("Erro: A data deve ser hoje ou uma data futura. Tente novamente.")

        except ValueError:
            print("Erro: Formato de data inválido ou data não existe (ex: 30 de Fev). Use DD/MM/AAAA.")

    queixa = input('Queixa do paciente: ').strip()
    while queixa == "":
        print('O campo "queixa" não pode ficar vazio. Tente novamente.')
        queixa = input('Queixa do paciente: ').strip()

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


def info_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        print("Não há consultas agendadas.")
        return
    else:
        id = input("Digite o ID da consulta que você quer verificar: ").strip()
        while(id.isdigit() == False):
            print("INVÁLIDO. Insira um ID válido (apenas números)")
            id = input("Digite o ID da consulta que você quer verificar: ").strip()
        id = int(id)

        for consulta in banco_consulta:
            if consulta["id"] == id:
                print(f"ID: {consulta['id']}")
                print(f"Médico: {consulta['medico']}")
                print(f"CRM: {consulta['crm']}")
                print(f"Paciente: {consulta['paciente']}")
                print(f"CPF: {consulta['cpf']}")
                print(f"Queixa: {consulta['queixa']}")
                print(f"Data: {consulta['data']}")
                return
    
    print("Consulta não encontrada.")


def alterar_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        print("Não há consultas agendadas.")
        return

    id_alterado = input("Digite o ID da consulta que você quer alterar: ")
    while(id_alterado.isdigit() == False):
        print("INVÁLIDO. Insira um ID válido (apenas números)")
        id_alterado = input("Digite o ID do médico que você quer alterar: ")
    id_alterado = int(id_alterado)

    for consulta in banco_consulta:
        if consulta["id"] == id_alterado:

            banco_medicos = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

            while True:
                crm_medico = input("CRM do médico (apenas números): ").strip()
                while (crm_medico.isdigit() == False):
                    print("INVÁLIDO. Insira apenas números.")
                    crm_medico = input("CRM do médico (apenas números): ").strip()
                
                medico_encontrado = False

                for m in banco_medicos:
                    if m['crm'] == crm_medico:
                        medico_encontrado = True
                        novo_medico = m['nome']                
                
                if medico_encontrado:
                    break
                else:
                    print("Médico não encontrado. Tente novamente.")

            banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTE)

            while True:
                cpf_paciente = input("CPF do paciente (apenas números): ").strip()
                while (cpf_paciente.isdigit() == False or len(cpf_paciente) != 11):
                    print("CPF INVÁLIDO! Insira apenas números e verifique novamente.")
                    cpf_paciente = input("CPF do paciente (apenas números): ").strip()

                paciente_encontrado = False

                for p in banco_pacientes:
                    if p['cpf'] == cpf_paciente:
                        paciente_encontrado = True
                        novo_paciente = p['nome']

                if paciente_encontrado:
                    break
                else:
                    print("Paciente não encontrado.")

            hoje = datetime.now().date()

            while True:
                nova_data = input('Digite a data da consulta (DD/MM/AAAA): ').strip()

                try:
                    data_datetime = datetime.strptime(nova_data, "%d/%m/%Y").date()

                    if data_datetime >= hoje:
                        break
                    else:
                        print("Erro: A data deve ser hoje ou uma data futura. Tente novamente.")

                except ValueError:
                    print("Erro: Formato de data inválido ou data não existe (ex: 30 de Fev). Use DD/MM/AAAA.")
            
            nova_queixa = input('Queixa do paciente: ').strip()
            while nova_queixa == "":
                print('O campo "queixa" não pode ficar vazio. Tente novamente.')
                nova_queixa = input('Queixa do paciente: ').strip()

            consulta['medico'] = novo_medico
            consulta['crm'] = crm_medico
            consulta['paciente'] = novo_paciente
            consulta['cpf'] = cpf_paciente
            consulta['data'] = nova_data
            consulta['queixa'] = nova_queixa

            gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA, banco_consulta)
            return
        
    print("Consulta não encontrada.")


def excluir_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)

    if len(banco_consulta) == 0:
        print("Não há consultas agendadas.")
        return
    else:
        id_excluido = input("Digite o ID que você quer excluir: ").strip()
        while id_excluido == "":
            print("Campo vazio. Tente novamente!")
            id_excluido = input("Digite o ID que você quer excluir: ").strip()
        while(id_excluido.isdigit() == False):
            print("INVÁLIDO. Insira um ID (apenas números)")
            id_excluido = input("Digite o ID que você quer excluir: ").strip()
        id_excluido = int(id_excluido)

        for consulta in banco_consulta:
            if(consulta["id"] == id_excluido):
                banco_consulta.remove(consulta)

                banco_consulta = gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA, banco_consulta)
                return

        print("Consulta não encontrada.")