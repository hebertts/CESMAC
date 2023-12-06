import os
import mysql.connector
from datetime import datetime, timedelta
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
        sql = '''INSERT INTO accounts(Account_client,Balance,Creation_date,CPF,password_account,limit_credit)
        VALUES (%s,%s,%s,%s,%s,%s)'''
        cursor.execute(sql,(account,balance,date,cpf,password,0))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback()


def insert_statement_database(Account_client, Transaction_date, Typo, value_statement, newbalance):
    try:
        insert_sql = '''
        INSERT INTO bank_statement (Account_client, Transaction_date, Typo, value_statement)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_sql, (Account_client, Transaction_date, Typo, value_statement))
        
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

def insert_loan_database(total_value, date_loan, payment_term, account_loan,payment_mounth):
    try:
        loan_sql = '''INSERT INTO loan(total_value, date_loan, payment_term, account_loan)
                      VALUES (%s, %s, %s, %s)'''
        cursor.execute(loan_sql, (total_value, date_loan, payment_term, account_loan))
        id_loan = cursor.lastrowid  

       
        installment_interval = 30 

        for installment_number in range(1, payment_term + 1):
            installment_value = payment_mounth 
            due_date = (datetime.strptime(date_loan, '%Y-%m-%d') + timedelta(days=(installment_number - 1) * installment_interval)).strftime('%Y-%m-%d')
            payment_status = False  

            installment_sql = '''INSERT INTO installments(id_loan, installment_number,
                                  installment_value, due_date, payment_status)
                                  VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(installment_sql, (id_loan, installment_number, installment_value,
                                             due_date, payment_status))
        
        conexao.commit()  
        print("Data inserted successfully!")

    except Exception as e:
        conexao.rollback()  # Rollback the changes if there's an exception
        input(f"Error: {e}")


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
        sql = f'''SELECT client_registry.Name_client, accounts.Account_client,accounts.password_account,accounts.Balance,
        accounts.limit_credit,client_registry.Salary
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

def search_client_database(cpf):
    try:
        sql = f'''select client_registry.Name_client, client_registry.Birth_date,
        client_registry.Salary,client_registry.Dependent,client_registry.Email,accounts.Balance from client_registry
        inner join accounts ON client_registry.CPF = accounts.CPF 
        where client_registry.CPF = {cpf};'''
        cursor.execute(sql)
        result = cursor.fetchone()
        return 'vazio' if result == None else result
    except Exception as e:
        print(f'Erro: {e}')
        conexao.rollback()

def search_statement_database(account):
    try:
        sql = 'SELECT Typo, value_statement, Transaction_date FROM bank_statement WHERE Account_client = %s'
        cursor.execute(sql, (account,))
        result = cursor.fetchall()
        
        statement_data = []
        for row in result:
            transaction = {
                'Transaction_date': row[2],
                'Typo': row[0],
                'value_statement': row[1]
            }
            statement_data.append(transaction)
            
        return {'statement': statement_data} if statement_data else 'vazio'
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        conexao.rollback()
        return 'vazio'
def update_limit(value,account):
    try:
        sql = 'UPDATE accounts SET limit_credit = %s WHERE account_client = %s'
        cursor.execute(sql,(value,account))
        conexao.commit()
    except Exception as e:
        print(f"Erro: {e}")
        conexao.rollback() 
def search_loan_database(account):
    try:
        sql = '''SELECT loan.id_loan, loan.amount_paid,installments.id_installment,installments.installment_value,
        installments.due_date,installments.payment_status,loan.total_value   from loan
        INNER JOIN installments ON loan.id_loan = installments.id_loan WHERE loan.account_loan = %s'''
        cursor.execute(sql,(account,))
        result = cursor.fetchall()
        installments_data = []
        
        for row in result:
            info = {
                'id_loan': row[0],
                'amount_paid': row[1],
                'id_installments': row[2],
                'installments_value': row[3],
                'due_date': row[4],
                'status': row[5]  ,# Adjusted index for payment_status
                'value_total': row[6]
            }  
            installments_data.append(info)
        return {'installments': installments_data} if installments_data else 'vazio'
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        conexao.rollback()
        return 'vazio'

def update_loan_installments(account,id_loan,status,id_installments,amount_paid):
    try:
        sql = 'UPDATE loan SET amount_paid = %s WHERE account_loan = %s AND id_loan = %s'
        cursor.execute(sql,(amount_paid,account,id_loan,))
        
        sql = 'UPDATE installments SET payment_status = %s WHERE id_installment = %s'
        cursor.execute(sql,(status,id_installments,))
        conexao.commit()
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        conexao.rollback()
def updade_balance_client(cpf,balance):
    try:
        sql = 'UPDATE client_registry SET balance = %s WHERE CPF = %s '
        cursor.execute(sql,(balance,cpf,))
    except Exception as e:
        print(f"Erro ao buscar extrato: {e}")
        conexao.rollback()
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
        sql = '''SELECT Typo, count(Typo) As Total FROM bank_statement
        WHERE Typo = 'Saque' AND Account_client = %s AND DATE_FORMAT(Transaction_date, '%Y-%m-%d') = %s
        GROUP BY Typo '''
        cursor.execute(sql, (account, today))
        result = cursor.fetchone() 
        return 0 if result is None else result[1] 
    except Exception as e:
        print(f"Erro ao contar saques: {e}")
        conexao.rollback()
        return 0 

def close_sql():
    conexao.close()