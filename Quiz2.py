def replace_even(data):
    '''
    Replace all elements at an even index in the list with 0.
    No return is required.
    data: the list of values to process'''

    pass

# Uncomment the following lines to test
# ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# replace_even(ONE_TEN)
# print(ONE_TEN)


def remove_middle(data):
    if len(ONE_TEN) % 2 != 0:
        ONE_TEN.remove(5)
    else:
        ONE_TEN.pop(5) and ONE_TEN.pop(4)

ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)
 
'''
    Remove the middle element if the list length is odd,
    or the middle two elements if the list length is even.  
    No return is required.
    data: the list of values to process
'''
pass

# Uncomment the following lines to test
# ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# remove_middle(ONE_TEN)
# print(ONE_TEN)


def insert_integer(data, number):
    insert_integer(7,8)

data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
new_data = insert_integer(data, 2015)
print(new_data)
'''
    given a sorted list of integers, insert a new integer into
    its proper position so that the new list stays sorted. 
    Do not use sort function or sorted function inside this function.
    data: a list of integers
    number: a new integer
    return: a new list of sorted integers with previous numbers and 
    the new number
'''
pass

# Uncomment the following lines to test
# data = [1, 3, 40, 75, 90, 2000, 2001, 2016]
# new_data = insert_integer(data, 2015)
# print(new_data)


def print_hist(data):
    '''
    given a dictionary of letter: positive integer pairs, 
    print rows with the letter and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    data: a dictionary of letter: positive integer pairs
    Example:
    letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
    print_hist(letter_counts)
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
    '''
    pass
