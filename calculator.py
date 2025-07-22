import os

art = '''


 _______       _             _                         
(_______)     | |           | |         _              
 _       _____| | ____ _   _| | _____ _| |_ ___   ____ 
| |     (____ | |/ ___) | | | |(____ (_   _) _ \ / ___)
| |_____/ ___ | ( (___| |_| | |/ ___ | | || |_| | |    
 \______)_____|\_)____)____/ \_)_____|  \__)___/|_|    
By Ayomal

'''


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():

    print(art)

    should_accumulate = True
    n1 = float(input('Enter first number: '))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        calc_operation = input('Enter operation: ')

        n2 = float(input('Enter second number: '))

        answer = operations[calc_operation](n1, n2)

        print(f'{n1} {calc_operation} {n2} = {answer}')

        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ")

        if choice == 'y':
            n1 = answer
            should_accumulate = True
        else:
            should_accumulate = False
            print(os.system('cls'))
            calculator()


calculator()
