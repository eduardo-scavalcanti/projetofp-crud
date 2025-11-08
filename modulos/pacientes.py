import gerenciador_dados
ARQUIVOPACIENTES = "pacientes.json"

prontuario = [ # Depois que terminar apagar banco fictício.
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

    while True: #OK
        paciente_nome = input("Digite o nome do paciente: ")
        if not paciente_nome.replace(" ", "").isalpha():
            print("Nome inválido, escreva novamente.")
        else:
            paciente["Nome"] = paciente_nome
            break

    while True: #OK
        paciente_idade = input("Digite a idade do paciente: ")
        if not paciente_idade.isdigit():
            print("Idade inválida. Digite uma idade positiva.")
        else:
            paciente["Idade"] = int(paciente_idade)
            break

    while True:
        paciente_sexo = input("Digite o sexo do paciente: ") # Colocar na mensagem do input qual os inputs aceitos, por exemplo "Digite o sexo do paciente (M/F): "
        if paciente_sexo not in ["Masculino", "Feminino", "masculino", "feminino"]: # Recomendo utilizar apenas M ou F
            print("Sexo inválido. Digite 'Masculino', 'Feminino'.")
        else:
            paciente["Sexo"] = paciente_sexo
            break

    while True: # Como o CPF vai ser a informação que vai diferenciar um cadastro de paciente do outro, precisa primeiro consultar o banco para saber se já existe algum paciente com o CPF informado.
        paciente_cpf = input("Digite o CPF do paciente: ") # Informar na pergunta do input que aceita apenas números. # O programa está crashando quando eu deixo o campo vazio e dou enter.
        if not paciente_cpf.isdigit() and len(paciente_cpf) == 11:
            print("CPF não reconhecido. Digite novamente sem '.' ou '-'.")
        else:
            paciente["CPF"] = int(paciente_cpf) # não cadastrar o cpf como número inteiro, cadastrar como string
            break

    while True: #OK
        paciente_diagnostico = input("Digite o diagnóstico do paciente: ")
        if not paciente_diagnostico.isalpha():
            print("Diagnóstico inválido. Digite um diagnóstico válido.")
        else:
            paciente["Diagnóstico"] = paciente_diagnostico
            break

    print(paciente) # Retirar print do dicionário e colocar uma mensagem do tipo "Paciente cadastrado com sucesso!"

    gerenciador_dados.salvar_dados(ARQUIVOPACIENTES, paciente) # Do jeito que está a função salvar_dados vai apagar todos os pacientes cadastrados e salvar apenas o que acabou de ser criado. O que deve ser feito é 1° carregar os dados existentes no banco, 2° dar um append na lista do banco e passar o novo dicionário (paciente) e 3° salvar o banco com o paciente adicionado.


def info_paciente():
    prontuario = #gerenciador_dados.carregar_dados(ARQUIVOPACIENTES)
    print("Bem vindo ao prontuario de pacientes!")
    if len(prontuario) == 0:
        print("Nenhum paciente encontrado.")
        return
    else:
        id_cpf = input("Digite o CPF do paciente que deseja encontrar: ") # Usar o método .strip() evita erros de espaço no início e no final (sempre pensar em possíveis erros do usuário)
        while(id_cpf.isdigit() == False): # Está aceitando resposta com apenas 1 número. Colocar validação para ter no mínimo 11 que é o tamanho do CPF.
            print("CPF inválido. Digite novamente sem '.' ou '-'.") # Melhorar um pouco a mensagem de erro. Porque a condicional apenas verifica se a string é um dígito ou não. Colocar algo como "CPF inválido. Digite apenas números."
            id_cpf = input("Digite o CPF do paciente que deseja encontrar: ")
        id_cpf = int(id_cpf) # Não salvar o CPF como int, mas sim como string.
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
    id_cpf = input("Digite o CPF do paciente que deseja alterar: ") # Usar o .strip() para evitar erros de input do usuário
    while(id_cpf.isdigit() == False): # Está aceitando CPFs com menos ou mais de 11 dígitos.
        print("CPF inválido. Digite novamente sem '.' ou '-'.")
        id_cpf = input("Digite o CPF do paciente que deseja alterar: ")
    id_cpf = int(id_cpf) # Não transformar o CPF em inteiro.
    encontrado = False # Não entendi essa variável. Qual a diferença dela no código?
    for paciente in prontuario:
        if paciente["CPF"] == id_cpf:
            encontrado # Não entendi essa variável. Qual a diferença dela no código?

            novo_nome = input("Digite o novo nome do paciente: ") # Usar o .strip() para evitar erros de inputs do usuário
            while(novo_nome.replace(" ", "").isalpha() == False):
                print("Nome inválido, escreva novamente")
                novo_nome = input("Digite o novo nome do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário

            nova_idade = input("Digite a nova idade do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário
            while(nova_idade.isdigit() == False):
                print("Idade inválida. Digite uma idade positiva.") # Melhorar mensagem de erro porque se o usuário digitar uma letra vai aparecer essa mesma mensagem que não faz sentido.
                nova_idade = input("Digite a nova idade do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário
                nova_idade = int(nova_idade)

            novo_sexo = input("Digite o novo sexo do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário e informar os tipos de input da pergunta.
            while(novo_sexo not in ["Masculino", "Feminino", "masculino", "feminino"]): # Recomendo usar M e F
                print("Sexo inválido. Digite 'Masculino', 'Feminino'.")
                novo_sexo = input("Digite o novo sexo do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário e informar os tipos de input da pergunta.

            novo_cpf = input("Digite o novo CPF do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário
            while(novo_cpf.isdigit() == False and len(novo_cpf) != 11):
                print("CPF não reconhecido. Digite novamente sem '.' ou '-'.")
                novo_cpf = input("Digite o novo CPF do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário

            novo_diagnostico = input("Digite o novo diagnóstico do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário
            while(novo_diagnostico.replace(" ", "").isalpha() == False):
                print("Diagnóstico inválido. Digite um diagnóstico válido.")
                novo_diagnostico = input("Digite o novo diagnóstico do paciente: ")# Usar o .strip() para evitar erros de inputs do usuário

            paciente["Nome"] = novo_nome
            paciente["Idade"] = int(nova_idade)
            paciente["Sexo"] = novo_sexo
            paciente["CPF"] = int(novo_cpf) # Não transformar o CPF em int
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
        cpf_excluido = input("Digite o CPF do paciente que deseja excluir: ") # Usar o .strip()
        while(cpf_excluido.isdigit() == False): # Está aceitando CPF com mais ou menos de 11 digitos.
            print("CPF inválido. Digite novamente sem '.' ou '-'.") # Melhorar um pouco a mensagem de erro. Porque a condicional apenas verifica se a string é um dígito ou não. Colocar algo como "CPF inválido. Digite apenas números."
            cpf_excluido = input("Digite o CPF do paciente que deseja excluir: ")
        cpf_excluido = int(cpf_excluido) # Não transformar o input do CPF em int, deixar como string.
    for paciente in prontuario:
        if paciente["CPF"] == cpf_excluido:
            prontuario.remove(paciente)
            gerenciador_dados.salvar_dados(ARQUIVOPACIENTES, prontuario)
            print("Paciente excluído com sucesso.")
            return
    print("Paciente não encontrado. Não foi possível excluir.")

