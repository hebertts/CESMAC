# Sistema Bancário

    Este código simula alguns funcionalidades(simplificadas) que um banco possui, criado em python com sql, foi utilizado o Mysql como sistema para gerenciar o banco de dados, a aplicação possui:

    ° Cadastro de cliente
    ° Criação de conta
    ° Sacar
    ° Depositar
    ° Pedir Empréstimo
    ° Pagar parcelas do Empréstimo
    ° Visualizar informações do cliente

# Criação das tabelas
    CREATE SCHEMA IF NOT EXISTS cesm_bank;

    USE cesm_bank;
    CREATE SCHEMA IF NOT EXISTS cesm_bank;

    USE cesm_bank;
    -- Tabela para armazenar informações do cliente
    CREATE TABLE client_registry(
        CPF VARCHAR(12) PRIMARY KEY,
        Name_client VARCHAR(80) NOT NULL,
        Birth_date DATE NOT NULL,
        Salary DECIMAL(10,2) NOT NULL,
        Dependent TINYINT(1),
        Email VARCHAR(40) UNIQUE
    );
    -- Tabela para armazenar algumas informações da conta
    CREATE TABLE accounts(
        Account_client VARCHAR(6) PRIMARY KEY,
        Balance DECIMAL(10,2) NOT NULL,
        Creation_date DATE,
        CPF VARCHAR(12),
        CONSTRAINT fk_account_cpf FOREIGN KEY (CPF) REFERENCES client_registry(CPF)
    );
    -- Movimentações da conta
    CREATE TABLE bank_statement(
        ID INT PRIMARY KEY AUTO_INCREMENT,
        Account_client VARCHAR(6),
        Transaction_date datetime,
        Typo VARCHAR(40),
        value_statement DECIMAL(10,2),
        FOREIGN KEY (Account_client) REFERENCES accounts(Account_client)
    );



    -- Tabela de Empréstimos solicitados pelo cliente
    CREATE TABLE loan (
        id_loan INT PRIMARY KEY AUTO_INCREMENT,
        total_value DECIMAL(10, 2), -- Example of total value as decimal
        date_loan DATE,
        payment_term INT, -- Term in months, for example
        account_loan VARCHAR(6),
        FOREIGN KEY (account_loan) REFERENCES accounts(Account_client)
    );

    -- Parcelas do empréstimo
    CREATE TABLE Installments (
        id_installment INT PRIMARY KEY AUTO_INCREMENT,
        id_loan INT,
        installment_number INT,
        installment_value DECIMAL(10, 2),
        due_date DATE,
        payment_status BOOLEAN DEFAULT FALSE, -- By default, the installment is unpaid
        FOREIGN KEY (id_loan) REFERENCES loan(id_loan)
    );

# Criação setx para getenv

    Enviar no terminal operacional: 

    setx host,
    setx user,
    setx password,
    setx database

# Instalações 


    pip install prettytable

    pip install mysql.connector