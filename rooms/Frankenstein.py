import random
import string
from EscapeRoom import EscapeRoom

from itertools import permutations
from itertools import product

class Frankenstein(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Lisa, Christoph und Thomas", __name__)
        #self.add_level(self.create_level1())
        #self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level4())
        #self.add_level(self.create_level5()))
        #self.add_level(self.create_level6())

    ### LEVELS ###

    def create_level1(self):            # Methode mit Tupel Int-Werte
        rectangle = random.choice([
            (1, 2, 6, 2, 6, 6, 1, 6),
            (3, 2, 7, 2, 7, 4, 3, 4),
            (3, 1, 9, 1, 9, 6, 3, 6)
        ])

        task_messages = [
            "Ein Monster wurde an vier Stellen in London gesichtet, die Menschen sind in Angst & Schrecken,",
            "du willst herausbekommen wo es herkommt.",
            "Dir fällt auf, dass die vier Orte ein Rechteck ergeben.",
            "Das Versteck des Monsters muss sich nahe des Mittelpunkts befinden",
            "Die Koordinaten sind: <b> " +
            str(rectangle)+"</b",
            "Schreibe eine Methode",
            "die aus den Koordinaten den Mittelpunkt errechnet."
        ]
        hints = [
            "Mittelpunkt eines Rechtecks",
            "Gegegben ist ein Tuple der Form (x,y,x,y,x,y,x,y)",
            "Mögliche Formel: A+1/2AD",
            "Erwartet wird eine List der Form[x,y]"

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level1, "data": rectangle}

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

    def create_level4(self):

            def create_random_code():

                alphabet = list(string.ascii_uppercase) # Create the list of the uppercase letters of the alphabet with a 1 and then a 2 added

                code_numbers = [item + ‘1’ for item in alphabet] + [item + ‘2’ for item in alphabet]

                random_code = []

                for _ in range(0, 6):
                    code.append(random.choice(code_numbers))

                return random_code

        code = create_random_code()

        task_messages = ["message here"]

        hints = ["hints here"]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.open_safe, "data": code}

    def create_level6(self):
            data = ("rjaa kt jv mfv gfjwgjw hjvlgniiu gnvu, mfvu kt tavjwj jfaofhj lgnalj czakza szw kjb bzavujw ot wjuuja!", 25, 13)

            task_messages = [
                "Du verstehst wie die Maschine funktioniert und stellst mit Grauen fest,",
                "dass Dr. Frankenstein hier das Monster erschaffen hat, dass in ganz London",
                "Angst und Schrecken verbreitet.",
                "Auf einem wüsten Schreibtisch findest du ein Notizbuch mit Einträgen,",
                "der letzte wurde vor einer Woche geschrieben,",
                "du kannst es aber nicht lesen, es scheint nur Buchstabensalat zu sein.",
                "Wenn du es nur entziffern könntest..."
            ]
            hints = [
                "Nutze den Code aus dem Safe um die Notiz zu entschlüsseln",
                "Schlüsselpaar",
                "inverses Element",
                "Euklidischer Algorithmus"

            ]
            return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level6, "data": data}

    ### SOLUTIONS ###

    ###Level 1###

    def solution_level1(self, rectangle):
    m = []  # Mittelpunkt des Rechtecks - List
    # Werte aus dem Tupel mit Formel für x
    m.append(rectangle[0] + (2 / (rectangle[4] - rectangle[0])))
    # Werte aus dem Tupel mit Formel für y
    m.append(rectangle[1] + (2 / (rectangle[5] - rectangle[1])))

    return m

    ###END Solution Level 1

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
        requirements per block of 3: cross sum is between 9 and 15, the digits are unique
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

    ###Level 4###

    def open_safe(self, code):
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

    ###END Solution Level 4

    ###Level 6###

        def solution_level6(self, data):  # Tupel/Tripel 3 Elemente
        msg_encr = data[0]
        a = data[1]
        b = data[2]

        def decrypt(y, a_inv, b):
            return ((a_inv*(y - b)) % 26)

        def euklid(a, m):
            def ggt_euklid(a, b):
                if a == 0:
                    return (b, 0, 1)
                else:
                    ggt, y, x = ggt_euklid(b % a, a)
                    return (ggt, x - (b // a) * y, y)

            ggt, x, y = ggt_euklid(a, m)
            if ggt != 1:
                raise Exception("Es gibt kein inverses zu a modulo m")
            else:
                return x % m

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        msg = ""
        for y in msg_encr:
            if alphabet.find(y) == -1:
                msg = msg + y
            else:
                a_inv = euklid(a, 26)
                x = decrypt(alphabet.find(y), a_inv, b)
                msg = msg + alphabet[x]
        return msg  # auf msg ist nun die entschlüsselte Nachricht gespeichert

    ###END Solution Level 6