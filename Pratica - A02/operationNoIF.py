
def add(number1,number2):
    return number1 + number2
def multiply(number1,number2):
    return number1 * number2
def divide(number1,number2):
    return number1 / number2
def subtract(number1,number2):
    return number1 - number2

calculate= {
    "1":[add,'Addition','+'],
    "2":[multiply,'Multiplication','*'],
    "3":[divide,'Division','/'],
    "4":[subtract,'Subtraction','-']
    }
def menu(choice,number1,number2):
    symbol = calculate[choice][2]
    operation = calculate[choice][1]
    result = calculate[choice][0](number1,number2)
    return symbol,result,operation