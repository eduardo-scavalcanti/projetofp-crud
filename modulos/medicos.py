import gerenciador_dados
ARQUIVOMEDICO = "medicos.json" 

def cadastrar_medico():
    nomemedico = str(input("Digite o nome do Médico: "))
    while(nomemedico.replace(" ", "").isalpha()== False):
        print("INVÁLIDO! Insira um NOME(apenas letras)")
        nomemedico = str(input("Digite o nome do Médico: "))
    crmmedico = input("Digite o CRM do Médico: ")
    while(crmmedico.isdigit() == False):
        print("INVÁLIDO. Insira um CRM (apenas números)")
        crmmedico = input("Digite o CRM do Médico: ")
    crmmedico = int(crmmedico)
    especialidademedico = str(input("Digite a especialidade do médico: "))
    while(especialidademedico.isalpha() == False):
        print("INVÁLIDO! Insira a especialidade do médico(apenas texto)")
        especialidademedico = str(input("Digite a especialidade do médico: "))

    bancomedico = gerenciador_dados.carregar_dados()
    medico = {}
    if len(bancomedico) == 0:
        medico["id"] = 1
    else:
       medico["id"] = bancomedico[len(bancomedico)-1]["id"]+1
    medico["nome"] = nomemedico 
    medico["crm"] = crmmedico
    medico["especialidade"] = especialidademedico
    print(bancomedico)
    gerenciador_dados.salvar_dados(medico, ARQUIVOMEDICO)
    print("Médico Cadastrado com sucesso!!")



def info_medico():
    bancomedico = gerenciador_dados.carregar_dados(ARQUIVOMEDICO)
    print("\n=== INFORMAÇÕES DOS MÉDICOS CADASTRADOS ===")
    if len(bancomedico) == 0:
        print("Nenhum médico cadastrado.")
        return
    else:
        id_busca = input("\nDigite o ID do médico: ")
        while(id_busca.isdigit() == False):
            print("INVÁLIDO. Insira um ID válido (apenas números)")
            id_busca = input("\nDigite o ID do médico: ")
        id_busca = int(id_busca)
    for medico in bancomedico:
            if medico["id"] == id_busca:
                print("--- Dados do Médico: ---")
                print(f"ID: {medico['id']}")
                print(f"Nome: {medico['nome']}")
                print(f"CRM: {medico['crm']}")
                print(f"Especialidade: {medico['especialidade']}")
                return
            else:
                print("Médico não encontrado.")
                return


def alterar_medico():
    bancomedico = gerenciador_dados.carregar_dados(ARQUIVOMEDICO)
    print("=== ALTERAR O CADASTRO DE UM MÉDICO ===")
    id_alterado = input("Digite o ID do médico que você quer alterar: ")
    while(id_alterado.isdigit() == False):
        print("INVÁLIDO. Insira um ID válido (apenas números)")
        id_alterado = input("Digite o ID do médico que você quer alterar: ")
    id_alterado = int(id_alterado)
    encontrado = False 
    for medico in bancomedico:
        if medico["id"] == id_alterado:
            encontrado = True  
            novo_nome = input("Novo nome: ").strip()
            while(novo_nome.replace(" ", "").isalpha() == False):
                print("INVÁLIDO! Insira um NOME (apenas letras)")
                novo_nome = input("Novo nome: ").strip()
            novo_crm = input("Novo CRM: ").strip()
            while(novo_crm.isdigit() == False):
                print("INVÁLIDO. Insira um CRM (apenas números)")
                novo_crm = input("Novo CRM: ").strip()
            nova_especialidade = input("Nova especialidade: ").strip()
            while(nova_especialidade.replace(" ", "").isalpha() == False):
                print("INVÁLIDO! Insira a especialidade do médico (apenas texto)")
                nova_especialidade = input("Nova especialidade: ").strip()
            print("Médico atualizado com sucesso!")
            medico["nome"] = novo_nome
            medico["crm"] = novo_crm
            medico["especialidade"] = nova_especialidade
            break  
    if not encontrado:
        print("ID não encontrado. Não é possível alterar o cadastro.")
    gerenciador_dados.salvar_dados(bancomedico, ARQUIVOMEDICO)


def excluir_medico():
    ...

