""" 
This program asks for username and password and check if they are correct. 
User has 5 tries. After fifth try print "Account locked" 

Created By  : stepanova13
"""

# create database
database = {
    "credentials":
    {
        "John101" : "dj1005$jd",
        "Anna222" : "stinm94563%443",
        "Peter404" : "pjpassword500"
    },
    "employees":
        [{"firstName" : "John", "lastName" : "Doe"},
        {"firstName" : "Anna", "lastName" : "Smith"}, 
        {"firstName" : "Peter", "lastName" : "Jones"}],
}

# initializing the variable for the number of tries
n = 0

# use while loop to keep asking until the credentials are correct or user runs out of tries( 5 tries)
while n < 5:
    n += 1
    username = input("username: ")
    password = input("password: ")
    if username in database["credentials"] and password in database["credentials"][username]:
        print("\n$$$$$ ACCESS GRANTED $$$$$\n")
        break
    elif n < 5:
        print("Incorrect. Try again")
    else:
        print("Account locked")



