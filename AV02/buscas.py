import os

def pesquisar_cpf(cadastro):
    while True:
        cpf_digitado = input("Digite seu CPF (somente números): ").strip()
        if verificacao_cpf(cpf_digitado):
            busca = cadastro.get(cpf_digitado)
            return cpf_digitado, busca

def verificacao_cpf(cpf):
    while not (cpf.isnumeric() and len(cpf) == 11):
        print("CPF inválido. Certifique-se de digitar exatamente 11 números.")
        cpf = input("Digite seu CPF (somente números): ").strip()
    
    print("CPF válido:", cpf)
    return True

def verificar_nome(nome):
    while not nome.replace(" ", "").isalpha():
        print("Nome inválido. Certifique-se de usar apenas letras.")
        nome = input("Digite seu nome (apenas letras): ")
    
    print("Nome válido:", nome)
    return nome

def verificar_data_nascimento(data):
    while True:
        try:
            from datetime import datetime
            datetime.strptime(data, '%d/%m/%Y')
            print("Data de nascimento válida:", data)
            return data
        except ValueError:
            print("Data de nascimento inválida. Certifique-se de usar o formato dd/MM/yyyy.")
            data = input("Digite a data de nascimento (dd/MM/yyyy): ")

def verificar_saldo(saldo):
    while True:
        try:
            saldo_float = float(saldo)
            print("Saldo válido:", saldo_float)
            return saldo_float
        except ValueError:
            print("Saldo inválido. Certifique-se de usar apenas números.")
            saldo = input("Digite seu saldo (apenas números): ")
