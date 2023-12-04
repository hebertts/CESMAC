from datetime import datetime
import time
from searches import clear_screen
import sql_operations
MAX_WITHDRAWAL_AMOUNT  = 1000
WITHDRAWAL_LIMIT  = 5
currente_date = datetime.now()




def deposit(account):
    print (account)
    deposit_value = input("Digite o valor do depósito (apenas números inteiros e separação por vírgula para centavos): ")
    value = verify_number(deposit_value)
    print()
    if value == None:
        print('Formato do número digitado não é aceito')
    elif value > 0:
        current_balance = float(account[3])    
        new_balance = current_balance + value
        date_transation =  currente_date.strftime('%Y-%m-%d %H:%M:%S')
        sql_operations.insert_statement_database(account[1],date_transation,"Depósito",value,new_balance)
        print(f"\n\nValor  de {value:.2f}, foi depositado com sucesso.")
        input("Pressione enter para continuar_")
    else: 
        print('Apenas números maiores que 0')


def withdrawal(account):
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


from operator import itemgetter

def statement(account):
    try:
        balance_br = f"{float(account[3]):_.2f}"
        balance_br = balance_br.replace('.', ',').replace('_', '.')
        print("======================== Extrato =======================")
        print(f"Extrato da conta {account[1]} - Saldo: R$ {balance_br}")

        statement_account = sql_operations.search_statement_database(account[1])
        sorted_statement = sorted(statement_account['statement'], key=itemgetter('Transaction_date'))
        current_period = None

        entradas_periodo = 0
        saidas_periodo = 0

        for transaction in sorted_statement:
            if transaction['Transaction_date'].date() != current_period:
                if current_period is not None:
                    print(f"\n{'Total de Entradas:':<20} R$ {entradas_periodo:.2f}")
                    print(f"{'Total de Saidas:':<20} R$ {saidas_periodo:.2f}")
                
                print(f"\nPeríodo: {(transaction['Transaction_date']).strftime('%d/%M/%Y')}")
                current_period = transaction['Transaction_date'].date()
                entradas_periodo = 0
                saidas_periodo = 0
                
            if 'depósito' in transaction['Descricao'].lower():
                entradas_periodo += float(transaction['value_statement'])
            elif 'saque' in transaction['Descricao'].lower():
                saidas_periodo += float(transaction['value_statement'])
            
            amount_br = f"{float(transaction['value_statement']):_.2f}"
            amount_br = amount_br.replace('.', ',').replace('_', '.')
            print(f"{transaction['Descricao']:<30} R$ {amount_br}")

        # Imprimir os totais finais de entradas e saídas
        print(f"\n{'Total de Entradas:':<20} R$ {entradas_periodo:.2f}")
        print(f"{'Total de Saidas:':<20} - R$ {saidas_periodo:.2f}")

        print("=====================================================")
        input("\nPressione enter para continuar_")

    
    except Exception as e:
        print(f"Erro ao imprimir extrato: {e}")

def verify_number(number):
    while True:
        if number.replace(",", "").isdigit() or (number.count(",") == 1 and number.replace(",", "").isdigit()):
            if "," in number:
                number = number.replace(",", ".")
            number = float(number)
            return number
        else:
            return None
       