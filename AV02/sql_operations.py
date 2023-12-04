import os
import mysql.connector

# Acesse as variáveis de ambiente
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

def insert_registry(cpf,name,data,salario,dependente,email):
    try:
        sql = '''INSERT INTO client_registry(CPF, Name_client, Birth_date, Salary, Dependent, Email) 
        VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(sql, (cpf, name, data, salario, dependente, email))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback()

def insert_accounts_database(account,balance,date,cpf,password):
    try:
        sql = '''INSERT INTO accounts(Account_client,Balance,Creation_date,CPF,password_account)
        VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(sql,(account,balance,date,cpf,password))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback()


def insert_statement_database(Account_client, Transaction_date, Descricao, value_statement, newbalance):
    try:
        insert_sql = '''
        INSERT INTO bank_statement (Account_client, Transaction_date, Descricao, value_statement)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_sql, (Account_client, Transaction_date, Descricao, value_statement))
        
        update_sql = '''
        UPDATE accounts
        SET Balance = %s
        WHERE Account_client = %s
        '''
        cursor.execute(update_sql, (newbalance, Account_client))
        
        conexao.commit()  
    except Exception as e:
        print(f"Erro ao realizar operação: {e}")
        conexao.rollback() 
def insert_loan_database(Account_client,Loan_date,End_date,Released_amount,Interest_rate):
    try:
        sql = '''INSERT INTO loan(Account_client,Loan_date,End_date,Released_amount,Interest_rate)
        VALUES (%s,%s,%s,%s)'''
        cursor.execute(sql,(Account_client,Loan_date,End_date,Released_amount,Interest_rate))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback()
def search_cpf_database(cpf):
    try: 
        sql = f'SELECT * FROM client_registry WHERE CPF = {cpf}'
        cursor.execute(sql)
        result= cursor.fetchone()
        return 'vazio' if result == None else result
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback()

def select_account_database(cpf):
    try:
        sql = f'''SELECT client_registry.Name_client, accounts.Account_client,accounts.password_account,accounts.Balance
        FROM client_registry
        left JOIN accounts ON accounts.CPF = client_registry.CPF
        where  client_registry.CPF = {cpf}'''
        cursor.execute(sql)
        result= cursor.fetchone()
        return 'vazio' if result == None else result 
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback() 
def search_account_databese(account):
    try:
        sql = f'''SELECT accounts.Account_client,accounts.Balance,accounts.password_account,client_registry.Name_client 
        FROM accounts 
        INNER JOIN client_registry ON accounts.CPF = client_registry.CPF
        WHERE Account_client = {account}'''
        cursor.execute(sql)
        result = cursor.fetchone()
        return 'vazio' if result == None else result
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback() 

def search_statement_database(account):
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


def update_password(passNew,cpf):
    try:
        sql = 'UPDATE accounts SET password_account = %s WHERE CPF = %s'
        cursor.execute(sql,(passNew,cpf))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback() 

def count_withdrawal(account, today):
    try:
        sql = '''SELECT Descricao, count(Descricao) As Total FROM bank_statement
        WHERE Descricao = 'Saque' AND Account_client = %s AND DATE_FORMAT(Transaction_date, '%Y-%m-%d') = %s
        GROUP BY Descricao '''
        cursor.execute(sql, (account, today))
        result = cursor.fetchone()  # Obtém a primeira linha de resultados

        return 0 if result is None else result[1]  # Retorna o segundo item da linha (o total)
    except Exception as e:
        print(f"Erro ao contar saques: {e}")
        return 0  # Retorna 0 em caso de erros
def close_sql():
    conexao.close()