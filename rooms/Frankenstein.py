import random
import string
from EscapeRoom import EscapeRoom

##Lib for Level 2 solution
from itertools import product


class Frankenstein(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Lisa, Christoph und Thomas", __name__)
        #self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())

    ### LEVELS ###

    #def create_level1(self):
    #    pass
    #    return

    def create_level2(self):
        doorbell = "Dr. VXktXr FrXnkXstXXn"
        task_messages = [
            "Du findest an dem errechneten Ort eine verfallene Stadtvilla mit \
            einem unleserlichen Namen an der Klingel: " +doorbell+ 
            " Die Vokale sind unkenntlich. Nachdem Du geklinglt hast, antwortet eine \
            mystische Stimme \"Wer klingelt an einer Klingel, ohne den Namen lesen zu \
            können?\" fragte die Stimme und fuhr nach eine kurzen Pause fort \"Vielleicht \
            verrate ich Dir den Namen. Doch dafür musst Du etwas tun. Erstelle eine Liste \
            mit allen möglichen Kombinationen. Gehe alphabetisch vor! Wie Du siehst fehlen \
            ja nur Vokale...aber es wird trotzdem eine lange Liste...HARHARHAR!! Wenn sie \
            vollständig ist und der richtige Name an der gleichen Postion wie auf meiner \
            Liste steht, verrate ich ihn dir...\" " 
        ]
        hints = [
            "Oje, so viele Kombinationen... probiere es trotzdem! Ersetze die X jeweils mit den \
            bekannten Vokalen \"a,e,i,o,u\"",
            "Mit jedem Einsetzen erhältst Du eine neue Kombiantion. Diese Kombination solltest Du \
            jeweils deiner Liste hinzufügen. ",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_combinations_and_position, "data": "Vokale verboten"}


    def create_level3(self):

        task_messages = ["message here"]

        hints = ["hints here"]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.create_badge_number, "data": "Scotland Yard Badge"}

    ### SOLUTIONS ###

    ###Level 2###
    def get_combinations_and_position(self, doorbell):
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
    ###END Solution Level 2    

    ###Level 3###

    def create_badge_number(self):
        '''
        create a badge number with format xxx-xxx-xxx
        requirements per block of 3: cross sum is between 9 and 15, the digits are digits
        '''

        def unique_digits(a):                                       # function to check uniqueness of digits in a number

            digits = [int(i) for i in str(a)]

            if digits[0] == digits[1]:
                return False
            
            elif digits[0] == digits[2]:
                return False

            elif digits[1] == digits[0]:
                return False

            else:
                return True

        def cross_sum(a):                                           # function to calculate the cross sum

            cross_sum_digits = [int(i) for i in str(a)]

            return sum(cross_sum_digits)

        numbers = []                                              # list of three digit numbers for the badge number

        import random

        while len(numbers) < 3:                                  # while we have less than 3 items in the list

            x = random.randint(101,998)                             # get random 3 digit number

            if unique_digits(x) == True:                            # check if all digits are unique

                if cross_sum(x) >= 9 and cross_sum(x) <= 15:        # check if cross sum is 9

                    numbers.append(x)                             # add number to ints list

            else:
                continue

        badge_number = '-'.join(map(str, numbers))
        
        print(badge_number)
        return badge_number

    ###END Solution Level 3 
