import bank
import people
import time
import getpass
import sql_operations
from hashlib import sha256
from searches import check_key,clear_screen,system_name
from prettytable import PrettyTable
from datetime import datetime

currente_date  =datetime.now()


def criptografar_senha(password):
    password_crip = sha256(password.encode()).hexdigest()

    return password_crip



def get_choice():
    while True:
        choice = input('Digite o número desejado: ').strip()
        if choice.isdigit():
            return int(choice)
        else:
            print('Por favor, digite um número válido.')
            time.sleep(1)




def main_menu():
    choice = 0  
    while choice!=4:
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
            people.new_registration()
        elif choice == 2:
            people.create_account()
        elif choice == 3:
            cpf,lookup = check_key("account")
            if lookup == 'vazio':
                print('CPF não possui conta')
                time.sleep(3)
            else:
                bank_menu(cpf,lookup)
                time.sleep(3)
          
        elif choice == 4:
            print('Saindo...')
            sql_operations.close_sql()

def bank_menu(cpf, lookup):
    choice = 0
 
    if 'newpass'  in lookup[2]:
        print('Seja bem-vindo(a), essa é a sua primeira vez acessando o CESM Bank')
        password_new = get_password("Digite sua senha: ")
        password_confirmation = get_password("Confirme sua senha: ")
        while password_new != password_confirmation:
            clear_screen()
            print('As senhas digitadas não são iguais')
            password_new = get_password("Digite sua senha: ")
            password_confirmation = get_password("Confirme sua senha: ")
        if password_confirmation == password_new:
            password_new = criptografar_senha(password_new)
            sql_operations.update_password(password_new,cpf)
            print('Senha salva com sucesso')
            print('O sistema irá voltar para o Menu principal para liberar o acesso')
            time.sleep(3)

    else:
        password_new = get_password("Digite sua senha: ")
        password_new = criptografar_senha(password_new)
        if password_new == lookup[2]:
            while choice != 8:
                lookup = sql_operations.select_account_database(cpf) 
                clear_screen()
           
                print('+'+'-'*42+'+')
                print("|              CESM Bank                   |")
                print('+'+'-'*42+'+')
                first_name = lookup[0].split()
                account_data = lookup
                print('+'+'-'*42+'+')
                print(f'| Olá, {first_name[0]}'.ljust(43) + '|')
                print('| Conta' + f'{lookup[1]}'.rjust(36) + '|')
                menu_principal = PrettyTable(['      OPÇÃO      ', '       ITEM     '])
                menu_principal.align['OPÇÃO'] = 'c'
                menu_principal.align['ITEM'] ='l'
                menu_principal.add_row(['1','Sacar'])
                menu_principal.add_row(['2','Depositar'])
                menu_principal.add_row(['3','Extrato'])
                menu_principal.add_row(['4','Crédito'])
                menu_principal.add_row(['5','Empréstimo'])
                menu_principal.add_row(['6','Pagar Parcela'])
                menu_principal.add_row(['7','Informações pessoais'])
                menu_principal.add_row(['8','Sair'])
                print(menu_principal)
                choice = get_choice()
                if choice == 1:
                    bank.withdrawal(account_data)
                elif choice == 2:
                    bank.deposit(account_data)
                elif choice == 3:
                    bank.statement(account_data)
                elif choice == 7:
                        clear_screen()
                        result = sql_operations.search_client_database(cpf)
                        print(f'Nome: {result[0]}')
                        date_string = result[1]
                        
                        formatted_date = date_string.strftime('%d/%m/%Y')
                        print(f'Data de Nascimento: {formatted_date}')
                        salary_br = format(float(result[2]))
                        print(f'Salário: {salary_br}')
                        dependent = 'Sim' if result[3] == 1 else "Não" 
                        print(f'Dependente: {dependent}')
                        print(f'Email: {result[4]}')
                        saldo_br = bank.format_br(result[5])
                        print(f'Saldo na conta: R$ {saldo_br}')
                        limit_credit_br = bank.format_br(result[6])
                        print(f'Limite de empréstimo até R$ {limit_credit_br}')
                        limmit_used = bank.format_br(result[7])
                        print(f'Empréstimo recente: {limmit_used}') if float(result[7]) > 0.0 else None
                        input('Pressione Enter para continuar_')
                elif choice == 4:
                    bank.upper_limit_credit(account_data)
                elif choice == 5:
                    bank.loan(account_data)
                elif choice == 6:
                    bank.pay_loan(account_data,cpf)

                elif choice == 8:
                    print('Saindo...')
        else:
            print('senha errada')
            time.sleep(2)

def get_password(prompt="Digite sua senha: "):
    os_system = system_name()
    if os_system == 'posix':  # Linux ou macOS
        senha = getpass.getpass(prompt)
        return senha
    elif os_system == 'nt':  # Windows
        import msvcrt
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
