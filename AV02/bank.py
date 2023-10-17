from datetime import datetime
import time
from searches import clear_screen
MAX_WITHDRAWAL_AMOUNT  = 1000
WITHDRAWAL_LIMIT  = 5
currente_date = datetime.now()
currente_date = currente_date.strftime('%d/%m/%Y')



def deposit(account):
    deposit_value = input("Digite o valor do depósito (apenas números inteiros e separação por vírgula para centavos): ")
    value = verify_number(deposit_value)
    print()
    if value == None:
        print('Formato do número digitado não é aceito')
    elif value > 0:
        current_balance = account.get("balance", 0) 
        new_balance = current_balance + value
        account["balance"] = new_balance
        transaction = {
                "description": "Depósito",
                "Amount": value,
                "date": currente_date
                }
        account["statement"].append(transaction)
        print("\n\nValor depositado realizado com sucesso.")
        input("Pressione enter para continuar_")
    else: 
        print('Apenas números maiores que 0')


def withdrawal(account):
    withdrawals_made = sum(1 for transaction in account["statement"] if transaction["description"] == "Saque")

    if withdrawals_made >= WITHDRAWAL_LIMIT:
        print("Você atingiu o limite de saque.")
    elif account["balance"] <= 0:
        print("Sem saldo na conta")
        input("Pressione enter para continuar_")
    else:
        value = input("Digite o valor do saque (apenas números inteiros e separação por vírgula para centavos): ")
        value = verify_number(value)
        if value is None:
            print('formato do número não é aceito')
            time.sleep(3)
        elif value > 0 and value <= account["balance"] and value <= MAX_WITHDRAWAL_AMOUNT:
            account["balance"] -= value
            transaction = {
                "description": "Saque",
                "Amount": value,
                "date": currente_date
            }
            account["statement"].append(transaction)
            print(f"\n\nSaque de {value} realizado com sucesso.")
            input("Pressione enter para continuar_")
        else:
            print("\n\nValor do saque é inválido ou superior ao saldo disponível.")
            input("Pressione enter para continuar_")


from operator import itemgetter

def statement(account):
    clear_screen()
    balance_br = f"{account['balance']:_.2f}"
    balance_br = balance_br.replace('.',',').replace('_','.')
    print("====================== Extrato =======================")
    print(f"Extrato da conta {account['account']} - Saldo: R$ {balance_br}")

    sorted_statement = sorted(account["statement"], key=itemgetter('date'))

    current_period = None

    for transaction in sorted_statement:
        if transaction['date'] != current_period:
            print(f"\nPeríodo: {transaction['date']}")
            print(f"{'Descrição':<30} Valor")
            current_period = transaction['date']
        amount_br = f"{transaction['Amount']:_.2f}"
        amount_br = amount_br.replace('.',',').replace('_','.')
        print(f"{transaction['description']:<30} R$ {amount_br}")
    print("======================================================")
    input("\nPressione enter para continuar_")


def verify_number(number):
    while True:
        if number.replace(",", "").isdigit() or (number.count(",") == 1 and number.replace(",", "").isdigit()):
            if "," in number:
                number = number.replace(",", ".")
            number = float(number)
            return number
        else:
            return None
       