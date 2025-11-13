import gerenciador_dados
from . import validacoes

ARQUIVO_PACIENTES = "pacientes.json"

def cadastrar_paciente(): 
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    paciente_cpf = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
    while validacoes.validar_cpf(paciente_cpf) == False: 
        paciente_cpf = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
    
    for paciente in banco_pacientes:
        if paciente_cpf == paciente['cpf']:
            print("ERRO! Já existe um paciente cadastrado com esse CPF.")
            return False

    paciente = {}

    if len(banco_pacientes) == 0:
        paciente['id'] = 1
    else:
       paciente['id'] = banco_pacientes[len(banco_pacientes) - 1]['id'] + 1

    paciente['cpf'] = paciente_cpf

    paciente_nome = input("Nome: ").strip().title()
    while validacoes.validar_nome(paciente_nome) == False:
        paciente_nome = input("Nome: ").strip().title()
    
    paciente['nome'] = paciente_nome

    paciente_sexo = input("Sexo (M/F): ").replace(" ", "").upper()
    while validacoes.validar_sexo(paciente_sexo) == False:
        paciente_sexo = input("Sexo (M/F): ").replace(" ", "").upper()

    paciente['sexo'] = paciente_sexo

    paciente_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")
    while validacoes.validar_data_nascimento(paciente_nascimento_medico) == False:
        paciente_nascimento_medico = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")

    paciente['data_nascimento'] = paciente_nascimento_medico

    paciente_email = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()
    while validacoes.validar_email(paciente_email) == False:
        paciente_email = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()

    paciente['email'] = paciente_email

    paciente_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
    while validacoes.validar_numero(paciente_numero) == False:
        paciente_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
        
    paciente['numero'] = paciente_numero

    banco_pacientes.append(paciente)

    gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)

    print("\n\033[1;32mPaciente cadastrado com sucesso.\033[0;0m")


def info_paciente():

    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("ERRO! Não há pacientes cadastrados.")
        return
    else:
        cpf = input("Digite o CPF do paciente que você deseja verificar (XXXXXXXXXXX): ").replace(" ", "")
        if validacoes.validar_cpf(cpf) == False:
            cpf = input("Digite o CPF do paciente que você deseja verificar (XXXXXXXXXXX): ").replace(" ", "")

        for paciente in banco_pacientes:
            if paciente['cpf'] == cpf:
                print(f"ID: {paciente['id']}")
                print(f"CPF: {paciente['cpf']}")
                print(f"Nome: {paciente['nome']}")
                print(f"Sexo: {paciente['sexo']}")
                print(f"Data de nascimento: {paciente['data_nascimento']}")
                print(f"E-mail: {paciente['email']}")
                print(f"Celular: {paciente['numero']}")
                return
            
        print("ERRO! Paciente não encontrado.")

def alterar_paciente():

    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("ERRO! Não há pacientes cadastrados.")
        return
    else: 
        cpf = input("Digite o CPF do paciente que você deseja alterar (XXXXXXXXXXX): ").replace(" ", "")
        if validacoes.validar_cpf(cpf) == False: 
            cpf = input("Digite o CPF do paciente que você deseja alterar (XXXXXXXXXXX): ").replace(" ", "")

    for paciente in banco_pacientes:
        if paciente['cpf'] == cpf:

            novo_cpf = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
            while validacoes.validar_cpf(novo_cpf) == False: 
                novo_cpf = input("CPF (XXXXXXXXXXX): ").replace(" ", "")
            
            for paciente in banco_pacientes:
                if novo_cpf == paciente['cpf']:
                    print("ERRO! Já existe um paciente cadastrado com esse CPF.")
                    return False

            paciente = {}

            paciente['cpf'] = novo_cpf

            novo_nome = input("Nome: ").strip().title()
            while validacoes.validar_nome(novo_nome) == False:
                novo_nome = input("Nome: ").strip().title()
            
            paciente['nome'] = novo_nome

            novo_sexo = input("Sexo (M/F): ").replace(" ", "").upper()
            while validacoes.validar_sexo(novo_sexo) == False:
                novo_sexo = input("Sexo (M/F): ").replace(" ", "").upper()

            paciente['sexo'] = novo_sexo

            nova_data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")
            while validacoes.validar_data_nascimento(nova_data_nascimento) == False:
                nova_data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").replace(" ", "")

            paciente['data_nascimento'] = nova_data_nascimento

            novo_email = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()
            while validacoes.validar_email(novo_email) == False:
                novo_email = input("E-mail (nome@dominio.com): ").replace(" ", "").lower()

            paciente['email'] = novo_email

            novo_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
            while validacoes.validar_numero(novo_numero) == False:
                novo_numero = input("Número de celular (DDD)9XXXX-XXXX: ").replace(" ", "")
                
            paciente['numero'] = novo_numero

            gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)
            return
        
    print("ERRO! Paciente não encontrado.")
        

def excluir_paciente():
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("ERRO! Não há pacientes cadastros.")
        return
    else:
        cpf_excluido = input("Digite o CPF do paciente que você deseja excluir (XXXXXXXXXXX): ").replace(" ", "")
        if validacoes.validar_cpf(cpf_excluido) == False: 
            cpf_excluido = input("Digite o CPF do paciente que você deseja alterar (XXXXXXXXXXX): ").replace(" ", "")

    for paciente in banco_pacientes:
        if paciente["cpf"] == cpf_excluido:
            banco_pacientes.remove(paciente)

            gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)
            return
        
    print("ERRO! Paciente não encontrado.")