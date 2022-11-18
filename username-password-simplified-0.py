""" Ask user for username and password 5 times. After the fifth time lock account. """

# create database
database = {
    "username0" : "password0",
    "username1" : "password1",
    "username2" : "password2",
}

# assign variables
n = 5
username = ''
password = ''

# use while loop to keep asking until the credentials are correct or user run out of tries( 5 tries)
while n != 0:
    username = input("username: ")
    password = input("password: ")
    n -= 1
    if username in database and database[username] == password:
        print("Access granted.")
        break
    elif n > 0:
        print("Incorrect. Try again.")
    else:
        print("Account locked.")