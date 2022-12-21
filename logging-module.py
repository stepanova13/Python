'''
logging-module.py: this code writes an error message in a log file 

Created By  : stepanova13
'''

import logging

logging.basicConfig(filename='Python\logging-module.log', filemode='w', level=logging.INFO)
logger = logging.getLogger()

#logger.info('msg')

def division(a, b):
    '''
    this function divides two nembers
    args: a(int), b(int)
    return: int
    '''
    try:
        c = a/b
    except Exception as error:
        logger.error(f'The operation is not feasible because of {error}')
        return False
    return c

if __name__ == '__main__':
    x = 10
    y = 0
    
    # execute the division
    division(x, y)