import bank
import people
import time
import getpass
import msvcrt
from searches import check_key,clear_screen,system_name
from prettytable import PrettyTable

registry={}
created_accounts = {}

def get_choice():
    while True:
        choice = input('Digite o número desejado: ').strip()
        if choice.isdigit():
            return int(choice)
        else:
            print('Por favor, digite um número válido.')




def main_menu():
    menu_options = {1:"Fazer cadastro",2:"Criar Conta",3:"Abra sua conta",4:"Sair"}
    choice = 0  
    while choice!=len(menu_options):
        clear_screen()
        print('+'+'-'*38+'+')
        print("|           Menu Principal             |")
        print('+'+'-'*38+'+')
        menu_principal = PrettyTable(['      OPÇÃO      ', '       ITEM     '])
        menu_principal.align['OPÇÃO'] = 'c'
        menu_principal.align['ITEM'] ='l'
        menu_principal.add_row(['1','Cadastrar'])
        menu_principal.add_row(['2','Criar Conta'])
        menu_principal.add_row(['3','Acessar conta'])
        menu_principal.add_row(['4','Sair'])
        print(menu_principal)
        choice = get_choice()
        if choice == 1:
            people.new_registration(registry)
        elif choice == 2:
            people.create_account(registry,created_accounts)
        elif choice == 3:
            cpf,lookup = check_key(created_accounts,"account")
            if not cpf:
                print('CPF não possui conta')
                time.sleep(3)
            else:
                bank_menu(cpf,lookup)
                time.sleep(3)
        elif choice == 4:
            print('Saindo...')

def bank_menu(cpf, lookup):
    bank_options = {1: "Sacar", 2: "Depositar", 3: "Extrato", 4: "Sair"}
    choice = 0
    if 'password' not in lookup or not lookup['password']:
        print('Seja bem-vindo(a), essa é a sua primeira vez acessando o CESM Bank')
        password_new = get_password("Digite sua senha: ")
        password_confirmation = get_password("Confirme sua senha: ")
        while password_new != password_confirmation:
            print('As senhas digitadas não são iguais')
            password_new = get_password("Digite sua senha: ")
            print('Confirme sua senha')
            password_confirmation = get_password("Confirme sua senha: ")
        if password_confirmation == password_new:
            lookup['password'] = password_new
            print('Senha salva com sucesso')
            print('O sistema irá voltar para o Menu principal para liberar o acesso')
            time.sleep(3)

    else:
        password_new = get_password("Digite sua senha: ")
        if password_new == lookup['password']:
            while choice != len(bank_options):
                clear_screen()
                print('+'+'-'*38+'+')
                print("|              CESM Bank               |")
                print('+'+'-'*38+'+')
                first_name = lookup['name'].split()
                account_data = lookup
                print('+'+'-'*38+'+')
                print(f'| Olá, {first_name[0]}'.ljust(39) + '|')
                print('| Conta' + f'{lookup["account"]}'.rjust(32) + '|')
                menu_principal = PrettyTable(['      OPÇÃO      ', '       ITEM     '])
                menu_principal.align['OPÇÃO'] = 'c'
                menu_principal.align['ITEM'] ='l'
                menu_principal.add_row(['1','Sacar'])
                menu_principal.add_row(['2','Depositar'])
                menu_principal.add_row(['3','Extrato'])
                menu_principal.add_row(['4','Sair'])
                print(menu_principal)
                choice = get_choice()

                if choice == 1:
                    bank.withdrawal(account_data)
                elif choice == 2:
                    bank.deposit(account_data)
                elif choice == 3:
                    bank.statement(account_data)
                elif choice == 4:
                    print('Saindo...')

def get_password(prompt="Digite sua senha: "):
    os_system = system_name()
    if os_system == 'posix':  # Linux ou macOS
        senha = getpass.getpass(prompt)
        return senha
    elif os_system == 'nt':  # Windows
        print(prompt, end="", flush=True)
        senha = b""
        while True:
            char = msvcrt.getch()
            if char == b'\r' or char == b'\n':
                print()
                break
            elif char == b'\x08':  # Backspace
                if senha:
                    senha = senha[:-1]
                    print("\b \b", end="", flush=True)
            else:
                senha += char
                print("*", end="", flush=True)
    return senha.decode('utf-8')
   


main_menu()
