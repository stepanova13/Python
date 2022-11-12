'''Check if 3 numbers are queal'''

ls = []

for i in range(3):
    number = input("Enter a number: ")
    ls.append(number)

if ls[0] == ls[1] == ls[2]:
    print("Equal")
else:
    print("Not Equal")