''' Ask for username and password and check if they are correct. 
    User has 5 tries. After fifth try print "Account locked" '''

# create database
database = [{"username" : "Mike", "password" : "Mike123$"},
            {"username" : "Joe", "password" : "Joseph^pass17"},
            {"username" : "Lilly", "password" : "flowerRose654"},
            {"username" : "May", "password" : "pas#4532H"}
            ]

# initializing variables
username = ' '
password = ' '
# ask user for username and password
enter_username = ''
enter_password = ''
# number of tries the user is allowed to type username and passowrd
n = 5
access_granted = bool()

# ask user for username and password
while enter_username != username or enter_password != password:
    enter_username = input("Please enter your username: ")
    enter_password = input("Please enter your password: ")
    # if username and password wrong, decrease the number of left tries by 1
    n -= 1
    # check if entered username and password match the respective username and password in database
    for i in database:
        username = i["username"]
        password = i["password"]
        # if credentials correct, grant access and stop
        if enter_username == username and enter_password == password:
            access_granted = True
            print("Access granted")
            break
    # if number of tries less than 5 and bigger than zero, and access not granted, print "Incorrect credentials. Please try again."
    if   5 > n > 0 and access_granted == False:
        print("Incorrect credentials. Please try again.")
    # if number of tries is equel to zero, and access to granted, lock account
    elif n == 0 and access_granted == False:
        print("Account locked")
        break
