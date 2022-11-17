''' Ask for username and password and check if they are correct. 
    User has 5 tries. After fifth try print "Account locked" '''

database = [{"username" : "Mike", "password" : "Mike123$"},
            {"username" : "Joe", "password" : "Joseph^pass17"},
            {"username" : "Lilly", "password" : "flowerRose654"},
            {"username" : "May", "password" : "pas#4532H"}
            ]

username = ' '
password = ' '
enter_username = ''
enter_password = ''
n = 5
access_granted = bool()

while enter_username != username or enter_password != password:
    enter_username = input("Please enter your username: ")
    enter_password = input("Please enter your password: ")
    n -= 1
    for i in database:
        username = i["username"]
        password = i["password"]
        if enter_username == username and enter_password == password:
            access_granted = True
            print("Access granted")
            break
    if   5 > n > 0 and access_granted == False:
        print("Incorrect credentials. Please try again.")
    elif n == 0 and access_granted == False:
        print("Account locked")
        break
