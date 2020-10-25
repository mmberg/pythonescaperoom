import string
from itertools import combinations,product

doorbell = "Dr. VXktXr FrXnkXstXXn"

def get_combinations_and_position(doorbell):
    vowels_alphabetical_order = ["a","e","i","o","u"]
    doorbell_solution = "Dr. Viktor Frankenstein"
    doorbell_solution_vowels = []
    ##Extract vowels of solution
    for character in doorbell_solution:
        ##If vowel add to vowel list
        if character in vowels_alphabetical_order:
            doorbell_solution_vowels.append(character)

    ##Using itertools.product to generate a list of all possible combinations
    combination_list = list(product(vowels_alphabetical_order,repeat=len(doorbell_solution_vowels)))
    position_counter = 1
    ##Now finding the position of the correct vowel order/combination
    for c in combination_list:
        position_counter = position_counter + 1
        if tuple(doorbell_solution_vowels) == c:
            print(position_counter)
            return position_counter
            
    return 

get_combinations_and_position(doorbell)
        
