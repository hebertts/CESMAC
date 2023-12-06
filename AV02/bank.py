from datetime import datetime
import time
from searches import clear_screen
import sql_operations
MAX_WITHDRAWAL_AMOUNT  = 1000
WITHDRAWAL_LIMIT  = 5
currente_date = datetime.now()


def deposit(account):
    clear_screen()
    print("==================== Depósito ===================")
    deposit_value = input("Digite o valor do depósito (apenas números inteiros e separação por vírgula para centavos): ")
    value = verify_number(deposit_value)
    print()
    if value == None:
        print('Formato do número digitado não é aceito')
        time.sleep(2)
    elif value > 0:
        current_balance = float(account[3])    
        new_balance = current_balance + value
        date_transation =  currente_date.strftime('%Y-%m-%d %H:%M:%S')
        sql_operations.insert_statement_database(account[1],date_transation,"Depósito",value,new_balance)
        value_br = format_br(value)
        print(f"\n\nValor  de {value_br}, foi depositado com sucesso.")
        input("Pressione enter para continuar_")
    else: 
        print('Apenas números maiores que 0')
        time.sleep(2)


def withdrawal(account):
    clear_screen()
    print("===================== Saque ====================")
    balance_account = float(account[3])
    date_transation =  currente_date.strftime('%Y-%m-%d')
    withdrawals_made = sql_operations.count_withdrawal(account[1],date_transation)
    if withdrawals_made >= WITHDRAWAL_LIMIT:
        input("Você atingiu o limite de saque.\nPrssione enter para continuar_")
        time.sleep(3)
    elif balance_account  <= 0:
        print("Sem saldo na conta")
        input("Pressione enter para continuar_")
    else:
        value = input("Digite o valor do saque (apenas números inteiros e separação por vírgula para centavos): ")
        value = verify_number(value)
        if value is None:
            print('formato do número não é aceito')
            time.sleep(3)
        elif value > 0 and value <= balance_account and value <= MAX_WITHDRAWAL_AMOUNT:
            date_transation =  currente_date.strftime('%Y-%m-%d %H:%M:%S')
            new_balance = balance_account-value
            sql_operations.insert_statement_database(account[1],date_transation,"Saque",value,new_balance)
            print(f"\n\nSaque de {value} realizado com sucesso.")
            input("Pressione enter para continuar_")
        else:
            print("\n\nValor do saque é inválido ou superior ao saldo disponível.")
            input("Pressione enter para continuar_")
def credit_account(rent,statement):
    fator = 3.5
    credito = (rent + statement) * fator
    return credito
def upper_limit_credit(account):
    print("==================== Crédito ===================")
    account_client = account[1]
    rent = float(account[5])
    limit_credit = float(account[4])
    statement_value = 0
    statement_account = sql_operations.search_statement_database(account[1])
    if statement_account == 'vazio':
        print('Sua conta não possui nenhuma atividade.')
        time.sleep(3)
        return
    if statement_account != 'vazio':
        statement_value = sum(
            float(transaction['value_statement']) 
            for transaction in statement_account['statement'] 
            if 'depósito' in transaction['Typo'].lower()
        )
        
        new_credit = credit_account(rent, statement_value)
        
        if new_credit == limit_credit:
            print('Você precisa movimentar mais para aumentar mais o seu limite.')
            time.sleep(3)
        elif new_credit != limit_credit:
            diff = new_credit - limit_credit
            diff_br = format_br(float(diff))
            new_credit_br = format_br(float(new_credit))
            sql_operations.update_limit(new_credit,account_client)
            input(f'Parabéns! seu novo limite é R$ {new_credit_br}. Aumentamos R$ {diff_br}.\nPressione enter para continuar_')
from operator import itemgetter

def price(n,value):
    taxa_n = 0.1 / n
    pmt = (value * taxa_n)/(1 - (1+taxa_n)**-n)
    return pmt

def loan(account):
    print("=================== Empréstimo ===================")
    account_client = account[1]
    limit = account[4]
    paid_loan = 0
    unpaid_loan = 0
    using_limit = sql_operations.search_loan_database(account_client)

    if using_limit == 'vazio' or not using_limit['installments']:
        # Caso a pessoa nunca tenha feito um empréstimo
        print(f'Seu limite é {limit}')
        while True:
            try:
                value = float(input('Digite o valor desejado do empréstimo: '))
                break
            except ValueError:
                print('Valor inválido. Por favor, insira um valor numérico.')

        while True:
            try:
                period = int(input('Digite quantas parcelas deseja: '))
                break
            except ValueError:
                print('Número inválido de parcelas. Por favor, insira um número inteiro.')
        if limit >= value:
            value_payment = price(period, value)
            date_loan = currente_date.strftime('%Y-%m-%d')
            sql_operations.insert_loan_database(value, date_loan, period, account_client, value_payment)
            
        else:
            print('Parece que você tentou pedir um empréstimo maior que seu limite atual')
            print('Tente novamente mais tarde')
            time.sleep(3)
        return

    # Verificando empréstimos existentes
    for loan in using_limit['installments']:
        if int(loan['status_loan']) == 1:
            paid_loan += 1
        if int(loan['status_loan']) == 0:
            unpaid_loan += 1

    if limit <= 0:
        print('Você não possui limite para empréstimo')
        time.sleep(2)
    elif paid_loan <= unpaid_loan:
        print('Você já possui empréstimo na conta. Quitá-lo primeiro para solicitar mais.')
        time.sleep(3)
    elif limit > 0 and unpaid_loan == 0:
        # Permitir novo empréstimo se não houver empréstimos pendentes
        while True:
            try:
                value = float(input('Digite o valor desejado do empréstimo: '))
                break
            except ValueError:
                print('Valor inválido. Por favor, insira um valor numérico.')

        while True:
            try:
                period = int(input('Digite quantas parcelas deseja: '))
                break
            except ValueError:
                print('Número inválido de parcelas. Por favor, insira um número inteiro.')

        value_payment = price(period, value)
        date_loan = currente_date.strftime('%Y-%m-%d')
        sql_operations.insert_loan_database(value, date_loan, period, account_client, value_payment)
        
