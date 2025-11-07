import medicos
import pacientes
import relatorios
import consultas

def menu_medicos():
    while True:
        print("1 - Cadastrar médico")
        print("2 - Ver informações")
        print("3 - Alterar Cadastro")
        print("4 - Excluir médico")
        print("0 - Voltar para o menu principal ")



        opcaomedico = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)
        while opcaomedico < 0 or opcaomedico > 4:
            print("ERRO! Opção inválida.")
            opcaomedico = (input("Opção: "))
       

        match(opcaomedico): 
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



        opcaopaciente = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)
        while opcaopaciente < 0 or opcaopaciente > 4:
            print("ERRO! Opção inválida.")
            opcaopaciente = int(input("Opção: "))

        match(opcaopaciente): 
                case 1:
                  pacientes.cadastrar_paciente()
                case 2:
                  pacientes.info_paciente()
                case 3:
                  pacientes.alterar_paciente()    
                case 4:
                    pacientes.excluir_paciente()
                case 0:
                    menu_principal() #break


def menu_consultas():
    while True:
        print("1 - Cadastrar Consulta")
        print("2 - Ver informações")
        print("3 - Alterar Cadastro de Consulta")
        print("4 - Excluir Consulta")
        print("0 - Voltar para o menu principal ")



        opcaoconsulta = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)
        while opcaoconsulta < 0 or opcaoconsulta > 4:
            print("ERRO! Opção inválida.")
            opcaoconsulta = int(input("Opção: ")) 

        match(opcaoconsulta): 
                case 1:
                  consultas.cadastrar_consulta()
                case 2:
                  consultas.info_consulta()
                case 3:
                  consultas.alterar_consulta()    
                case 4:
                    consultas.excluir_consulta()
                case 0:
                    menu_principal() #break
          

def menu_relatorios():
    while True:
        print("1 - Cadastrar Relatorio")
        print("2 - Ver informações de Relatorio")
        print("0 - Voltar para o menu principal ")



        opcaorelatorio = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)
        while opcaorelatorio < 0 or opcaorelatorio > 2:
            print("ERRO! Opção invalida.")
            opcaorelatorio = int(input("Opção: "))

        match(opcaorelatorio): 
                case 1:
                  relatorios.relatorio_data()
                case 2:
                  relatorios.relatorio_medicos()   
                case 0:
                    menu_principal() #break


def menu_principal():
     while True:
        print("1 - Menu Médicos")
        print("2 - Menu Pacientes")
        print("3 - Menu Consultas")
        print("4 - Menu Relatórios")
        print("0 - Encerrar o Programa ")



        opcao = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)
        while opcao < 0 or opcao > 4:
            print("ERRO! Opção inválida.")
            opcao = int(input("Opção: ")) # Fazer validação para caso o usuário digitar uma letra ou caractere especial. (copiar de Tiago)

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
menu_principal()