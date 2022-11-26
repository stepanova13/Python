''' Check if a number is even or odd '''

# make a while loop
while True:
    # ask user to enter a number between 1 and 100
    # function 'input' returns string, so we cast it into integer with int() function, so that we can compare it with another integer
    number = int(input("Please enter a number between 1-100: \n"))
    # if number is less than 0 or greater than 100, print "Invalid input"
    if number < 0 or number > 100:
        print("Invalid input")
    # if number between 1 and 100
    else:
        if number % 2 == 0:
            print(f"Number {number} is even.")
        else:
            print(f"Number {number} is odd.")
    # ask user if they want to do another number and make the input lowercase
    another_try = input("Another number? / NO-type 'n', YES - press enter\n")
    # if answer is no
    if another_try == 'n':
        # break out if the while loop
        break