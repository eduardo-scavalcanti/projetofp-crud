from . import medicos
from . import pacientes
from . import consultas
from . import relatorios

def menu_medicos():
  while True:
    print("1 - Cadastrar médico")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro")
    print("4 - Excluir médico")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_medico = input("Opção: ").strip()

      if not opcao_medico.isdigit():
          print("Digite apenas números.")
          continue

      opcao_medico_int = int(opcao_medico)

      if 0 <= opcao_medico_int <= 4:
          opcao_medico = opcao_medico_int
          break
      else:
          print("Opção inválida.")

    match(opcao_medico): 
      case 1:
        medicos.cadastrar_medico()
      case 2:
        medicos.info_medico()
      case 3:
        medicos.alterar_medico()    
      case 4:
        medicos.excluir_medico()
      case 0:
        break
                    

def menu_pacientes():
  while True:
    print("1 - Cadastrar Paciente")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro")
    print("4 - Excluir Paciente")
    print("0 - Voltar para o menu principal ")

    
    while True:
      opcao_paciente = input("Opção: ").strip()

      if not opcao_paciente.isdigit():
          print("Digite apenas números.")
          continue

      opcao_paciente_int = int(opcao_paciente)

      if 0 <= opcao_paciente_int <= 4:
          opcao_paciente = opcao_paciente_int
          break
      else:
          print("Opção inválida.")

    match(opcao_paciente): 
      case 1:
        pacientes.cadastrar_paciente()
      case 2:
        pacientes.info_paciente()
      case 3:
        pacientes.alterar_paciente()    
      case 4:
        pacientes.excluir_paciente()
      case 0:
        break


def menu_consultas():
  while True:
    print("1 - Cadastrar Consulta")
    print("2 - Ver informações")
    print("3 - Alterar Cadastro de Consulta")
    print("4 - Excluir Consulta")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_consulta = input("Opção: ").strip()

      if not opcao_consulta.isdigit():
          print("Digite apenas números.")
          continue

      opcao_consulta_int = int(opcao_consulta)

      if 0 <= opcao_consulta_int <= 4:
          opcao_consulta = opcao_consulta_int
          break
      else:
          print("Opção inválida.")

    match(opcao_consulta): 
      case 1:
        consultas.cadastrar_consulta()
      case 2:
        consultas.info_consulta()
      case 3:
        consultas.alterar_consulta()    
      case 4:
        consultas.excluir_consulta()
      case 0:
        break
          

def menu_relatorios():
  while True:
    print("1 - Relatório por médicos")
    print("2 - Relatório por datas")
    print("0 - Voltar para o menu principal ")

    while True:
      opcao_relatorio = input("Opção: ").strip()

      if not opcao_relatorio.isdigit():
          print("Digite apenas números.")
          continue

      opcao_relatorio_int = int(opcao_relatorio)

      if 0 <= opcao_relatorio_int <= 4:
          opcao_relatorio = opcao_relatorio_int
          break
      else:
          print("Opção inválida.")

    match(opcao_relatorio): 
      case 1:
        relatorios.relatorio_data()
      case 2:
        relatorios.relatorio_medicos()   
      case 0:
        break


def menu_principal():
  while True:
    print("1 - Menu Médicos")
    print("2 - Menu Pacientes")
    print("3 - Menu Consultas")
    print("4 - Menu Relatórios")
    print("0 - Encerrar o Programa ")

    while True:
      opcao = input("Opção: ").strip()

      if not opcao.isdigit():
          print("Digite apenas números.")
          continue

      opcao_int = int(opcao)

      if 0 <= opcao_int <= 4:
          opcao = opcao_int
          break
      else:
          print("Opção inválida.")

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