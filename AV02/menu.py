import os
import banco
import people
import buscas
limpar = ["cls","clear"]
cadastro={}

def menu_inicial():
    menu_principal = {1:"Fazer cadastro",2:"Criar Conta",3:"Login",4:"Sair"}
    escolha = 0  # Inicialize a variável escolha
    while escolha!=4:
        os.system("clear")
        print('-'*40)
        print("|           Menu Principal             |")
        for chave,valor in menu_principal.items():
            print(f'| {chave}: {valor}'.ljust(39)+'|')
        print('-'*40)
        escolha= int(input("Digite o número desejado: "))         
        if escolha == 1:
            people.novo_cadastro(cadastro)
        elif escolha == 2:
            people.criar_conta(cadastro)
        elif escolha == 3:
            cpf = buscas.pesquisar_cpf(cadastro)
            banco.menu_banco(cadastro,cpf)
        elif escolha == 4:
            print('Saindo...')


    

menu_inicial()
