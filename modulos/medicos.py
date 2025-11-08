import gerenciador_dados
ARQUIVOMEDICO = "medicos.json" 

def cadastrar_medico():
    nome_medico = input("Nome: ").strip()
    while(nome_medico.replace(" ", "").isalpha() == False):
        print("INVÁLIDO! Insira um NOME (apenas letras).")
        nome_medico = input("Nome do médico: ").strip()

    crm_medico = input("CRM: ").strip()
    while(crm_medico.isdigit() == False):
        print("INVÁLIDO. Insira um CRM (apenas números).")
        crm_medico = input("CRM do médico: ").strip()

    especialidade_medico = input("Especialidade: ").strip()
    while(especialidade_medico.isalpha() == False):
        print("INVÁLIDO! Insira a especialidade do médico(apenas texto)")
        especialidade_medico = input("Especialidade: ").strip()

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVOMEDICO)

    medico = {}

    if len(banco_medico) == 0:
        medico['id'] = 1
    else:
       medico['id'] = banco_medico[len(banco_medico) - 1]['id'] + 1
    medico['nome'] = nome_medico 
    medico['crm'] = crm_medico
    medico['especialidade'] = especialidade_medico

    banco_medico.append(medico)

    gerenciador_dados.salvar_dados(medico, ARQUIVOMEDICO)
    
    print("Médico cadastrado com sucesso!")


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
    bancomedico = gerenciador_dados.carregar_dados(ARQUIVOMEDICO)
    if len(bancomedico)==0:
        print("Não Há Médicos cadastrados nesse banco.")
        return
    else:
        id_excluido = input("Digite o ID você quer excluir: ")
        while(id_excluido.isdigit() == False):
            print("INVÁLIDO. Insira um CRM (apenas números)")
            id_excluido = input("Digite o ID você quer excluir: ")
        id_excluido = int(id_excluido)
        for medico in bancomedico:
            if(medico["id"] == id_excluido):
                bancomedico.remove(medico)
                print("Médico excluido com sucesso!!")
                bancomedico = gerenciador_dados.salvar_dados(ARQUIVOMEDICO, bancomedico)
                return
        print("Médico Não encontrado. Não é possível excluir.")