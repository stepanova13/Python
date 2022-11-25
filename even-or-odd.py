''' Check if a number is even or odd '''

while True:
    # input returns string, so we cast it into integer with int() function, so that we can compare it with another integer
    number = int(input("Please enter a number between 1-100: \n"))
    if number < 0 or number > 100:
        print("Invalid input")
    else:
        if number % 2 == 0:
            print(f"Number {number} is even.")
        else:
            print(f"Number {number} is odd.")

    another_try = input("Another number? / NO-type 'n', YES - press enter\n")
    if another_try == 'n':
        break