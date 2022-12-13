'''
Check if 3 numbers are equal
'''

# initiate a variable list
ls = []

# ask user 3 times to give a number and put the three numbers in the variable ls
for i in range(3):
    i = input("Enter a number: ")
    # append each number from the user in the list
    ls.append(i)

# compare the three numbers by referencing them in the list by theor index
# if the three numbers are equal, print "Equal"
if ls[0] == ls[1] == ls[2]:
    print("Equal")
# the the three numbers are not eqial, print "Not Equal" 
else:
    print("Not Equal")
