import medicos


def menu_medicos():
    while True:
        print("1 - Cadastrar médico")
        print("2 - Ver informações")
        print("3 - Alterar Cadastro")
        print("4 - Excluir médico")
        print("0 - Voltar para o menu principal ")



        opcao = int(input("Opção: ")) 
        while opcao < 0 or opcao > 4:
            print("ERRO! Opção invalida.")
            opcao = int(input("Opção: "))

        match(opcao): 
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
                 
        ... 

def menu_pacientes():
    ...

def menu_consultas():
    ...

def menu_relatorios():
    ...

def menu_principal():
    ...