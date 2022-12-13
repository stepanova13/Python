'''
 even-numbers-multiplier.py: multiplies even numbers from a list of numbers
 
 Created By  : stepanova13
'''
# global variable 'Numbers' holds a list of whole numbers
Numbers = [8, 9, 11, 20, 32, 101, 100]

# defining the function
def multiply_even_numbers(list):
    ''' 
    this function multiplies the even numbers from a list
    args: list(a list of numbers)
    returns: int
    '''
    # assigne local variable 'product' to initiate the calculation of the product
    product = 1
    # iterate over the list of numbers to take the even numbers and multiply them 
    for i in list:
        if i % 2 == 0:
            product *= i
    return product

# body of the main
if __name__ == '__main__':
    try:
        print(f"The product of all even numbers in the list is: {multiply_even_numbers(Numbers)}")
    
    # handle exceptions 
    except Exception as error:
        print(f"There is an error: {error}")

