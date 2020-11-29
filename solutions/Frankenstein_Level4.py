from itertools import permutations
import string

def run(code):
    '''
    find the right 3 keys red, blue, yellow
    decode numbers from the note
    '''
    # Try out all combinations of the keys

    def key_combinations():

        colours =['red', 'yellow', 'blue']
        all_possible_compinations = []

        p = permutations(colours)
        
        for p in list(p):
            all_possible_compinations.append(p)

        print(all_possible_compinations)
        return all_possible_compinations

    key_combinations()

    # Decode the numbers to open the safe, 1-52 (A1 - Z2)

    def decoding_numbers(code):
     
        alphabet = list(string.ascii_uppercase) # Create the list of the uppercase letters of the alphabet with a 1 and then a 2 added

        key = [item + '1' for item in alphabet] + [item + '2' for item in alphabet]

        decoded_numbers = []

        for item in code:

            num = key.index(item)
            
            decoded_numbers.append(num+1)

        print(decoded_numbers)
        return decoded_numbers
    
    decoding_numbers(code)