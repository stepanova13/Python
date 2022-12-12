''' 
sales.py: this code returns the total sum a client owes in a supermarcet in a receipt file
Created By  : stepanova13
'''

# items in an order with prices
order = {
        'tomato' : 30,
        'thyme' : 4.50,
        'garlic' : 7.5,
        'rice' : 10,
        'onions' : 4,
        'fish' : 9.99,
        'radish' : 5.59
}

# return the sum of all values as a string
total = str(sum(order.values()))

def receipt():
        ''' 
        this function creats a file
        args: None
        return: boolean
        '''
        with open('Python\\receipt.txt', 'w') as file:
                file.write('================= RECEIPT =================\n\n')
                file.write('The TOTAL SUM of your order is: $')
                file.write(total)
        return True

# body of the main
if __name__ == '__main__':
        try:
                # call the function
                receipt()
        
        # handle exceptions
        except TypeError:
                print("You had a typo.")
        except MemoryError:
                print("You ran out of memory. Try to delete some objects.")
        except KeyError:
                print("A mapping (dictionary) key is not found in the set of existing keys.")
        except Exception as error:
                print(f"There is an error: {error}")
        




