''' 
calculator.py: create a calculator

Created By  : stepanova13
'''

# define a function that exponentiates two numbers
def exponentiate(a, b):
    '''
    this function exponents two nembers
    args: a(float), b(float)
    return: float
    '''
    return a ** b
# define a function that multiplies two numbers
def multiply(a, b):
    '''
    this function multiplies two nembers
    args: a(float), b(float)
    return: float
    '''
    return a * b
# define a function that divides two numbers
def divide(a, b):
    '''
    this function divides two nembers
    args: a(float), b(float)
    return: float
    '''
    return a / b
# define a function that adds two numbers
def add(a, b):
    '''
    this function adds two nembers
    args: a(float), b(float)
    return: float
    '''
    return a + b
# define a function that subtracts two numbers
def subtract(a, b):
    '''
    this function subtracts two nembers
    args: a(float), b(float)
    return: float
    '''
    return a - b
# define a function that returns the modulo of two numbers
def modulo(a, b):
    '''
    this function returns the modulo of two nembers
    args: a(float), b(float)
    return: float
    '''
    return a % b
# define a function that returns the integer division of two numbers
def integer_division(a, b):
    '''
    this function returns the integer division of two nembers
    args: a(float), b(float)
    return: float
    '''
    return a // b

#body of the main
if __name__ == '__main__':
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
            try:
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
                another = input("Another calculation? / NO -type 'n', YES - press enter\n").lower()
                # if answer is no, break out of the whole loop
                if another == 'n':
                    break
            # handle exceptions  
            except ZeroDivisionError:
                print("Division by zero is not supported.")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as error:
                print(f"There is an error: {error}")
        # if the operation user selected is NOT in the list of possible operations print "Invalid input."
        else:
            print("Invalid input.")
            
    # when out of the while loop, print "Thank you!"
    print("Thank you for using our calculator!")

