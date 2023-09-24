from operationNoIF import *
import os
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
os.system('clear')
choice = input('''Choose the operation:
1.Add
2.Multiply
3.Divide
4.Subtract
=> ''')
symbol,result,operation = menu(choice,number1,number2)
os.system('clear')
print(f'Selected operation: {operation}')
print(f'{number1} {symbol} {number2} = {result}')