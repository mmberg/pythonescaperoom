import random
import string
import datetime
from EscapeRoom import EscapeRoom

##Lib for Level 2 solution
from itertools import product


class Frankenstein(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Lisa, Christoph und Thomas", __name__)
        #self.add_level(self.create_level1())
        self.add_level(self.create_level5())
        #self.add_level(self.create_level3())
        #self.add_level(self.create_level4())
        self.add_level(self.create_level2())
        #self.add_level(self.create_level6())

    ### LEVELS ###

    def create_level1(self):
       pass
       return

    def create_level2(self):
        doorbell = "Dr. VXktXr FrXnkXnstXXn"
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
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_combinations_and_position, "data": doorbell}


    def create_level5(self):

        d = datetime.datetime.now()
        d_num_raw = d.strftime("%d" "%m" "%Y")
        d_num = list(map(int, str(d_num_raw)))

        static_chars = [
            "|⁻^^⁻⁻^⁻^⁻⁻^|",
            "|*=≠≠≠==*|",
            "|" + "&nbsp" * 17 + "|",
            "|< ⊛ : ⦻ >|",
            "|⊡--" + "&nbsp" * 7 + "▫" + "&nbsp" * 8 + "--⊡|",
            "|" + "&nbsp" * 14 + "|",
            "| ▭▭▭ |",
            "|_______|",
        ]



        task_messages = [
            "•" * d_num[0] + "·" * 6 + static_chars[0],
            "•" * d_num[1] + "·" * 6 + static_chars[1],
            "•" * d_num[2] + "·" * 6 + static_chars[2],
            "•" * d_num[3] + "·" * 6 + static_chars[3],
            "•" * d_num[4] + static_chars[4],
            "•" * d_num[5] + "·" * 7 + static_chars[5],
            "•" * d_num[6] + "·" * 7 + static_chars[6],
            "•" * d_num[7] + "·" * 7 + static_chars[7],
            "&nbsp",
            str(d_num_raw),
            "&nbsp",
            "Was ist das für ein seltsames Bild? Sieht irgendwie aus, als wäre es zeilenweise verschoben... Und was hat diese \
            Zahl in Reihe 10 zu bedeuten? Scheinbar ändert sie sich jeden Tag etwas... ",
            "Es sind 8 Zahlen und das Bild besteht aus 8 Reihen. Wie kannst Du es wieder richtig zusammensetzen?"
        ]
        hints = [
            "Wie hängt die 8-stellige Zahl mit den 8 Zeilen des Bildes zusammen? Um wieviele Positionen musst\
            Du die Zeilen jeweils verschieben, so dass das Bild wieder richtig zusammengesezt ist?",
            "\"Verschieben\" heisst in dem Fall, dass Du etwas entfernen solltest. Gebe am Ende nur die 8 korrekt\
            ausgerichteten Zeilen aus.",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.realign_picture, "data": task_messages}



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
    ###END Solution Level 2   

    ###Level 5###     
    def realign_picture(self, task_messages):
        ###Put the misaligned picture into fresh array (only first 10 lines)
        picture_lines = task_messages[0:10]
        ###Create empty array to put the realigned lines into
        aligned_picture_lines = []
        ###Now we have to convert the number in line 9 to a list of numbers
        date_from_picture = list(map(int, str(picture_lines[9])))
        ###Lets iterate throug the misaligned lines by using enumerate in order to match the index to Number index of line 9
        for i, elem in enumerate(picture_lines[0:8]):
            ###Make sure to convert each line to  list to make sure we can proper remove elements 
            picture_line = list(picture_lines[i])
            ###Removing the number of first elements depending on the number which is given in number list from line 9
            del picture_line[:date_from_picture[i]]
            ###Add the aligned line to the realigned lines array after converting it back to string
            picture_line = ''.join(picture_line)  
            aligned_picture_lines.append(str(picture_line))

        return aligned_picture_lines
        ###End solution Level 5###
