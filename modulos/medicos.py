import gerenciador_dados
from . import validacoes

ARQUIVO_MEDICO = "medicos.json" 

def cadastrar_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)
    
    crm_medico = input("CRM (999999/UF): ").replace(" ", "").upper()
    while validacoes.validar_crm(crm_medico) == False:
        crm_medico = input("CRM (999999/UF): ").replace(" ", "").upper()

    for medico in banco_medico:
        if crm_medico == medico['crm']:
            print("ERRO! Já existe um médico cadastrado com esse CRM.")
            return

    nome_medico = input("Nome: ").strip().title()
    while validacoes.validar_nome(nome_medico) == False:
        nome_medico = input("Nome: ").strip().title()

    especialidade_medico = input("Especialidade: ").strip().title()
    while validacoes.validar_especialidade(especialidade_medico) == False:
        especialidade_medico = input("Especialidade: ").strip().title()

    data_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")
    while validacoes.validar_data_nascimento(data_nascimento_medico) == False:
        data_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")

    email_medico = input("E-mail (email@gmail.com): ").replace(" ", "").lower()
    while validacoes.validar_email(email_medico) == False:
        email_medico = input("E-mail (email@gmail.com): ").replace(" ", "")

    numero_medico = input("Telefone (99)99999-9999: ").replace(" ", "")
    while validacoes.validar_numero(numero_medico) == False:
        numero_medico = input("Telefone (99)99999-9999: ").replace(" ", "")

    medico = {}

    if len(banco_medico) == 0:
        medico['id'] = 1
    else:
       medico['id'] = banco_medico[len(banco_medico) - 1]['id'] + 1
    medico['nome'] = nome_medico 
    medico['crm'] = crm_medico
    medico['especialidade'] = especialidade_medico
    medico['data_nascimento'] = data_nascimento_medico
    medico['email'] = email_medico
    medico['numero'] = numero_medico

    banco_medico.append(medico)

    gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)

    print("\n\033[1;32mMédico criado com sucesso.\033[0;0m")


def info_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("Não há médicos cadastrados.")
        return
    else:
        id_busca = input("Digite o id do médico: ").replace(" ", "")
        while validacoes.validar_id(id_busca) == False:
            id_busca = input("Digite o id do médico: ").replace(" ", "")
        
    for medico in banco_medico:
        if medico["id"] == int(id_busca):
            print(f"\nID: {medico['id']}")
            print(f"Nome: {medico['nome']}")
            print(f"CRM: {medico['crm']}")
            print(f"Especialidade: {medico['especialidade']}")
            return
        
    print("Médico não encontrado.")


def alterar_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("Não há médicos cadastrados.")
        return
    else:
        id_alterado = input("Digite o id do médico: ").replace(" ", "")
        while validacoes.validar_id(id_alterado) == False:
            id_alterado = input("Digite o id do médico: ").replace(" ", "")

        for medico in banco_medico:
            if medico["id"] == int(id_alterado):

                novo_nome = input("Nome: ").strip()
                while validacoes.validar_nome(novo_nome) == False:
                    novo_nome = input("Nome: ").strip()

                novo_crm = input("CRM: ").replace(" ", "")
                while validacoes.validar_crm(novo_crm) == False:
                    novo_crm = input("CRM: ").replace(" ", "")

                nova_especialidade = input("Especialidade: ").strip()
                while validacoes.validar_especialidade(nova_especialidade) == False:
                    nova_especialidade = input("Especialidade: ").strip()
                
                medico['nome'] = novo_nome
                medico['crm'] = novo_crm
                medico['especialidade'] = nova_especialidade
                
                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)
                return
            
        print("Médico não encontrado.")


def excluir_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("Não há médicos cadastrados.")
        return
    else:
        id_excluido = input("Digite o id do médico: ").replace(" ", "")
        while validacoes.validar_id(id_excluido) == False:
            id_excluido = input("Digite o id do médico: ").replace(" ", "")

        for medico in banco_medico:
            if medico["id"] == int(id_excluido):

                banco_medico.remove(medico)

                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)
                return
            
        print("Médico não encontrado.")
