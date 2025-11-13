from . import medicos
from . import pacientes
from . import consultas
from . import relatorios
from . import mensagens


def menu_medicos():
  while True:
    mensagens.titulo("MÓDULO MÉDICOS")
    print("1 - Cadastrar médico")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro")
    print("4 - Excluir médico")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_medico = input("Opção: ").replace(" ", "")

      if opcao_medico.isdigit() == False:
        mensagens.erro("ERRO! Digite apenas números.")
        continue
      else:
        opcao_medico = int(opcao_medico)
        break

    match(opcao_medico): 
      case 1:
        mensagens.titulo("CADASTRAR MÉDICO")
        medicos.cadastrar_medico()
      case 2:
        mensagens.titulo("INFORMAÇÕES MÉDICO")
        medicos.info_medico()
      case 3:
        mensagens.titulo("ALTERAR MÉDICO")
        medicos.alterar_medico()    
      case 4:
        mensagens.titulo("EXCLUIR MÉDICO")
        medicos.excluir_medico()
      case 0:
        break
      case __:
        mensagens.erro("ERRO! Opção inválida")
                    

def menu_pacientes():
  while True:
    mensagens.titulo("MÓDULO PACIENTES")
    print("1 - Cadastrar Paciente")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro")
    print("4 - Excluir Paciente")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_paciente = input("Opção: ").replace(" ", "")

      if not opcao_paciente.isdigit():
        mensagens.erro("ERRO! Digite apenas números.")
        continue
      else:
        opcao_paciente = int(opcao_paciente)
        break

    match(opcao_paciente): 
      case 1:
        mensagens.titulo("CADASTRAR PACIENTE")
        pacientes.cadastrar_paciente()
      case 2:
        mensagens.titulo("INFORMAÇÕES PACIENTE")
        pacientes.info_paciente()
      case 3:
        mensagens.titulo("ALTERAR PACIENTE")
        pacientes.alterar_paciente()    
      case 4:
        mensagens.titulo("EXCLUIR PACIENTE")
        pacientes.excluir_paciente()
      case 0:
        break
      case __:
        mensagens.erro("ERRO! Opção inválida")


def menu_consultas():
  while True:
    mensagens.titulo("MÓDULO CONSULTAS")
    print("1 - Cadastrar Consulta")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro de Consulta")
    print("4 - Excluir Consulta")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_consulta = input("Opção: ").replace(" ", "")

      if not opcao_consulta.isdigit():
          mensagens.erro("ERRO! Digite apenas números.")
          continue
      else:
        opcao_consulta = int(opcao_consulta)
        break

    match(opcao_consulta): 
      case 1:
        mensagens.titulo("AGENDAR CONSULTA")
        consultas.cadastrar_consulta()
      case 2:
        mensagens.titulo("INFORMAÇÕES CONSULTA")
        consultas.info_consulta()
      case 3:
        mensagens.titulo("ALTERAR CONSULTA")
        consultas.alterar_consulta()    
      case 4:
        mensagens.titulo("EXCLUIR CONSULTA")
        consultas.excluir_consulta()
      case 0:
        break
      case __:
        mensagens.erro("ERRO! Opção inválida")
          

def menu_relatorios():
  while True:
    mensagens.titulo("MÓDULO RELATÓRIOS")
    print("1 - Relatório por médicos")
    print("2 - Relatório por datas")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_relatorio = input("Opção: ").replace(" ", "")

      if not opcao_relatorio.isdigit():
          mensagens.erro("ERRO! Digite apenas números.")
          continue
      else:
        opcao_relatorio = int(opcao_relatorio)
        break

    match(opcao_relatorio): 
      case 1:
        mensagens.titulo("RELATÓRIO POR MÉDICOS")
        relatorios.relatorio_medicos()
      case 2:
        mensagens.titulo("RELATÓRIO POR DATA")
        relatorios.relatorio_data() 
      case 0:
        break
      case __:
        mensagens.erro("ERRO! Opção inválida")


def menu_principal():
  while True:
    mensagens.titulo("MENU PRINCIPAL")
    print("1 - Menu Médicos")
    print("2 - Menu Pacientes")
    print("3 - Menu Consultas")
    print("4 - Menu Relatórios")
    print("0 - Encerrar o Programa ")

    while True:
      opcao = input("Opção: ").replace(" ", "")

      if opcao.isdigit() == False:
        print("ERRO! Digite apenas números.")
        continue
      else:
        opcao = int(opcao)
        break

    match(opcao): 
      case 1:
        menu_medicos()
      case 2:
        menu_pacientes()
      case 3:
        menu_consultas()    
      case 4:
        menu_relatorios()
      case 0:
          break
      case __:
        mensagens.erro("ERRO! Opção inválida.")