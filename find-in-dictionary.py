""" 
Display the last name of the second employee 
"""

d = {
  "employees":[{"firstName" : "John", "lastName" : "Doe"},
                {"firstName" : "Anna", "lastName" : "Smith"}, 
                {"firstName" : "Peter", "lastName" : "Jones"}],

  "owners":[{"firstname": "Jack", "lastName": "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]
    }

# from dictionary 'd' select 'emplyees' which is a list of dictionaries
# select the second element - {"firstName" : "Anna", "lastName" : "Smith"}, it has index 1
# select the key 'lastName'
print(d["employees"][1]['lastName'])
