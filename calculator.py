''' Create a calculator '''

# function that exponentiates two numbers
def exponentiate(a, b):
    return a ** b
# function that multiplies two numbers
def multiply(a, b):
    return a * b
# function that divides two numbers
def divide(a, b):
    return a / b
# function that adds two numbers
def add(a, b):
    return a + b
# function that subtracts two numbers
def subtract(a, b):
    return a - b
# function that shows the modulo of two numbers
def modulo(a, b):
    return a % b
# function that shows the integer division of two numbers
def integer_division(a, b):
    return a // b

# display on the screen
print("\nThis calculator provides the following operations: \n")
print(" ** Exponention")
print(" * Muliplication")
print(" / Dividion")
print(" + Addition")
print(" - Subtraction")
print(" % Modulo")
print(" // Integer division\n")

# make a list with the possible operations
operations = ['**','*','/','+','-','%','//']

while True:
    # ask user what operation they want to perform
    select = input("Select operation **, *, /, +, -, %, //\n")
    # chack if the operation user selected is in the possible operations
    if select in operations:
        # ask user for two numbers
        n0 = float(input("Enter a number/can be integer or floating point/: "))
        n1 = float(input("Enter another number/can be integer or floating point/: "))
        if select == '**':
            print(exponentiate(n0, n1))
        elif select == '*':
            print(multiply(n0, n1))
        elif select == '/':
            print(divide(n0, n1))
        elif select == '+':
            print(add(n0, n1))
        elif select == '-':
            print(subtract(n0, n1))
        elif select == '%':
            print(modulo(n0, n1))
        elif select == '//':
            print(integer_division(n0, n1))

        # ask user if they want to do another calculation
        another = input("Another calculation? / NO-type 'n', YES - press enter\n").lower()
        if another == 'n':
            break
    # if the operation user selected is NOT in the possible operations
    else:
        print("Invalid input.")
print("Thank you! :)")