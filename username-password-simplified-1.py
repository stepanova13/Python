""" Ask user for username and password 5 times. After the fifth time lock account. """

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

# assign variables
n = 0
username = ''
password = ''

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



