import msvcrt

def get_password(prompt="Digite sua senha: "):
    print(prompt, end="", flush=True)
    senha = b""
    while True:
        char = msvcrt.getch()
        if char == b'\r' or char == b'\n':
            print()
            break
        elif char == b'\x08':  # Backspace
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char
            print("*", end="", flush=True)
    return senha.decode('utf-8')

# Usando a função para obter a senha mascarada
senha = get_password()
print("Senha digitada:", senha)  # A senha não é exibida no terminal
