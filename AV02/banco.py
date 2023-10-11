VALOR_MAXIMO_SAQUE = 1000
LIMITE_SAQUE = 5

import buscas
def deposito(cadastro,cpf):
    conta_digitada = input("Digite o número da conta: ")
    conta = buscas.encontrar_conta(cadastro[cpf]["conta"], conta_digitada)
    if not conta:
        print("Conta não encontrada")
        input("Pressione enter para continuar_")
    else:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"].append(f"Depósito de {valor}")
                print("Valor depositado realizado com sucesso.")
                input("Pressione enter para continuar_")
            else:
                print("Valor do depósito é inválido.")
                input("Pressione enter para continuar_")

def saque(cadastro,cpf):
    conta_digitada = input("Digite o número da conta: ")
    conta = buscas.encontrar_conta(cadastro[cpf]["conta"], conta_digitada)
        
    if conta is None:
        print("Conta não encontrada")
        input("Pressione enter para continuar_")
    else:
            saques_realizados = sum(1 for transacao in conta.get("extrato", []) if "Saque" in transacao)
            if saques_realizados >= LIMITE_SAQUE:
                print("Você atingiu o limite de saque.")
            elif conta["saldo"] <= 0:
                print("Sem saldo na conta")
                input("Pressione enter para continuar_")
            else:
                valor = float(input("Digite o valor do saque: "))
                if valor > 0 and valor <= conta["saldo"] and valor <= VALOR_MAXIMO_SAQUE:
                    conta["saldo"] -= valor
                    conta["extrato"].append(f"Saque de {valor}")
                    print(f"Saque de {valor} realizado com sucesso.")
                    input("Pressione enter para continuar_")
                else:
                    print("Valor do saque é inválido ou superior ao saldo disponível.")
                    input("Pressione enter para continuar_")
def extrato(cadastro,cpf):
    conta_digitada = input("Digite o número da conta: ")
    conta = buscas.encontrar_conta(cadastro[cpf]["conta"], conta_digitada)
    if not conta:
            print("Conta não encontrada")
    else:
            print("====================== Extrato =======================")
            print(f"Extrato da conta {conta['conta']} - Saldo: R$ {conta['saldo']:.2f}")
            print("Histórico de transações:")
            for transacao in conta["extrato"]:
                print(transacao)
            print("======================================================")
            input("Pressione enter para continuar_")

def menu_banco(cpf,cadastro):
    menu_opcoes = {1:"Sacar",2:"Depositar",3:"Extrato",4:"Sair"}
    escolha = 0  # Inicialize a variável escolha
    while escolha != len(menu_opcoes):
        primeiro_nome = cadastro[cpf]["nome"].split()  # Pega o primeiro nome
        print('-' * 40)
        print(f'| Olá, {primeiro_nome}'.ljust(39) + '|')
        print(f'| Conta        {cadastro[cpf]["conta"]}'.ljust(39) + '|')
        for chave, valor in menu_opcoes.items():
            print(f'| {chave}: {valor}'.ljust(39) + '|')
        print('-' * 40)
        escolha = int(input('Digite o número desejado: '))

        if escolha ==1:
            saque(cadastro,cpf)
        elif escolha == 2:
            deposito(cadastro,cpf)
        elif escolha == 3:
            extrato(cadastro,cpf)
        elif escolha == 4:
            print('Saindo...')

