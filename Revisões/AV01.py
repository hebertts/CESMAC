def Menu():
    escolha = int(input('''Digite o Desafio:
1. Desafio 1
2. Desafio 2
3. Desafio 3
4. Desafio 4
=> '''))
    match(escolha):
        case 1: desafio1()
        case 2: desafio2()
        case 3: desafio3()
        case 4: desafio4()

def desafio1():
    numero_digitado = int(input("Digite um número inteiro: "))
    pares = [numero for numero in range(1,numero_digitado+1) if numero % 2 == 0]         
    impares = [numero for numero in range(1,numero_digitado+1) if numero %2 != 0]
    print(f"Números pares até{numero_digitado}: {', '.join(map(str, pares))}")
    print(f"Números ímpares até {numero_digitado}: {', '.join(map(str,impares))}")

def desafio2():
    notas = 3
    total = 0
    for i in range(notas):
      nota = float(input(f"Digite a {i+1}° nota: "))
      total += nota
    total = total/notas
    if total >= 7:
      print("Aprovado")
    elif total < 4:
      print("Reprovado")
    else:
      print("Reposição")
    input("Pressione qualquer tecla_")

def desafio3():
   n = int(input("Digite um valor inteiro: "))
   for i in range(1,n+1):
      print(f"{i}: {i*2}")

def desafio4():
    temperatura_escolhida = int(input('''1. Converter de Celsius para Fahrenheit
2. Converter de Fahrenheit para Celsius
=> '''))
    if temperatura_escolhida == 1:
      Celsius = float(input("Digite a temperatura °C: "))
      Fahrenheit = (Celsius*9/5) + 32
      print(f"{Celsius}°C é igual a {Fahrenheit}°F ")
    else:
      Fahrenheit = float(input("Digite a temperatura °F: "))
      Celsius = (Fahrenheit - 32)*5/9
      print(f"{Fahrenheit}°F é igual a {Celsius}°C ")   
   
   
Menu()   