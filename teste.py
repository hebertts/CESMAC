email = input("Digite o seu email ou pressione enter para pular: ")
if email.strip():
    while True:
        if email.endswith('@yahoo.com') or email.endswith('@gmail.com') or email.endswith('@outlook.com'):
            break
        else:
             email = input("Por favor, insira um email válido: ")
