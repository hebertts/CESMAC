from operation import *
import os
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
os.system('clear')
choice = int(input('''Choose the operation:
1. Add
2. Multiply
3. Divide
4. Subtract
=> '''))
if choice == 1:
    sum_value = add(number1,number2)
    print(f'{number1} + {number2} = {sum_value}')
elif choice == 2:
    multiply_value = multiply(number1,number2)
    print(f'{number1} * {number2} = {multiply_value}')

elif choice == 3:
    divide_value = divide(number1,number2)
    print(f'{number1} / {number2} = {divide_value}')
elif choice == 4:
    subtract_value = subtract(number1,number2)
    print(f'{number1} - {number2} = {subtract_value}')