import gerenciador_dados

ARQUIVO_PACIENTES = "pacientes.json"

def cadastrar_paciente(): 
    paciente = {}

    while True:
        paciente_nome = input("Digite o nome do paciente: ").strip()
        if paciente_nome == "":
            print("Nome inválido, escreva novamente.")
        else:
            paciente["nome"] = paciente_nome
            break

    while True:
        paciente_idade = input("Digite a idade do paciente: ").strip()
        if not paciente_idade.isdigit():
            print("Idade inválida. Digite apenas números inteiros.")
            continue
        elif int(paciente_idade) <= 0:
            print("Idade inválida. Digite uma idade maior ou igual a 1 ano.")
            continue
        else:
            paciente["idade"] = int(paciente_idade)
            break

    while True:
        paciente_sexo = input("Digite o sexo do paciente (M/F): ").strip().upper()
        if not paciente_sexo.replace(" ", "").isalpha():
            print("Sexo inválido. Digite apenas letras.")
        elif paciente_sexo not in "MF":
            print("Sexo inválido. Tente novamente")
        else:
            paciente["sexo"] = paciente_sexo
            break

    while True: 
        paciente_cpf = input("Digite o CPF do paciente (apenas números): ").strip()
        if not paciente_cpf.isdigit(): 
            print("CPF inválido. Digite apenas números.")
            continue
        elif len(paciente_cpf) != 11:
            print("CPF inválido. Digite apenas 11 digitos.")
            continue
        else:
            paciente["cpf"] = paciente_cpf
            break

    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    for p in banco_pacientes:
        if p['cpf'] == paciente_cpf:
            print("ERRO: Já existe um paciente cadastrado com este CPF.")
            return

    banco_pacientes.append(paciente)

    gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)


def info_paciente():
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("Não há pacientes cadastrados.")
        return
    else:
        while True: 
            id_cpf = input("Digite o CPF do paciente (apenas números): ").strip()
            if not id_cpf.isdigit(): 
                print("CPF inválido. Digite apenas números.")
                continue
            elif len(id_cpf) != 11:
                print("CPF inválido. Digite apenas 11 digitos.")
                continue
            else:
                break

        for paciente in banco_pacientes:
            if paciente["cpf"] == id_cpf:
                print(f"Nome: {paciente['nome']}")
                print(f"Idade: {paciente['idade']}")
                print(f"Sexo: {paciente['sexo']}")
                print(f"CPF: {paciente['cpf']}")
                return
            
        print("Paciente não encontrado.")

def alterar_paciente():
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("Não há pacientes cadastrados.")
        return
    else:
        while True: 
            id_cpf = input("Digite o CPF do paciente (apenas números): ").strip()
            if not id_cpf.isdigit(): 
                print("CPF inválido. Digite apenas números.")
                continue
            elif len(id_cpf) != 11:
                print("CPF inválido. Digite apenas 11 digitos.")
                continue
            else:
                break

    for paciente in banco_pacientes:
        if paciente["cpf"] == id_cpf:

            while True:
                novo_nome = input("Digite o novo nome do paciente: ").strip()
                if novo_nome == "":
                    print("Nome inválido, escreva novamente.")
                else:
                    break

            while True:
                nova_idade = input("Digite a nova idade do paciente: ").strip()
                if not nova_idade.isdigit():
                    print("Idade inválida. Digite apenas números inteiros.")
                    continue
                elif int(nova_idade) <= 0:
                    print("Idade inválida. Digite uma idade maior ou igual a 1 ano.")
                    continue
                else:
                    break

            while True:
                novo_sexo = input("Digite o novo sexo do paciente (M/F): ").strip().upper()
                if not novo_sexo.replace(" ", "").isalpha():
                    print("Sexo inválido. Digite apenas letras.")
                elif novo_sexo not in "MF":
                    print("Sexo inválido. Tente novamente")
                else:
                    break

            while True: 
                novo_cpf = input("Digite o novo CPF do paciente (apenas números): ").strip()
                if not novo_cpf.isdigit(): 
                    print("CPF inválido. Digite apenas números.")
                    continue
                elif len(novo_cpf) != 11:
                    print("CPF inválido. Digite apenas 11 digitos.")
                    continue
                else:
                    break

            for p in banco_pacientes:
                if p['cpf'] == novo_cpf and p['cpf'] != id_cpf: 
                    print("ERRO: Este novo CPF já pertence a outro paciente.")
                    return

            paciente["nome"] = novo_nome
            paciente["idade"] = int(nova_idade)
            paciente["sexo"] = novo_sexo
            paciente["cpf"] = novo_cpf
            
            gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)

            return
    print("Paciente não encontrado. Não foi possível alterar.")
        

def excluir_paciente():
    banco_pacientes = gerenciador_dados.carregar_dados(ARQUIVO_PACIENTES)

    if len(banco_pacientes) == 0:
        print("Não há pacientes cadastros.")
        return
    else:
        while True: 
            cpf_excluido = input("Digite o CPF do paciente para ser excluído (apenas números): ").strip()
            if not cpf_excluido.isdigit(): 
                print("CPF inválido. Digite apenas números.")
                continue
            elif len(cpf_excluido) != 11:
                print("CPF inválido. Digite apenas 11 digitos.")
                continue
            else:
                break

    for paciente in banco_pacientes:
        if paciente["cpf"] == cpf_excluido:
            banco_pacientes.remove(paciente)

            gerenciador_dados.salvar_dados(ARQUIVO_PACIENTES, banco_pacientes)
            return
        
    print("Paciente não encontrado. Não foi possível excluir.")