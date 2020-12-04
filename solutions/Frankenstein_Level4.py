from itertools import permutations
import string

# code = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']

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

        return all_possible_compinations

    # Decode the numbers to open the safe, 1-52 (A1 - Z2)

    def decoding_numbers(code):

        # Create the list of the uppercase letters of the alphabet with a 1 and then a 2 added
     
        alphabet = list(string.ascii_uppercase) 

        key = [item + '1' for item in alphabet] + [item + '2' for item in alphabet]

        # Decode the numbers using their list position 

        decoded_numbers = []

        for item in code:

            num = key.index(item)
            
            decoded_numbers.append(num+1)

        return decoded_numbers

    print(key_combinations() + decoding_numbers(code))
    return key_combinations() + decoding_numbers(code)