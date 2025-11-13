from datetime import datetime
import re

def validar_id(id):
    if id == "":
        print("ERRO! Campo em branco.")
        return False

    try:
        int(id)
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")
        return False
    
    if int(id) <= 0:
        print("ERRO! Id menor ou igual a zero.")
        return False
    

def validar_nome(nome):
    if nome == "":
        print("ERRO! Campo em branco.")
        return False

    if not nome.replace(" ", "").isalpha():
        print("ERRO! Digite apenas letras.")
        return False

    return True


def validar_data_nascimento(data):
    if data == "":
        print("ERRO! Campo vazio.")
        return False
    
    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        print("ERRO! Formato incorreto.")
        print("Ex.: 19/02/2017")
        return False
    
    hoje = datetime.now().date()
    
    try:
        data_datetime = datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        print("ERRO! Data inválida.")
        return False

    if data_datetime > hoje:
        print("ERRO! A data deve ser igual ou menor que a de hoje.")
        return False
    
    return True


def validar_data_consulta(data):
    if data == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        print("ERRO! Formato incorreto.")
        print("Ex.: 01/01/2031")
        return False
    
    hoje = datetime.now().date()
    try:
        data_datetime = datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        print("ERRO! Data inválida.")
        return False
    
    if data_datetime < hoje:
        print("ERRO! A data deve ser igual ou maior que a de hoje.")
        return False
    
    return True
    

def validar_crm(crm):
    if crm == "":
        print("ERRO! Campo vazio.")
        return False
    
    padrao = r"^\d{6}/[A-Z]{2}$"

    if not re.fullmatch(padrao, crm):
        print("ERRO! Formato incorreto.")
        print("Ex.: 123456/PE")
        return False

    return True
    

def validar_cpf(cpf):
    if cpf == "":
        print("ERRO! Campo vazio.")
        return False
    
    if cpf.isdigit() == False:
        print("ERRO! Digite apenas números inteiros.")
        return False
    
    padrao = r"^\d{11}$"

    if not re.fullmatch(padrao, cpf):
        print("ERRO! Formato incorreto.")
        print("Ex.: 12345678900")
        return False

    return True


def validar_email(email):
    if email == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^[a-z0-9\._-]+@[a-z0-9]+\.[a-z]{2,}\.?([a-z]{2,})?"

    if not re.fullmatch(padrao, email):
        print("ERRO! Formato incorreto.")
        return False
    
    return True


def validar_numero(numero):
    if numero == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^\(\d{2}\)\d{5}-\d{4}$"

    if not re.fullmatch(padrao, numero):
        print("ERRO! Formato incorreto.")
        return False

    return True


def validar_especialidade(especialidade):
    if especialidade == "":
        print("ERRO! Campo em branco.")
        return False

    if not especialidade.replace(" ", "").isalpha():
        print("ERRO! Digite apenas letras.")
        return False

    return True


def validar_sexo(sexo):
    if sexo == "":
        print("ERRO! Campo em branco.")
        return False
    
    if sexo[0] not in "MF":
        print("ERRO! Sexo inválido.")
        return False
    
    return True


def validar_queixa(queixa):
    if queixa == "":
        print("ERRO! Campo em branco.")
        return False

    return True