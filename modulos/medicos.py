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
cadastrar_medico()

def info_medico():
    print("===INFORMAÇÕES DOS MÉDICOS===")
    opcao = str(input("Deseja procurar por algum médico ? (S/N)"))
    if(opcao in "Ss"):
        print("")
info_medico()

def alterar_medico():
    ...

def excluir_medico():
    ...

