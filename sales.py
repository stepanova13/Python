''' This code returns the total sum a client owes in a supermarcet in a receipt text'''

# items in an order with prices
order = {
        'tomato' : 30,
        'thyme' : 4.50,
        'garlic' : 7.5,
        'rice' : 10,
        'onions' : 4,
        'fish' : 9.99
}

# return the sum of all values as a string
total = str(sum(order.values()))

def receipt(text):
    with open('Python\\receipt.txt', 'a') as file:
            file.write(text)

line1 = 'The TOTAL SUM of your order is: $'

# call the function
receipt(line1)
receipt(total)



