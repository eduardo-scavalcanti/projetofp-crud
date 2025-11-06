import gerenciador_dados
ARQUIVOPACIENTES = "pacientes.json"

prontuario = [
    {
        "Nome": "João Silva",
        "Idade": 30,
        "Sexo": "Masculino",
        "CPF": 12345678901,
        "Diagnóstico": "Hipertensão"
    },
    {
        "Nome": "Maria Oliveira",
        "Idade": 25,
        "Sexo": "Feminino",
        "CPF": 10987654321,
        "Diagnóstico": "Diabetes"
    },
    {
        "Nome": "Carlos Santos",
        "Idade": 40,
        "Sexo": "Masculino",
        "CPF": 98765432100,
        "Diagnóstico": "Asma"
    }
]



def cadastrar_paciente(): 

    
    print("Bem vindo ao cadastro de pacientes!")

    paciente = {}
        
    while True:  
        paciente_nome = input("Digite o nome do paciente: ")
        if not paciente_nome.replace(" ", "").isalpha():
            print("Nome inválido, escreva novamente")
        else:
            paciente["Nome"] = paciente_nome
            break
    while True:
        paciente_idade = input("Digite a idade do paciente: ")
        if not paciente_idade.isdigit():
            print("Idade inválida. Digite uma idade positiva.")
        else:
            paciente["Idade"] = int(paciente_idade)
            break
    while True:
        paciente_sexo = input("Digite o sexo do paciente: ")
        if paciente_sexo not in ["Masculino", "Feminino", "masculino", "feminino"]:
            print("Sexo inválido. Digite 'Masculino', 'Feminino'.")
        else:
            paciente["Sexo"] = paciente_sexo
            break
    while True:
        paciente_cpf = input("Digite o CPF do paciente: ")
        if not paciente_cpf.isdigit() and len(paciente_cpf) == 11:
            print("CPF não reconhecido. Digite novamente sem '.' ou '-'.")
        else:
            paciente["CPF"] = int(paciente_cpf)
            break
    while True:
        paciente_diagnostico = input("Digite o diagnóstico do paciente: ")
        if not paciente_diagnostico.isalpha():
            print("Diagnóstico inválido. Digite um diagnóstico válido.")
        else:
            paciente["Diagnóstico"] = paciente_diagnostico
            break

    print(paciente)

    gerenciador_dados.salvar_dados(ARQUIVOPACIENTES, paciente)

def info_paciente():
    prontuario = gerenciador_dados.carregar_dados(ARQUIVOPACIENTES)
    print("Bem vindo ao prontuario de pacientes!")
    if len(prontuario) == 0:
        print("Nenhum paciente encontrado.")
        return
    else:
        id_cpf = input("Digite o CPF do paciente que deseja encontrar: ")
        while(id_cpf.isdigit() == False):
            print("CPF inválido. Digite novamente sem '.' ou '-'.")
            id_cpf = input("Digite o CPF do paciente que deseja encontrar: ")
        id_cpf = int(id_cpf)
    for paciente in prontuario:
        if paciente["CPF"] == id_cpf:
            print("--- Prontuário do Paciente ---")
            print(f"Nome: {paciente['Nome']}")
            print(f"Idade: {paciente['Idade']}")
            print(f"Sexo: {paciente['Sexo']}")
            print(f"CPF: {paciente['CPF']}")
            print(f"Diagnóstico: O paciente possui {paciente['Diagnóstico']}")
            return
        else:
            print("Paciente não encontrado.")
            return

def alterar_paciente():
    prontuario = gerenciador_dados.carregar_dados(ARQUIVOPACIENTES)
    print("Bem vindo ao menu de alterações de pacientes!")
    id_cpf = input("Digite o CPF do paciente que deseja alterar: ")
    while(id_cpf.isdigit() == False):
        print("CPF inválido. Digite novamente sem '.' ou '-'.")
        id_cpf = input("Digite o CPF do paciente que deseja alterar: ")
    id_cpf = int(id_cpf)
    encontrado = False
    for paciente in prontuario:
        if paciente["CPF"] == id_cpf:
            encontrado = True
            novo_nome = input("Digite o novo nome do paciente: ")
            while(novo_nome.replace(" ", "").isalpha() == False):
                print("Nome inválido, escreva novamente")
                novo_nome = input("Digite o novo nome do paciente: ")
            nova_idade = input("Digite a nova idade do paciente: ")
            while(nova_idade.isdigit() == False):
                print("Idade inválida. Digite uma idade positiva.")
                nova_idade = input("Digite a nova idade do paciente: ")
                nova_idade = int(nova_idade)
            novo_sexo = input("Digite o novo sexo do paciente: ")
            while(novo_sexo not in ["Masculino", "Feminino", "masculino", "feminino"]):
                print("Sexo inválido. Digite 'Masculino', 'Feminino'.")
                novo_sexo = input("Digite o novo sexo do paciente: ")
            novo_cpf = input("Digite o novo CPF do paciente: ")
            while(novo_cpf.isdigit() == False and len(novo_cpf) != 11):
                print("CPF não reconhecido. Digite novamente sem '.' ou '-'.")
                novo_cpf = input("Digite o novo CPF do paciente: ")
            novo_diagnostico = input("Digite o novo diagnóstico do paciente: ")
            while(novo_diagnostico.replace(" ", "").isalpha() == False):
                print("Diagnóstico inválido. Digite um diagnóstico válido.")
                novo_diagnostico = input("Digite o novo diagnóstico do paciente: ")
            paciente["Nome"] = novo_nome
            paciente["Idade"] = int(nova_idade)
            paciente["Sexo"] = novo_sexo
            paciente["CPF"] = int(novo_cpf)
            paciente["Diagnóstico"] = novo_diagnostico
            break
        else:
            print("Paciente não encontrado. Não foi possível alterar.")
        gerenciador_dados.salvar_dados(ARQUIVOPACIENTES, prontuario)

def excluir_paciente():
    prontuario = gerenciador_dados.carregar_dados(ARQUIVOPACIENTES)
    print("Bem vindo ao menu de exclusão de pacientes!")
    if len(prontuario) == 0:
        print("Nenhum paciente encontrado.")
        return
    else:
        cpf_excluido = input("Digite o CPF do paciente que deseja excluir: ")
        while(cpf_excluido.isdigit() == False):
            print("CPF inválido. Digite novamente sem '.' ou '-'.")
            cpf_excluido = input("Digite o CPF do paciente que deseja excluir: ")
        cpf_excluido = int(cpf_excluido)
    for paciente in prontuario:
        if paciente["CPF"] == cpf_excluido:
            prontuario.remove(paciente)
            gerenciador_dados.salvar_dados(ARQUIVOPACIENTES, prontuario)
            print("Paciente excluído com sucesso.")
            return
    print("Paciente não encontrado. Não foi possível excluir.")

