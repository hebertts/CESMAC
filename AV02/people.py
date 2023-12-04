import searches
import time
import sql_operations
from datetime import datetime
current_date = datetime.now()
import random

def get_choice():
    choice = int(input('Digite o número desejado: '))
    while True:
        try:
            if  1 <= choice <= 3:  
                return choice
            else:
                choice = int(input('Por favor, digite um número válido (1-3): '))
                if  1 <= choice <= 3:  
                    return choice
            
        except ValueError:
                choice = int(input('Por favor, digite um número válido (1-3): '))



def new_registration():
    cpf_entered, loolup = searches.search_cpf()
    if not cpf_entered: 
        print('Cadastro não poderá ser efetuado.')
        return
    elif loolup !=  'vazio':
        print('CPF existente')
        time.sleep(3)
    else:
        searches.clear_screen()
        print('◉----------------◌-----------> ')
        print(' Dados Pessoais'.ljust(30))
        print('-'*30)
        name_entered = input("Digite seu nome completo: ")
        searches.verification_name(name_entered)
        birth_date_entered  = input("Digite a data de nascimento (dd/MM/yyyy): ")
        birth_date_entered  = searches.verify_birth_date(birth_date_entered)
        birth_date_entered  = datetime.strptime(birth_date_entered , '%d/%m/%Y')
        
        age_difference = current_date.year - birth_date_entered.year
        if birth_date_entered.month < birth_date_entered.month or (birth_date_entered.month == birth_date_entered.month and birth_date_entered.day < birth_date_entered.day):
            age_difference -= 1
               
        if age_difference >= 18:
            salary_entered = input('Digite a sua renda mensal: ')
            salary_entered = verify_number(salary_entered)
            if salary_entered is None:
                print('\n\nValor digitado é inválido, tente novamente')
                time.sleep(2)
            else:
                email = input("Digite o seu email: ")
                dependent = input("Você tem dependentes('S' ou 'N')? ")
                dependent = 1 if dependent == 'S' else  0
                birth_date_entered = birth_date_entered.strftime('%Y-%m-%d')
                sql_operations.insert_registry(cpf_entered,name_entered,birth_date_entered,salary_entered,dependent,email)
                print('-'*30)
                input('\n\nCadastro efetuado com sucesso\nPressione Enter para continuar_')
        else:
            print("\n\nVocê é menor de idade, infelizmente o cadastro não será efetuado.")
            time.sleep(3)
            
def create_account():
    cpf, lookup = searches.check_key("account")
    if lookup[1] == None:
        searches.clear_screen()
        print('◌----------------◉-----------> ')
        print('Criação da conta'.rjust(30))
        print('-'*30)
        account = random.randint(1, 99999)
        account = str(min(account,99999))
        account = account.zfill(5)
        account = account[:4] + '-' + account[4:]
        print(account)
        result = sql_operations.search_account_databese(account)
        while result != 'vazio':
            account  = [random.randint(1, 100) for _ in range(4)]
            account = str(account)
            account = account[:3] + '-' + account[3:]
            result = sql_operations.search_account_databese(account)   
        if result =='vazio':  
            creat_account  = datetime.strftime(current_date , '%Y-%m-%d')
            sql_operations.insert_accounts_database(account,0,creat_account,cpf,f'newpass{account}')
            print('-'*30)
            input(f"\n\nConta: {account} cadastrada com sucesso.\nPressione Enter para continuar_")

    elif lookup == 'vazio': 
        print('A conta não pode ser criada, CPF não cadastrado')
        
        time.sleep(3)
    else:
        print("CPF já possui uma conta.")
        time.sleep(3)
    print(lookup)

def verify_number(number):
    while True:
        if number.replace(",", "").isdigit() or (number.count(",") == 1 and number.replace(",", "").isdigit()):
            if "," in number:
                number = number.replace(",", ".")
            number = float(number)
            return number
        else:
            return None