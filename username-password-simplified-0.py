""" 
This program asks for username and password and check if they are correct. 
User has 5 tries. After fifth try print "Account locked" 

Created By  : stepanova13
"""

# create database
database = {
    "username0" : "password0",
    "username1" : "password1",
    "username2" : "password2",
}

# initializing the variable for the number of tries
n = 5

# use while loop to keep asking until the credentials are correct or user runs out of tries( 5 tries)
while n != 0:
    username = input("username: ")
    password = input("password: ")
    n -= 1
    if username in database and database[username] == password:
        print("\n$$$$$ ACCESS GRANTED $$$$$\n")
        break
    elif n > 0:
        print("Incorrect. Try again.")
    else:
        print("Account locked.")