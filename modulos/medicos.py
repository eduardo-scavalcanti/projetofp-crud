import gerenciador_dados
ARQUIVO_MEDICO = "medicos.json" 

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

    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    medico = {}

    if len(banco_medico) == 0:
        medico['id'] = 1
    else:
       medico['id'] = banco_medico[len(banco_medico) - 1]['id'] + 1
    medico['nome'] = nome_medico 
    medico['crm'] = crm_medico
    medico['especialidade'] = especialidade_medico

    banco_medico.append(medico)

    gerenciador_dados.salvar_dados(medico, ARQUIVO_MEDICO)
    
    print("Médico cadastrado com sucesso!")


def info_medico():
    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("Não há médicos cadastrados.")
        return
    else:
        id_busca = input("Digite o id do médico: ").strip()
        while(id_busca.isdigit() == False):
            print("INVÁLIDO. Insira um ID válido (apenas números)")
            id_busca = input("Digite o id do médico: ").strip()
        id_busca = int(id_busca)
        
    for medico in banco_medico:
        if medico["id"] == id_busca:
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
        id_alterado = input("Digite o id do médico: ").strip()
        while(id_alterado.isdigit() == False):
            print("INVÁLIDO. Insira um ID válido (apenas números)")
            id_alterado = input("Digite o id do médico: ").strip()
        id_alterado = int(id_alterado)

        for medico in banco_medico:
            if medico["id"] == id_alterado:
                novo_nome = input("Nome: ").strip()
                while(novo_nome.replace(" ", "").isalpha() == False):
                    print("INVÁLIDO! Insira um NOME (apenas letras).")
                    novo_nome = input("Nome do médico: ").strip()

                novo_crm = input("CRM: ").strip()
                while(novo_crm.isdigit() == False):
                    print("INVÁLIDO. Insira um CRM (apenas números).")
                    novo_crm = input("CRM do médico: ").strip()

                nova_especialidade = input("Especialidade: ").strip()
                while(nova_especialidade.isalpha() == False):
                    print("INVÁLIDO! Insira a especialidade do médico(apenas texto)")
                    nova_especialidade = input("Especialidade: ").strip()
                
                medico['nome'] = novo_nome
                medico['crm'] = novo_crm
                medico['especialidade'] = nova_especialidade
                
                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)

                print("Médico atualizado com sucesso!")
                return
            
        print("Médico não encontrado.")


def excluir_medico():
    banco_medico = gerenciador_dados.carregar_dados(ARQUIVO_MEDICO)

    if len(banco_medico) == 0:
        print("Não há médicos cadastrados.")
        return
    else:
        id_excluido = input("Digite o id do médico: ").strip()
        while(id_excluido.isdigit() == False):
            print("INVÁLIDO. Insira um ID válido (apenas números)")
            id_excluido = input("Digite o id do médico: ").strip()
        id_excluido = int(id_excluido)

        for medico in banco_medico:
            if(medico["id"] == id_excluido):
                banco_medico.remove(medico)

                gerenciador_dados.salvar_dados(ARQUIVO_MEDICO, banco_medico)
                
                print("Médico excluído com sucesso!")
                return
            
        print("Médico não encontrado.")