import os
import mysql.connector
import random
from datetime import datetime
currente_date  =datetime.now()
# Acesse as variáv eis de ambiente
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

# Conecte-se ao banco de dados
conexao = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database=database
)

cursor = conexao.cursor()

def search_cpf_database(cpf): 
    sql = 'SELECT * FROM client_registry WHERE CPF = %s'
    cursor.execute(sql, (cpf,))
    result = cursor.fetchone()
    print(result)
    valor = float(result[3]) + 6
 
    print(valor)
    return 'vazio' if result is None else result
def select_account_database(cpf):
    sql = f'''SELECT client_registry.Name_client, accounts.Account_client
    FROM client_registry
    left JOIN accounts ON accounts.CPF = client_registry.CPF
    where  client_registry.CPF = {cpf}'''
    cursor.execute(sql)
    result= cursor.fetchone()
   
    return 'vazio' if result == None else result

from datetime import datetime
from operator import itemgetter

def search_statement_database(account='4989-0'):
    try:
        sql = 'SELECT Descricao, value_statement, Transaction_date FROM bank_statement WHERE Account_client = %s'
        cursor.execute(sql, (account,))
        result = cursor.fetchall()
        
        statement_data = []
        for row in result:
            transaction = {
                'Transaction_date': row[2],
                'Descricao': row[0],
                'value_statement': row[1]
            }
            statement_data.append(transaction)
            
        return {'statement': statement_data} if statement_data else 'vazio'
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        return 'vazio'

def Statement():
    try:
        balance_br = f"{float(0):_.2f}"
        balance_br = balance_br.replace('.', ',').replace('_', '.')
        print("================= ====== Extrato =======================")
        print(f"Extrato da conta {'4989-0'} - Saldo: R$ {balance_br}")
        
        account = search_statement_database("4989-0")
        sorted_statement = sorted(account['statement'], key=itemgetter('Transaction_date'))
        current_period = None
        
        for transaction in sorted_statement:
            if transaction['Transaction_date'].date() != current_period:
                print(f"\nPeríodo: {(transaction['Transaction_date']).strftime('%Y-%m-%d')}")
                current_period = transaction['Transaction_date'].date()
            
            amount_br = f"{float(transaction['value_statement']):_.2f}"
            amount_br = amount_br.replace('.', ',').replace('_', '.')
            print(f"{transaction['Descricao']:<30} R$ {amount_br}")
        
        print("=============== =====================================")
        input("\nPressione enter para continuar_")
    
    except Exception as e:
        print(f"Erro ao imprimir extrato: {e}")

Statement()



cpf = 12345678912

'''account_info = select_account_database(cpf)
print(account_info)
search_cpf_database(cpf)
if account_info[1] == None:
    print("sem conta")'''

def search_statement_database(account):
    try:
        sql = 'SELECT Descricao, value_statement, Transaction_date FROM bank_statement WHERE Account_client = %s ORDER BY Transaction_date'
        cursor.execute(sql, (account,))
        result = cursor.fetchall()
        return result if result else 'vazio'
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        return 'vazio'    


conexao.close()  # Feche a conexão quando terminar de usar
