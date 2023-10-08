import os
import banco
import people

escolha = 0  # Inicialize a variável escolha

while escolha != 7:
    os.system("clear")
    escolha = int(input('''====================== MENU =======================
 1. Fazer cadastro
 2. Criar Conta
 3. Depósito
 4. Saque
 5. Extrato
 6. Listar contas
 7. Sair 
=> '''))
          
    if escolha == 3:
        banco.deposito(cadastro)
    elif escolha == 4:
        banco.saque(cadastro)
    elif escolha == 5:
        banco.extrato(cadastro)
    elif escolha == 1:
        people.novo_cadastro(cadastro)
    elif escolha == 2:
        people.criar_conta(cadastro)
    elif escolha == 7:
        print("Saindo...")
print(cadastro)