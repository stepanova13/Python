""" Display the lastname of the second employee"""

d = {
  "employees":[{"firstName" : "John", "lastName" : "Doe"},
                {"firstName" : "Anna", "lastName" : "Smith"}, 
                {"firstName" : "Peter", "lastName" : "Jones"}],

  "owners":[{"firstname": "Jack", "lastName": "Petter"},
            {"firstName": "Jessy", "lastName": "Petter"}]
    }

print(d["employees"][1]['lastName'])
