# mapping
def is_greater_than_5(numbers:list) -> list:
    '''Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5'''

    return list(map(lambda x: x>5, numbers))

# filtering
def filter_less_than_5(numbers:list)->list:
    '''Given an list of numbers, return a list of numbers that are less than 5'''

    return list(filter(lambda x: x<5, numbers))

# aggregation with filtering
def sum_of_two_digit_numbers(numbers:list):
    '''Given a list of numbers find the sum of all two_digit_numbers.
    '''

    return sum(filter(lambda x: len(str(x))==2, numbers))

# aggregation with mapping
def is_all_has_a(words:list)->bool:
    '''Given a list of words check if all words has the letter a(case insensitive) in it.
    '''

    return all(map(lambda x: 'a' in x.lower(), words))

# enumerate
def print_with_numbering(items): 
    '''
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    '''

    for i, value in enumerate(items,1):
        print(f"{i}. {value}")

# zip
def parallel_print(countries, capitals):
    '''
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    '''

    for country, capital in zip(countries, capitals):
        print(f"{country} - {capital}")

# key value list to dict
def make_dict(keys, values):
    '''Create a dict with keys and values'''

    return dict(zip(keys,values))

# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    '''Given a list of words, find the indices of the big words(length greater than 5).
    '''

    return list(map(
      lambda x: x[0], # taking only the indices
      filter(lambda y: len(y[1])>5, enumerate(words)) # filtering with size
    ))

# zip with mapping and aggregation
def decode_rle(chars:str, repeats:list)->str:
    '''
    Create a string with i-th char from chars repeated i-th value of repeats number of times. 

    Note rle refers to Run-length encoding
    '''

    return "".join(map(lambda x: x[0]*x[1], zip(chars, repeats)))
