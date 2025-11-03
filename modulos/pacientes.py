
def cadastrar_paciente(): 

    
    print("Bem vindo ao cadastro de pacientes!")

    paciente = {}
        
    paciente_nome = input("Digite o nome do paciente: "),
    while True:
        paciente_idade = int(input("Digite a idade do paciente: "))
        if paciente_idade < 0 or paciente_idade > 120:
            print("Idade inválida. Digite uma idade positiva.")
        else:
            paciente["Nome"] = paciente_nome
            paciente["Idade"] = paciente_idade
            break
    while True:
        paciente_sexo = input("Digite o sexo do paciente: ")
        if paciente_sexo not in ["Masculino", "Feminino", "maculino", "feminino"]:
            print("Sexo inválido. Digite 'Masculino', 'Feminino'.")
        else:
            paciente["Sexo"] = paciente_sexo
            break
    while True:
        paciente_cpf = input("Digite o CPF do paciente: ")
        if len(paciente_cpf) != 11:
            print("CPF não reconhecido. Digite novamente sem '.' ou '-'.")
        else:
            paciente["CPF"] = paciente_cpf
            break
    while True:
        paciente_endereco = input("Digite o endereço do paciente: ")
        if not paciente_endereco:
            print("Endereço inválido. Digite um endereço válido.")
        else:
            paciente["Endereço"] = paciente_endereco
            break

    print (f"Paciente {paciente_nome} cadastrado com sucesso!\n possui {paciente_idade} anos, sexo {paciente_sexo}, CPF {paciente_cpf} e endereço {paciente_endereco}.")
    print(paciente)

def info_paciente():
    ...

def alterar_paciente():
    ...

def excluir_paciente():
    ...



cadastrar_paciente()