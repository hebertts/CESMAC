import searches
import time
from datetime import datetime
current_date = datetime.now()
accounts=[0]

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



def new_registration(registry):
    cpf_entered, loolup = searches.search_cpf(registry)
    if not cpf_entered: 
        print('Cadastro não poderá ser efetuado.')
        return
    elif loolup:
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
        birth_date_entered  = searches.verify_birth_date(birth_date_entered )
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
                registry[cpf_entered] = {
                    "name": name_entered,
                    "birth_date": birth_date_entered,
                    "salary": salary_entered,
                    "account":[]
                }
                print('-'*30)
                input('\n\nCadastro efetuado com sucesso\nPressione Enter para continuar_')
        else:
            print("\n\nVocê é menor de idade, infelizmente o cadastro não será efetuado.")
            time.sleep(3)
            
def create_account(registry, created_account):
    cpf, lookup = searches.check_key(registry, "registry")
    if not cpf:
        print('A conta não pode ser criada')
        time.sleep(3)
    elif not lookup:
        print("CPF não possui cadastro. Cadastre-se primeiro.")
        time.sleep(3)
    elif cpf in created_account:
        print('CPF já possui conta')
        time.sleep(3)
    else:
        searches.clear_screen()
        print('◌----------------◉-----------> ')
        print('Criação da conta'.rjust(30))
        print('-'*30)
        agency = 0
        print('''Agências disponíveis:
[1] - 01
[2] - 02
[3] - 03''')
        agency = get_choice()
        str(agency).zfill(2)
        name = lookup['name']
        last_account = max(accounts) + 1
        accounts.append(last_account)
        account = str(last_account).zfill(4)
        account = account[:3] + '-' + account[3:]
        
        created_account[cpf] = {
            "name": name,
            "agency": agency,
            "account": account,
            "balance": 0.0,
            "password":"",
            "statement": []
        }
        print('-'*30)
        lookup["account"] = {"agency": agency,
            "account": account} 
        input(f"\n\nConta: {account} cadastrada com sucesso.\nPressione Enter para continuar_")

def verify_number(number):
    while True:
        if number.replace(",", "").isdigit() or (number.count(",") == 1 and number.replace(",", "").isdigit()):
            if "," in number:
                number = number.replace(",", ".")
            number = float(number)
            return number
        else:
            return None