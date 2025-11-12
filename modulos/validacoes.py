from datetime import datetime
import re

def validar_nome(nome):
    # input com .strip()
    if nome == "":
        print("ERRO! Campo em branco.")
        return False
    
    return True


def validar_idade(idade):
    # input com replace(" ", "")
    if idade == "":
        print("ERRO! Campo vazio.")
        return False
    
    try:
        int(idade)
        return True
    except ValueError:
        print("ERRO! Digite apenas números inteiros.")
        return False


def validar_data_nascimento(data):
    # input com replace(" ", "")
    if data == "":
        print("ERRO! Campo vazio")
        return False
    
    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        print("ERRO! Formato incorreto.")
        print("Ex.: 19/02/2017")
        return False
    
    hoje = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"

    if data > hoje:
        print("ERRO! Data inválida")
        print("A data deve ser igual ou menor que a de hoje.")
        return False
    
    return True


def validar_data_consulta(data):
    # input com replace(" ", "")
    if data == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        print("ERRO! Formato incorreto.")
        print("Ex.: 01/01/2031")
        return False
    
    hoje = f"{datetime.now().day}/{datetime.now().month}/{datetime.now().year}"

    if data < hoje:
        print("ERRO! Data inválida")
        print("A data deve ser igual ou maior que a de hoje.")
        return False
    
    return True
    

def validar_crm(crm):
    # input com replace(" ", "")
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
    # input com replace(" ", "")
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
    # input com replace(" ","")
    if email == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2}$"

    if not re.fullmatch(padrao, email):
        print("ERRO! Formato incorreto.")
        print("Ex.: email@gmail.com")
        return False
    
    return True


def validar_numero(numero):
    # input replace(" ", "")
    if numero == "":
        print("ERRO! Campo vazio.")
        return False

    padrao = r"^\(\d{2}\)\d{5}-\d{4}$"

    if not re.fullmatch(padrao, numero):
        print("ERRO! Formato incorreto.")
        print("Ex.: (81)99999-9999")
        return False

    return True