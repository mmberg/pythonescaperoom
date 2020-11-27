import string
from itertools import combinations,product

def run(doorbell):
    vowels_alphabetical_order = ["a","e","i","o","u"]
    doorbell_solution = "Dr. Viktor Frankenstein"
    doorbell_solution_vowels = []
    for character in doorbell_solution:
        ##If vowel add to vowel list
        if character in vowels_alphabetical_order:
            doorbell_solution_vowels.append(character)

    combination_list = list(product(vowels_alphabetical_order,repeat=len(doorbell_solution_vowels)))
    position_counter = 1
    for c in combination_list:
        position_counter = position_counter + 1
        if tuple(doorbell_solution_vowels) == c:
            print(position_counter)
            return position_counter
