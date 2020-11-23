from EscapeRoom import EscapeRoom
from random import randint
import random

f = open('pyramide.txt', 'w')

stein = ["[]"]

reihen = [
"                /\ ",
"               /][\ ",
"              /[][[\ ",
"             /[][]T[\ ",
"            /[][][]U[\ ",
"           /[][][]T[][\ ", 
"          /[][][]A[][][\ ", 
"         /[][][]N[][][][\ ", 
"        /[][][][]C[][][][\ ",
"       /[][]H[][][][][][][\ ", 
"      /[]A[][][][][][][][][\ ", 
"     /[][][]M[][][][][][][][\ ", 
"    /[]U[][][][][][][][][][][\ ", 
"   /[][][][][][][][]N[][][][][\ "]


#Steine zählen Stein = []
def count_block(string):
    i = 0
    for i in range(len(string)):
        
        bloecke=string[i].count("[]")
        #f.write(str(bloecke)+"\n")

    return string

count_block(reihen)


#Pyramide wird random gemischelt und sicher gestellt, dass jeder Eintrag genau einmal ausgegeben wird (.remove)
def built_pyramide(reihen):
    i = 0
    for i in range(len(reihen)):
        reihe = random.choice(reihen)
        reihen.remove(reihe)
        f.write(str(reihe)+"\n")
    
    return reihe

built_pyramide(reihen)

class DieGrabkammerdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###
    
    def create_level1(self):
        secret = randint(0, 2222)

            
        # f = open('pyramide.txt', 'w')

        # stein = ["[]"]

        # reihen = [
        # "                /\ ",
        # "               /][\ ",
        # "              /[][[\ ",
        # "             /[][]T[\ ",
        # "            /[][][]U[\ ",
        # "           /[][][]T[][\ ", 
        # "          /[][][]A[][][\ ", 
        # "         /[][][]N[][][][\ ", 
        # "        /[][][][]C[][][][\ ",
        # "       /[][]H[][][][][][][\ ", 
        # "      /[]A[][][][][][][][][\ ", 
        # "     /[][][]M[][][][][][][][\ ", 
        # "    /[]U[][][][][][][][][][][\ ", 
        # "   /[][][][][][][][]N[][][][][\ "]


        # #Steine zählen Stein = []
        # def count_block(string):
        #     i = 0
        #     for i in range(len(string)):
                
        #         bloecke=string[i].count("[]")
        #         #f.write(str(bloecke)+"\n")

        #     return string

        # count_block(reihen)


        # #Pyramide wird random gemischelt und sicher gestellt, dass jeder Eintrag genau einmal ausgegeben wird (.remove)
        # def built_pyramide(reihen):
        #     i = 0
        #     for i in range(len(reihen)):
        #         reihe = random.choice(reihen)
        #         reihen.remove(reihe)
        #         f.write(str(reihe)+"\n")
            
        #     return reihe
        
        # built_pyramide(reihen)

        task_messages = ["Während du dich im Raum umschaust entdeckst du zwei Rätsel an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raetselxy.jpg' width='1000' height='550'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel, als du ihn öffnest siehst du folgendes:"
        
            ]
        hints = [
            "Hello",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}

    ### SOLUTIONS ###

    def sol_lv1(self, secret):
        return "1234"