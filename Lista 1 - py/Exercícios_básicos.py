import os

def main():
  escolha = 0
  while escolha !=8:
   os.system("clear")
   escolha = int(input('''Escolha o Desafio: 
1. Desafio 1
2. Desafio 2
3. Desafio 3
4. Desafio 4
5. Desafio 5
6. Desafio 6
7. Desafio 7
-> '''))
   match(escolha):
      case 1: d1()
      case 2: d2()
      case 3: d3()
      case 4: d4()
      case 5: d5()
      case 6: d6()
      case 7: d7()
      case _: print("Valor inválido")
def d1():
   os.system("clear")
   print('''      DESAFIO 1
        ''')
   numero = int(input("Digite um número: "))
   epar = numero %2
   if epar == 0:
      print(f"o número {numero} é par")
   else:
      print(f"O número {numero} é impar")
   input("Pressione qualquer tecla_")

def d2():
   os.system("clear")
   print('''      DESAFIO 2
        ''')

   num1 = float(input("Digite um número: "))
   num2 = float(input("Digite outro número: "))
   if num1 > num2:
      print(f"Número: {num1} é maior que {num2}")
   elif num1 == num2:
       print("Os dois números são igauis")
   else:
      print(f"O número {num2} é maior que {num1}")
   input("Pressione qualquer tecla_")
    
def d3():
   os.system("clear")
   print('''      DESAFIO 3
        ''') 
   vogal = "aeiou"
   letra = str(input("Digite uma letra: "))
   if letra.lower() in vogal:
      print("é vogal")
   else:
      print("É consoante")
   input("Pressione qualquer tecla_")
def d4():
   os.system("clear")
   print('''      DESAFIO 4
        ''') 
   notas = int(input("Quantas notas você gostaria de inserir? "))
   total = 0
   for i in range(notas):
      nota = float(input(f"Digite a {i+1}° nota: "))
      total += nota
   total = total/notas
   if total < 7:
      print("Reprovado")
   elif total == 10:
      print("Aprovado com distinção")
   else:
      print("Aprovado")
   input("Pressione qualquer tecla_")

def d5():
   os.system("clear")
   print('''      DESAFIO 5
        ''')
   numero = 3
   emaior = 0
   eigual = 1 
   for i in range(numero):
      n = float(input(f"Digite o {i+1}° número: "))
      if n > emaior:
         emaior = n
      elif n == emaior:
         eigual += 1
   if eigual == 3:
      print("Os 3 números são iguais")
   else:
      print(f"\nO número {emaior} é o maior número entre os 3 números digitados")
   input("Pressione qualquer tecla_")
      
def d6():
   os.system("clear")
   print('''      DESAFIO 6
        ''') 
   turno = input('''Qual seu turno?
M. Matutino
V. Vespertino
N. Noturno                 
''')
   match turno.lower():
      case "m":
         print("Bom dia!")
      case "v" :
         print("Boa tarde!")
      case "n":
         print("Boa noite!")
   input("Pressione qualquer tecla_")
def d7():
   os.system("clear")
   print('''      DESAFIO 7
        ''')
   nivel_suspeito = 0
   p1 = int(input('''Telefonou para a vítima?
1. Sim
2. Não
-> '''))
   p2 = int(input('''Esteve no local do crime?
1. Sim
2. Não
-> '''))
   p3 = int(input('''Mora perto da vítima?
1. Sim
2. Não
-> '''))
   p4 = int(input('''Devia para a vítima?
1. Sim
2. Não
-> '''))
   p5 = int(input('''Já trabalhou com a vítima?
1. Sim
2. Não
-> '''))
   if p1 == 1:
      nivel_suspeito += 1
   if p2 == 1:
      nivel_suspeito += 1
   if p3 == 1:
      nivel_suspeito += 1
   if p4 == 1:
      nivel_suspeito += 1
   if p5 == 1:
      nivel_suspeito += 1
   if nivel_suspeito == 2:
      print("Você é deveras suspeito")
   elif nivel_suspeito == 3 or nivel_suspeito == 4:
      print("Chamem a equipe investigativa aqui, temos um cúmplice")
   elif nivel_suspeito == 5:
      print("Os homi estão vindo lhe buscar")
   else:
      print("Nem sei o motivo de você está fazendo este questionário")
   input("Pressione qualquer tecla_")

main()