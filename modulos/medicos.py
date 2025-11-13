import gerenciador_dados
from . import validacoes

ARQUIVO_MEDICO = "medicos.json" 

def cadastrar_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)
    
    crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
    while validacoes.validar_crm(crm_medico) == False:
        crm_medico = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()

    for medico in banco_medico:
        if crm_medico == medico['crm']:
            print("ERRO! Já existe um médico cadastrado com esse CRM.")
            return

    nome_medico = input("Nome: ").strip().title()
    while validacoes.validar_nome(nome_medico) == False:
        nome_medico = input("Nome: ").strip().title()

    sexo_medico = input("Sexo (M/F): ").replace(" ", "").upper()
    while validacoes.validar_sexo(sexo_medico) == False:
        sexo_medico = input("Sexo (M/F): ").replace(" ", "").upper()

    especialidade_medico = input("Especialidade: ").strip().title()
    while validacoes.validar_especialidade(especialidade_medico) == False:
        especialidade_medico = input("Especialidade: ").strip().title()

    data_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")
    while validacoes.validar_data_nascimento(data_nascimento_medico) == False:
        data_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")

    email_medico = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()
    while validacoes.validar_email(email_medico) == False:
        email_medico = input("E-mail: ").replace(" ", "").lower()

    numero_medico = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
    while validacoes.validar_numero(numero_medico) == False:
        numero_medico = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")

    medico = {}

    if len(banco_medico) == 0:
        medico['id'] = 1
    else:
       medico['id'] = banco_medico[len(banco_medico) - 1]['id'] + 1
    medico['crm'] = crm_medico
    medico['nome'] = nome_medico
    medico['sexo'] = sexo_medico
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
        print("ERRO! Não há médicos cadastrados.")
        return
    else:
        crm_busca = input("Digite o CRM do médico que você deseja verificar (XXXXXX/UF): ").replace(" ", "").upper()
        while validacoes.validar_crm(crm_busca) == False:
            crm_busca = input("Digite o CRM do médico que você deseja verificar (XXXXXX/UF): ").replace(" ", "").upper()
        
    for medico in banco_medico:
        if medico['crm'] == int(crm_busca):
            print(f"\nID: {medico['id']}")
            print(f"CRM: {medico['crm']}")
            print(f"Nome: {medico['nome']}")
            print(f"Sexo: {medico['sexo']}")
            print(f"Especialidade: {medico['especialidade']}")
            print(f"Data de nascimento: {medico['data_nascimento']}")
            print(f"E-mail: {medico['email']}")
            print(f"Celular: {medico['numero']}")
            return
        
    print("ERRO! Médico não encontrado.")


def alterar_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("ERRO! Não há médicos cadastrados.")
        return
    else:
        crm_alterado = input("Digite o CRM do médico que você deseja alterar (XXXXXX/UF): ").replace(" ", "").upper()
        while validacoes.validar_crm(crm_alterado) == False:
            crm_alterado = input("Digite o CRM do médico que você deseja alterar (XXXXXX/UF): ").replace(" ", "").upper()

        for medico in banco_medico:
            if medico['crm'] == crm_alterado:

                novo_crm = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()
                while validacoes.validar_crm(novo_crm) == False:
                    novo_crm = input("CRM (XXXXXX/UF): ").replace(" ", "").upper()

                    for m in banco_medico:
                        if novo_crm == m['crm']:
                            print("ERRO! Já existe um médico cadastrado com esse CRM.")
                            return False

                novo_nome = input("Nome: ").strip().title()
                while validacoes.validar_nome(novo_nome) == False:
                    novo_nome = input("Nome: ").strip().title()

                novo_sexo = input("Sexo (M/F): ").replace(" ", "").upper()
                while validacoes.validar_sexo(novo_sexo) == False:
                    novo_sexo = input("Sexo (M/F): ").replace(" ", "").upper()

                nova_especialidade = input("Especialidade: ").strip().title()
                while validacoes.validar_especialidade(nova_especialidade) == False:
                    nova_especialidade = input("Especialidade: ").strip().title()

                nova_data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")
                while validacoes.validar_data_nascimento(nova_data_nascimento) == False:
                    nova_data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")

                novo_email = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()
                while validacoes.validar_email(novo_email) == False:
                    novo_email = input("E-mail: ").replace(" ", "").lower()

                novo_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
                while validacoes.validar_numero(novo_numero) == False:
                    novo_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
                
                medico = {}

                medico['crm'] = novo_crm
                medico['nome'] = novo_nome
                medico['sexo'] = novo_sexo
                medico['especialidade'] = nova_especialidade
                medico['data_nascimento'] = nova_data_nascimento
                medico['email'] = novo_email
                medico['numero'] = novo_numero
                
                banco_medico.append(medico)

                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)
                return
            
        print("ERRO! Médico não encontrado.")


def excluir_medico():

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("ERRO! Não há médicos cadastrados.")
        return
    else:
        crm_excluido = input("Digite o CRM do médico que você deseja excluir: ").replace(" ", "").upper()
        while validacoes.validar_id(crm_excluido) == False:
            crm_excluido = input("Digite o CRM do médico que você deseja excluir: ").replace(" ", "").upper()

        for medico in banco_medico:
            if medico['crm'] == crm_excluido:

                banco_medico.remove(medico)

                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)
                return
            
        print("ERRO! Médico não encontrado.")
