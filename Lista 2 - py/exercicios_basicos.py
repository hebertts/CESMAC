import os

def main():
    escolha = 0
    while escolha != 4:
        os.system("clear")
        escolha = int(input('''Escolha o Desafio: 
1. Desafio 1
2. Desafio 2
3. Desafio 3
-> '''))
        match(escolha):
            case 1: d1()
            case 2: d2()
            case 3: d3()
            case _: print("Valor inválido")

def d1():
    contador = 0 
    while contador <= 100:
        print(contador)
        contador += 1
    input("Pressione enter para continuar_")

def d2():
    n = int(input("Digite o número total da repetição: "))
    contador = 0
    while contador <= n:
        print(contador)
        contador += 1
    input("Pressione enter para continuar_")
def d3():
    repit = "S"
    lista_valores = []
    while repit.upper() == "S":
        os.system("clear")
        print("Operação - Adição")
        qtd_soma = int(input("\nQuantos números você gostaria de somar? "))
        contador = 0
        while contador < qtd_soma:
            valores = int(input(f"Digite o {contador+1}° número: "))
            lista_valores.append(valores)
            contador +=1
        valores_somar = ' + '.join(map(str,lista_valores))
        soma = sum(lista_valores)
        print(f"{valores_somar} = {soma}")
        repit = input('''Deseja realizar mais uma soma? [S ou N] 
Respota: ''')

main()