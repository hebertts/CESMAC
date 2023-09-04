import os
def main():
    escolha = 0
    while escolha != 5:
        os.system("clear")
        escolha = int(input('''Escolha o Desafio: 
1. Desafio 1
2. Desafio 2
3. Desafio 3
4. Desafio 4
5. Desafio 5
-> '''))
        match(escolha):
            case 1: d1()
            case 2: d2()
            case 3: d3()
            case 4: d4()
            case 5: d5()
            case _: print("Valor inválido")

def d1():
    fibonaccie = [0,1]
    contador = 0
    for contador in range(14):
        fibonaccie.append(fibonaccie[contador] + fibonaccie[contador +1])
    separar_valores = ', '.join(map(str,fibonaccie))
    print(separar_valores)
    input("Pressione enter para continuar_")

def d2():
    numeros = []
    contador = 0
    while contador < 3:
        numero_digitado = int(input(f"Digite  o {contador+1}° número: "))
        numeros.append(numero_digitado)
        contador += 1

    if len(set(numeros)) != 1:
        print(f"Maior número: {max(numeros)}")
        print(f"Menor número: {min(numeros)}")
        input("Pressione enter para continuar_")
    else:
        print("Todos os valores digitado são iguais")
        input("Pressione enter para continuar_")

def d3():
    numeros = []
    contador = 0
    epositivo = 0
    emenor = 1000
    while contador < 3:
        numero_digitado = int(input(f"Digite  o {contador+1}° número: ")) 
        while numero_digitado < epositivo or numero_digitado > emenor:
            numero_digitado = int(input("Digite apenas numeros maiores que 0 e menores que 1000: "))            
        numeros.append(numero_digitado)
        contador += 1
    if len(set(numeros)) != 1:
        print(f"Maior número: {max(numeros)}")
        print(f"Menor número: {min(numeros)}")
        input("Pressione enter para continuar_")
    else:
        print("Todos os valores digitado são iguais")
        input("Pressione enter para continuar_")
def d4():
    pessoas = {"nome": "",
               "idade": "" ,
               "salario":"" ,
               "sexo": "",
               "estado_civil": ""
    }
    nome_digitado = input("Qual seu nome: ")
    while len(nome_digitado) <=3:
        nome_digitado = input("Digita um nome com mais de 3 caracteres: ")
    
    idade_digitada = int(input("Quantos anos você tem: "))
    while idade_digitada <= 0 or idade_digitada > 150:
        idade_digitada = int(input("Apenas idades acima de 0 e menores que 150: "))
    
    salario_digitado = int(input("Digite o seu sálario: "))
    while salario_digitado <= 0:
        salario_digitado = int(input("O sálario tem que ser maior do que 0: "))
    
    sexo_digitado = input("Digite o seu sexo: ")
    while sexo_digitado not in ["m","f","outros"]:
        sexo_digitado = input("Escolha entre f, m ou outros: ")
    
    estado_civil_digitado = input("Digite seu estado civil: ")
    while estado_civil_digitado  not in ["s","c","v","d"]:
        estado_civil_digitado = input("Escolha entre c, s, v, d:  ")     
    pessoas["nome"] = nome_digitado
    pessoas["idade"] = idade_digitada
    pessoas["salario"] = salario_digitado
    pessoas["sexo"] = sexo_digitado
    pessoas["estado_civil"] = estado_civil_digitado
    for chave,valor in pessoas.items():
        print(f"{chave}: {valor}")
def d5():
     eprimo = int(input("Digite um número inteiro: "))
     numero_divisor = 0 
     for i in range(1,eprimo+1):
        if eprimo % i == 0:
            numero_divisor += 1

     eprimo = "É primo" if numero_divisor == 2  else "Não é primo" 
     print(eprimo)
main()