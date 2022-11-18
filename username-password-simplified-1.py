""" Ask user for username and password 5 times. After the fifth time lock account. """

# create database
database = {
    "credentials":
    {
        "username0" : "password0",
        "username1" : "password1",
        "username2" : "password2"
    }
}

# assign variables
n = 0
username = ''
password = ''

# use while loop to keep asking until the credentials are correct or user run out of tries( 5 tries)
while n < 5:
    n += 1
    username = input("username: ")
    password = input("password: ")
    if username in database["credentials"] and password in database["credentials"][username]:
        print("\n$$$$$ ACCESS GRANTED $$$$$\n")
        break
    elif n < 5:
        print("\n   Incorrect. Try again\n")
    else:
        print("\n------- Account locked ------\n")



