''' Program that askes user their weight in lb and convert it in kilograms/ kg'''

body_weight_in_lb = int(input("What is your body weight in lb? \n"))
body_weight_in_kg = round(body_weight_in_lb * 0.45359237, 3) # display 3 digit decimal

print(f"Your body weight is {body_weight_in_lb} lb,\nand the equivalent in kg is: {body_weight_in_kg} kg.\nThank you!")