''' Check if a number is even or odd '''

# input returns string, so we turn it into integer with int() function, so that we can compare it with another integer 
number = int(input("Please enter a number between 1-100: \n"))

if number > 100:
    print("Invalid input")
else:
    if number % 2 == 0:
        print(f"Your number {number} is even.")
    else:
        print(f"Your number {number} is odd.")