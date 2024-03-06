"""
Engeto Online Python Akademie: Projekt2 - Bulls & Cows
author: Andrea Kvapilová
email: a.ndrea@centrum.cz
discord: andreakvapilova
"""

import random

def random_number_generation(number_digit: int) -> int:
    """
    The function generate a random number with defined number of digits and does not start with 0.
    """
    range_start = 10**(number_digit -1) #with number_digit = 4 start from 1000
    range_end = (10**number_digit)-1 #with number_digit = 4 end with 9999
    check_unique = False
    while check_unique is False:
        random_number = random.randrange(range_start, range_end)
        check_unique = checking_unique_symbols(str(random_number))
        if check_unique is True:
            return random_number
    
def checking_unique_symbols(input: str) -> bool:
    """
    The function checks input if all symbols are unique.
    Return False if it contains the same characters.
    """
    control_set = set(input)
    if len(input) != len(control_set):
        return False
    else:
        return True

def starting_with_zero(input: str) -> bool:
    """
    The function checks if input starts with 0.
    Return True if it starts with 0.
    """
    if input.startswith("0", 0, 1):
        print("The number starts with 0.")
        return True
    else:
        return False

def containing_nonnumeric_symbol(input: str) -> bool:
    """
    The function checks if input is numeric.
    Return True if it doesn't contain non-numeric characters.
    """
    if input.isdigit() is False:
        print("The input contains non-numeric characters.")
        return False
    else:
        return True 

def checking_len_number(number_digit: int, input: str) -> bool:
    """
    The function checks if input is the same length as the entered number of digits.
    Return False if it shorter or longer than number_digit
    number_digit: how many digits should the number contain
    insert: what input should be checked
    """
    if len(input) > number_digit:
        print("The entered number is longer.")
        return False
    elif len(input) < number_digit:
        print("The entered number is shorter.")
        return False
    else:
        return True
    
def checking_players_number(input: str, number_digit: int) -> bool:
    """
    The function checks if the input does not contain non-numeric characters, has the correct length and does not start with zero.
    Returns False if one or more of the conditions are not fulfilled.
    input: what input should be checked
    number_digit: how many digits should the number contain
    """
    checking_input = True
    if (containing_nonnumeric_symbol(input) is False 
        or checking_len_number(number_digit, input) is False 
        or starting_with_zero(input) is True):
        checking_input = False
    elif checking_unique_symbols(input) is False:
        print("The entered number contains duplicate numbers.")
        checking_input = False
    return checking_input

def creating_list_input_and_random_number(input: str, generated_random_number: int) -> list:
    """
    The function creates two sheets from the input and the generated random number.
    Returns two lists with integers- the first is list from the input and list from random number.
    """
    list_input = []
    list_random = []
    str_random_number = str(generated_random_number)
    #saving input to the list
    for index in range(len(input)):
        list_input.append(int(input[index]))
    #saving random number to the list
    for index in range(len(str_random_number)):
        list_random.append(int(str_random_number[index]))
    return list_input, list_random

def checking_bulls_and_cows(input: str, generated_random_number: int) -> bool:
    """
    The function checks if the input contains a number from generated_random_number.
    If the number is correct it counts to cows and if it matches the number and position it counts to bulls.
    Prints the muber of cows/bulls and returns False if the input is not matched with generated_random_number.
    """
    list_input, list_random = creating_list_input_and_random_number(input, generated_random_number)
    cows = 0
    bulls = 0
    #counting bulls (same position and value)
    for index in range(len(list_random)):
        if list_input[index] == list_random[index]:
            bulls += 1 
    #counting cows (only value)
    for number in list_input:
        right_number = list_random.count(number)
        cows += right_number 
    cows -= bulls #subtracting the numbers counted in the bull
    #printing number of cow/cows and bull/bulls
    cow = "cows" if cows != 1 else "cow" #condition to determine singular and plural nouns
    bull = "bulls" if bulls != 1 else "bull" #condition to determine singular and plural nouns
    if bulls != len(input):
        print(f"{bulls} {bull}, {cows} {cow}")
        return False
    else:
        return True
    
if __name__ == "__main__":
    number_digit = 4
    number_random = (random_number_generation(number_digit))
    number_insert = (input("Enter a number: "))
    print(checking_players_number(number_insert, number_digit))
    print(checking_bulls_and_cows(number_insert, number_random))