def pay_loan(account,cpf):
    account_client = account[1]
    balance_account = float(account[3])
    

    loan_data = sql_operations.search_loan_database(account_client)
    
    if loan_data == 'vazio':
        print('Nenhuma parcela encontrada para ser paga')
        time.sleep(2)
    else:
        count = 0
        value_payment = 0.0
        unpaid_installments = []

        for portion in loan_data['installments']:
            if portion['status'] == 0:
                count += 1
                value = (float(portion['installments_value']))
                value_payment = value_payment + value
                
                unpaid_installments.append(portion)

        if count == 0:
            print('Todas as parcelas já foram pagas.')
        else:
            value_payment = format_br(value_payment)
            print(f'Você tem {count} parcelas a pagar, totalizando o valor de R$ {value_payment}')
            while True:
                try:
                    value_entered = int(input('Quantas parcelas deseja pagar? '))
                    if value_entered <= 0:
                        print('Por favor, insira um número válido de parcelas.')
                        continue
                    break
                except ValueError:
                     print('Número inválido de parcelas. Por favor, insira um número inteiro.')

            while value_entered > count:
                print('O número de parcelas é maior que as parcelas pendentes')
                value_entered = int(input(f'Você tem {count} parcelas pendentes, totalizando R$ {value_payment}. Quantas parcelas deseja pagar? '))

            count = 0
            value_total = 0

            for portion in unpaid_installments:
                if count < value_entered and portion['status'] == 0 and balance_account >= portion['installments_value']:
                    count += 1
                    value_total += portion['installments_value']
                    sql_operations.update_loan_installments(account_client, portion['id_loan'], 1, portion['id_installments'], value_total)
            new_balance = float(balance_account) - float(value_total)
      
            date_transation =  currente_date.strftime('%Y-%m-%d %H:%M:%S')
            sql_operations.insert_statement_database(account_client,date_transation,"Parcela paga",value_total,new_balance)
            print(f'Foram pagas um total de {count} parcelas com o saldo disponível na conta.')
            time.sleep(3)




        
def statement(account):
    try:
        clear_screen()
        balance_br = f"{float(account[3]):_.2f}"
        balance_br = balance_br.replace('.', ',').replace('_', '.')
        print("======================== Extrato =======================")
        print(f"Extrato da conta {account[1]} - Saldo: R$ {balance_br}")

        statement_account = sql_operations.search_statement_database(account[1])
        sorted_statement = sorted(statement_account['statement'], key=itemgetter('Transaction_date'))
        current_period = None

        entries_period = 0
        exits_period = 0

        for transaction in sorted_statement:
            if transaction['Transaction_date'].date() != current_period:
                if current_period is not None:
                    print(f"\n{'Total de Entradas:':<20} R$ {entries_period:.2f}")
                    print(f"{'Total de Saidas:':<20} R$ {exits_period:.2f}")
                
                print(f"\nPeríodo: {(transaction['Transaction_date']).strftime('%d/%m/%Y')}")
                current_period = transaction['Transaction_date'].date()
                entries_period = 0
                exits_period = 0
                
            if 'depósito' in transaction['Typo'].lower():
                entries_period += float(transaction['value_statement'])
            elif 'saque' in transaction['Typo'].lower() or 'parcela paga' in transaction['Typo'].lower() :
                exits_period += float(transaction['value_statement'])
            
            amount_br = f"{float(transaction['value_statement']):_.2f}"
            amount_br = amount_br.replace('.', ',').replace('_', '.')
            print(f"{transaction['Typo']:<30} R$ {amount_br}")

        # Imprimir os totais finais de entradas e saídas
        print(f"\n{'Total de Entradas:':<20} R$ {entries_period:.2f}")
        print(f"{'Total de Saidas:':<18} - R$ {exits_period:.2f}")

        print("=====================================================")
        input("\nPressione enter para continuar_")

    
    except Exception as e:
        print(f"Erro ao imprimir extrato: {e}")
        time.sleep(2)

def verify_number(number):
    while True:
        if number.replace(",", "").isdigit() or (number.count(",") == 1 and number.replace(",", "").isdigit()):
            if "," in number:
                number = number.replace(",", ".")
            number = float(number)
            return number
        else:
            return None
def format_br(value):
    amount_br = f"{float(value):_.2f}"
    amount_br = amount_br.replace('.', ',').replace('_', '.')
    return amount_br