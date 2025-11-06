

prontuario = [
    {
        "Nome": "João Silva",
        "Idade": 30,
        "Sexo": "Masculino",
        "CPF": "12345678901",
        "Diagnóstico": "Hipertensão"
    },
    {
        "Nome": "Maria Oliveira",
        "Idade": 25,
        "Sexo": "Feminino",
        "CPF": "10987654321",
        "Diagnóstico": "Diabetes"
    },
    {
        "Nome": "Carlos Santos",
        "Idade": 40,
        "Sexo": "Masculino",
        "CPF": "98765432100",
        "Diagnóstico": "Asma"
    }
]



def cadastrar_paciente(): 

    
    print("Bem vindo ao cadastro de pacientes!")

    paciente = {}
        
    while True:  
        paciente_nome = input("Digite o nome do paciente: ")
        if not paciente_nome.isalpha():
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
            paciente["CPF"] = paciente_cpf
            break
    while True:
        paciente_diagnostico = input("Digite o diagnóstico do paciente: ")
        if not paciente_diagnostico.isalpha():
            print("Diagnóstico inválido. Digite um diagnóstico válido.")
        else:
            paciente["Diagnóstico"] = paciente_diagnostico
            break

    print(paciente)

def info_paciente():
    
    

def alterar_paciente():
    ...

def excluir_paciente():
    ...



cadastrar_paciente()