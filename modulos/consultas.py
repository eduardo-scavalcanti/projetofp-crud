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
    print(data_consulta)

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
    especialidade_medico = input('Informe a especialidade do médico: ')
    while especialidade_medico.replace(" ", "").isalpha() == False:
        print('Digite apenas letras. Tente novamente!')
        especialidade_medico = input('Informe a especialidade do médico: ')

    def formas_pagamento():
        print('1 - Pix')
        print('2 - Cartão')
        print('3 - Dinheiro')

    formas_pagamento()
    pagamento = input('Digite a forma do pagamento: ')
    while pagamento not in ['1', '2', '3']:
        print('Digite uma opção de pagamento dentre uma das opções acima. Tente novamente!')
        pagamento = input('Digite a forma do pagamento:')
    
    if pagamento == '1':
        print('Pagamento Confirmado!')
    
    if pagamento == '2':
        print('Pagamento efetuado com sucesso!')
    
    if pagamento == '3':
        valor = float(input('Informe o valor da consulta: R$'))
        especie = float(input('Informe o valor pago em espécie: R$'))
        troco = especie - valor
        if troco != 0:
            print(f'O valor do troco foi de R${troco:.2f}')

    banco_consulta = gerenciador_dados.carregar_dados()
    consulta = {}
    if len(banco_consulta) == 0:
        consulta['id'] = 1
    else:
        consulta['id'] = banco_consulta[len(banco_consulta)-1]['id']+1
    consulta['especialidade'] = especialidade_medico
    consulta['pagamento'] = pagamento
    banco_consulta.append(consulta)
    print(banco_consulta)
    banco_consulta = gerenciador_dados.salvar_dados(ARQUIVO_CONSULTA,consulta)

info_consulta()

def alterar_consulta():
    ...

def excluir_consulta():
    ...