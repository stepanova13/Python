''' Check if a number is even or odd '''

# defing function even_or_odd_number that checks if a number is even or odd and displays it on the screen
def even_or_odd_number(n):
    if n % 2 == 0:
        print(n," is an EVEN number")
    else:
        print(n," is an ODD number")

# make a while loop
while True:  
    # ask user to enter a number between 1 and 100
    # intrinsic fulction 'input' returns string, so we cast it into integer with int() function, so that we can compare it with another integer 
    number = int(input("Please enter a number between 1-100: \n"))
    # if number is less than 0 or greater than 100, print "Invalid input"
    if number < 0 or number > 100:
        print("Invalid input")
    else:
        # if number between 1 and 100, call even_or_odd_number function
        even_or_odd_number(number)
    # ask user if they want to do another number and make the input lowercase
    another = input("Another number? / NO-type 'n', YES - press enter\n").lower()
    # if answer is no
    if another == 'n':
        # break out if the while loop
        break
