import time
import sql_operations
from os import name,system
from datetime import datetime

def search_cpf():
    while True:
        cpf_entered = input('Digite seu CPF (somente números): ').strip()
        if verification_cpf(cpf_entered):
            lookup = sql_operations.search_cpf_database(cpf_entered)
            return cpf_entered, lookup

def check_key(search_type):
     while True:
        if search_type == 'registry':
            cpf_entered = input('Digite seu CPF (somente números): ').strip()
            if verification_cpf(cpf_entered):
                if cpf_entered is not 'vazio' :
                    lookup = sql_operations.search_cpf_database(cpf_entered)
                    return cpf_entered, lookup
                else:
                    print('CPF não cadastrado')
                    time.sleep(3)
                    return False, None
        elif search_type == 'account':
            cpf_entered = input("Digite seu CPF (somente números): ").strip()
            if verification_cpf(cpf_entered):
                lookup = sql_operations.select_account_database(cpf_entered)
                if lookup:
                    return cpf_entered, lookup
                else:
                    return False, None


    

def verification_cpf(cpf):
    while not (cpf.isnumeric() and len(cpf) == 11):
        print('CPF inválido. Certifique-se de digitar exatamente 11 números.')
        cpf = input('Digite seu CPF (somente números): ').strip()
    return True

def verification_name(name):
    while not name.replace(" ", "").isalpha():
        print('Nome inválido. Certifique-se de usar apenas letras.')
        name = input('Digite seu nome (apenas letras): ')
    return name

def verify_birth_date(date):
    while True:
        if not all(char.isdigit() or char == '/' for char in date):
            print('Data de nascimento inválida. Certifique-se de usar o formato dd/MM/yyyy.')
            date = input('Digite a data de nascimento (dd/MM/yyyy): ')
        else:
            try:
                
                datetime.strptime(date, '%d/%m/%Y')
                return date
            except ValueError:
                print('Data de nascimento inválida. Certifique-se de usar o formato dd/MM/yyyy.')
                date = input('Digite a data de nascimento (dd/MM/yyyy): ')


def find_account(accounts, account_number):
    for account in accounts:
        if account["account"] == account_number:
            return account
    return None

def clear_screen():
    os_name = name

    if os_name == 'posix':  # Linux ou macOS
        system('clear')
    elif os_name == 'nt':  # Windows
        system('cls')
    else:
        
        print('Não foi possível limpar a tela. Por favor, faça isso manualmente.')

def system_name():
    os_name = name
    return os_name