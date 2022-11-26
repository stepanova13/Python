''' Create a calculator '''

# define a function that exponentiates two numbers
def exponentiate(a, b):
    return a ** b
# define a function that multiplies two numbers
def multiply(a, b):
    return a * b
# define a function that divides two numbers
def divide(a, b):
    return a / b
# define a function that adds two numbers
def add(a, b):
    return a + b
# define a function that subtracts two numbers
def subtract(a, b):
    return a - b
# define a function that returns the modulo of two numbers
def modulo(a, b):
    return a % b
# define a function that returns the integer division of two numbers
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
    # if the operation is in the list of possible operations
    if select in operations:
        # ask user for two numbers
        n0 = float(input("Enter a number/can be integer or floating point/: "))
        n1 = float(input("Enter another number/can be integer or floating point/: "))
        # according to the operation user selected, call the corresponding function and display the output
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
        # if answer is no, break out of the whole loop
        if another == 'n':
            break
    # if the operation user selected is NOT in the list of possible operations print "Invalid input."
    else:
        print("Invalid input.")
# when out of the while loop, print "Thank you!"
print("Thank you!")