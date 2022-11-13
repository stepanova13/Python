'''Check if 3 numbers are equal'''

ls = []

for i in range(3):
    i = input("Enter a number: ")
    ls.append(i)

if ls[0] == ls[1] == ls[2]:
    print("Equal")
else:
    print("Not Equal")
