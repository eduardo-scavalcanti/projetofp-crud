import gerenciador_dados
ARQUIVO_CONSULTA = 'consultas.json'

def cadastrar_consulta():
    nome_medico = input('Digite o nome do médico: ')
    while nome_medico.replace(" ", "").isalpha() == False:
        print('Digite apenas letras. Tente novamante!')
        nome_medico = input('Digite o nome do médico: ')

    nome_paciente = input('Digite o nome do paciente: ')
    while nome_paciente.replace(" ", "").isalpha() == False:
        print('Digite apenas letras. Tente novamante!')
        nome_paciente = input('Digite o nome do médico: ')

    dia = int(input('Digite o dia da consulta: '))
    while dia < 1 or dia > 31:
        print('Digite o dia entre 1 e 31. Tente novamente!')
        dia = int(input('Digite o dia da consulta: '))

    mes = int(input('Digite o mês da consulta: '))
    while mes < 1 or mes > 12:
        print('Digite o mês entre 1 e 12. Tente novamente!')
        mes = int(input('Digite o mês da consulta: '))
      
    ano = int(input('Digite o ano da consulta: '))
    while ano <= 2024:
        print('O ano da consulta precisa ser acima ou igual a 2025. Tente novamente!')
        ano = int(input('Digite o ano da consulta: '))

    data_consulta = f'{dia}/{mes}/{ano}'
    

    queixa = input('Qual foi a queixa do cliente: ')
    while queixa.replace(" ", "").isalpha() == False:
        print('Digite apenas letras. Tente novamante!')
        queixa = input('Qual foi a queixa do cliente: ')

    banco_consulta = gerenciador_dados.carregar_dados()
    consulta = {}
    if len(banco_consulta) == 0:
        consulta['id'] = 1
    else:
        consulta['id'] = banco_consulta[len(banco_consulta)-1]['id']+1
    consulta['medico'] = nome_medico
    consulta['paciente'] = nome_paciente
    consulta['data'] = data_consulta
    consulta['queixa'] = queixa
    banco_consulta.append(consulta)
    print(banco_consulta)
    banco_consulta = gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA,consulta)
    
def info_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVO_CONSULTA)
    if len(bancoconsulta) == 0:
        print('Nenhum consulta cadastrado.')
    else:
        id_consulta = input('Digite o ID da consulta: ')
        while id_consulta.isdigit() == False:
            print('Digite apenas o ID (apenas números).')
            id_consulta = input('Digite o ID da consulta: ')
        id_consulta = int(id_consulta)

        for consulta in banco_consulta:
            if consulta['id'] == id_consulta:
                print('Dados da Consulta:')
                print(f'ID : {consulta['id']}')
                print(f'Médico : {consulta['medico']}')
                print(f'Paciente : {consulta['paciente']}')
                print(f'Data : {consulta['data']}')
                print(f'Queixa : {consulta['queixa']}')
            else:
                print('A consulta não foi encontrada!')
                return

def alterar_consulta():
    banco_consulta = gerenciador_dados.carregar_dados(ARQUIVOMEDICO)
    id_alterado = input("Digite o ID do médico que você quer alterar: ")
    while(id_alterado.isdigit() == False):
        print("INVÁLIDO. Insira um ID válido (apenas números)")
        id_alterado = input("Digite o ID do médico que você quer alterar: ")
    id_alterado = int(id_alterado)
    encontrado = False

    for consulta in banco_consulta:
        if consulta["id"] == id_alterado:
            encontrado = True  
            novo_nomemedico = input("Novo nome do médico: ").strip()
            while(novo_nomemedico.replace(" ", "").isalpha() == False):
                print("INVÁLIDO! Insira um NOME (apenas letras)")
                novo_nomemedico = input("Novo nome do médico: ").strip()

            novo_nomepaciente = input("Novo nome do paciente: ").strip()
            while(novo_nomepaciente.replace(" ", "").isalpha() == False):
                print("INVÁLIDO. Insira um NOME (apenas letras)")
                novo_nomepaciente = input("Novo nome do paciente: ").strip()

            novo_dia = input("Novo dia da consulta: ").strip()
            while(novo_dia.isdigit() == False):
                print("INVÁLIDO! Insira o dia da consulta (apenas números)")
                novo_dia = input("Novo dia da consulta: ").strip()

            novo_mes = input("Novo mês da consulta: ").strip()
            while(novo_mes.isdigit() == False):
                print("INVÁLIDO! Insira o mês da consulta (apenas números)")
                novo_mes = input("Novo mês da consulta: ").strip()

            novo_ano = input("Novo ano da consulta: ").strip()
            while(novo_ano.isdigit() == False):
                print("INVÁLIDO! Insira o ano da consulta (apenas números)")
                novo_ano = input("Novo ano da consulta: ").strip()

            nova_dataconsulta = f'{novo_dia}/{novo_mes}/{novo_ano}'

            print("Consulta atualizada com sucesso!")
            medico['medico'] = novo_nomemedico
            medico['paciente'] = novo_nomepaciente
            medico['data'] = nova_dataconsulta
            break  
    if not encontrado:
        print("ID não encontrado. Não é possível alterar o cadastro.")
    gerenciador_dados.salvar_dados(banco_consulta, ARQUIVO_CONSULTA)

def excluir_consulta():
    ...