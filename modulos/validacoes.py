from datetime import datetime
from . import mensagens
import re

def validar_opcao(opcao):
    if opcao.isdigit() == False:
        mensagens.erro("ERRO! Digite apenas números.")
        return False
    
    return True


def validar_id(id):
    if id == "":
        mensagens.erro("ERRO! Campo em branco.")
        return False

    try:
        int(id)
    except ValueError:
        mensagens.erro("ERRO! Digite apenas números inteiros.")
        return False
    
    if int(id) <= 0:
        mensagens.erro("ERRO! Id menor ou igual a zero.")
        return False
    

def validar_nome(nome):
    if nome == "":
        mensagens.erro("ERRO! Campo em branco.")
        return False

    if not nome.replace(" ", "").isalpha():
        mensagens.erro("ERRO! Digite apenas letras.")
        return False

    return True


def validar_data_nascimento(data):
    if data == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False
    
    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        mensagens.erro("ERRO! Formato incorreto.")
        return False
    
    hoje = datetime.now().date()
    
    try:
        data_datetime = datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        mensagens.erro("ERRO! Data inválida.")
        return False

    if data_datetime > hoje:
        mensagens.erro("ERRO! A data deve ser igual ou menor que a de hoje.")
        return False
    
    return True


def validar_data_consulta(data):
    if data == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False

    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.fullmatch(padrao, data):
        mensagens.erro("ERRO! Formato incorreto.")
        return False
    
    hoje = datetime.now().date()
    try:
        data_datetime = datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        mensagens.erro("ERRO! Data inválida.")
        return False
    
    if data_datetime < hoje:
        mensagens.erro("ERRO! A data deve ser igual ou maior que a de hoje.")
        return False
    
    return True
    

def validar_crm(crm):
    if crm == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False
    
    padrao = r"^\d{6}/[A-Z]{2}$"

    if not re.fullmatch(padrao, crm):
        mensagens.erro("ERRO! Formato incorreto.")
        return False

    return True
    

def validar_cpf(cpf):
    if cpf == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False
    
    if cpf.isdigit() == False:
        mensagens.erro("ERRO! Digite apenas números inteiros.")
        return False
    
    padrao = r"^\d{11}$"

    if not re.fullmatch(padrao, cpf):
        mensagens.erro("ERRO! Formato incorreto.")
        return False

    return True


def validar_email(email):
    if email == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False

    padrao = r"^[a-z0-9\._-]+@[a-z0-9]+\.[a-z]{2,}\.?([a-z]{2,})?$"
    
    if not re.fullmatch(padrao, email):
        mensagens.erro("ERRO! Formato incorreto.")
        return False
    
    return True


def validar_numero(numero):
    if numero == "":
        mensagens.erro("ERRO! Campo vazio.")
        return False

    padrao = r"^\(\d{2}\)\d{5}-\d{4}$"

    if not re.fullmatch(padrao, numero):
        mensagens.erro("ERRO! Formato incorreto.")
        return False

    return True


def validar_especialidade(especialidade):
    if especialidade == "":
        mensagens.erro("ERRO! Campo em branco.")
        return False

    if not especialidade.replace(" ", "").isalpha():
        mensagens.erro("ERRO! Digite apenas letras.")
        return False

    return True


def validar_sexo(sexo):
    if sexo == "":
        mensagens.erro("ERRO! Campo em branco.")
        return False
    
    if sexo[0] not in "MF":
        mensagens.erro("ERRO! Sexo inválido.")
        return False
    
    return True


def validar_queixa(queixa):
    if queixa == "":
        mensagens.erro("ERRO! Campo em branco.")
        return False

    return True