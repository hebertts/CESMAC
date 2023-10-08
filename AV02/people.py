import buscas
import os

contas=[0]


def novo_cadastro(cadastro):
    cpf_digitado, busca = buscas.pesquisar_cpf(cadastro)
    if busca:
        print("CPF existente")
    else:
        nome_digitado = input("Digite seu nome: ")
        buscas.verificar_nome(nome_digitado)
        data_digitada = input("Digite a data de nascimento (dd/MM/yyyy): ")
        buscas.verificar_data_nascimento(data_digitada)
        salario_digitado = input("Digite a sua renda mensal: ")
        salario_digitado = buscas.verificar_saldo(salario_digitado)
        cadastro[cpf_digitado] = {
            "nome": nome_digitado,
            "data_nascimento": data_digitada,
            "salario": salario_digitado,
            "conta":[]
        }
        input("Cadastro efetuado com sucesso\nPressione Enter para continuar_")
def criar_conta(cadastro):
    cpf,busca = buscas.pesquisar_cpf(cadastro)
    if not busca:
        print("CPF não possui cadastro. Cadastre-se primeiro.")
    else:
        agencia  = input('''Escolha sua agência:
[1] - 01
[2] - 02
[3] - 03
=> 

''').zfill(2)
        ultima_conta = max(contas) + 1
        contas.append(ultima_conta)
        conta = str(ultima_conta).zfill(4)
        conta = conta[:3] + '-' + conta[3:]
        nova_conta = {
            "agencia": agencia,
            "conta": conta,
            "extrato": []
        }
        busca["conta"].append(nova_conta)
        input(f"Conta: {conta} cadastrada com sucesso.\nPressione Enter para continuar_")
        return nova_conta
