''' 
Get Max and Min values 

Created By  : stepanova13
'''

list_of_numbers = []
numbers_count = int(input("How many numbers do you want to compare? "))

for i in range(numbers_count):
    i = int(input("Type a number: "))
    list_of_numbers.append(i)

# if numbers_count == 0:
# if len(list_of_numbers) == 0:
if list_of_numbers == []:
    print("None")
else:
    print(f"{max(list_of_numbers)} {min(list_of_numbers)}")
   
        





