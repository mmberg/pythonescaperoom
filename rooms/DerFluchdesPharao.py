from random import randint
import random
from EscapeRoom import EscapeRoom
import os
import sys

# %matplotlib inline 
# import matplotlib.pyplot as plt

def umwandeln_in_ascii(buchstabe):

    asci0=ord(buchstabe)

    return asci0 #gibt Zahl zurück

        
def caesar(asci):

    zahl=asci+3 #Zahl +3
    
    return zahl

def umwandeln_in_buchstabe(zahl):

    buchstabe=chr(zahl)

    return buchstabe

bilder01=["<img src='https://github.com/alex2101998/pythonescaperoom/blob/Jess/static/Bilder/wp1.jpg?raw=true' width='370' height='600'>",
    "<img src='https://github.com/alex2101998/pythonescaperoom/blob/Jess/static/Bilder/wp2.jpg?raw=true'width='370' height='600 >", 
    "<img src='https://github.com/alex2101998/pythonescaperoom/blob/Jess/static/Bilder/wp3.jpg?raw=true'width='370' height='600'>",
    "<img src='https://github.com/alex2101998/pythonescaperoom/blob/Jess/static/Bilder/wp4.jpg?raw=true'width='370' height='600'>"]

bild01 = random.choice(bilder01)

startbild = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab.jpg'  width='800' height='600'>"
cleospiel = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/ABCD.jpg'  width='800' height='600'>"


if bild01==bilder01[0]:
    code = "031"
else:
    if bild01==bilder01[1]:
        code = "130"     
    else:
        if bild01==bilder01[2]:
            code = "813"  
        else:
            if bild01==bilder01[3]:
                code = "308"  

buchstabensalat =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
random.shuffle(buchstabensalat)

buchstabe=random.choice(buchstabensalat) #zufälliger Buchstabe zwischen A-Z

buchstabe_als_ascii=umwandeln_in_ascii(buchstabe) #ergibt die passende Zahl des Buchstaben
    
zahl2=caesar(buchstabe_als_ascii)  #verschlüsselt die in Zeile 51 ausgegebene ascii Zahl

buchstabe_verschluesselt=umwandeln_in_buchstabe(zahl2)

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())
        # self.add_level(self.create_level2())

    ### LEVELS ###
    
    def create_level1(self):
        secret = ["1.Der Mensch",
                                "2.Jede Krankheit",
                                "3.Dein Aufwand",
                                "4.Der Nil",
                                "5.Die Hoffnung",
                                "6.Tabak ohne Kaffee",
                                "7.Geduld",
                                "8. Das Kamel",
                                "9. Das Schiff",
                                "10. Ein Käfer",
                                "11. Ein Mistkäfer"]
        random.shuffle(secret)  


        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Wie bist du nun ",
            "Satzanfang:", secret,
            "Zufälliger Buchstabe" , buchstabe,
            # " = " ,  buchstabe_als_ascii, # Buchstabe = Zahl
            # buchstabe_verschluesselt,  #Buchstabe 
            " =" , zahl2, #= verschlüsselte Zahl von zufälligem Buchstaben
            "<b>Der Pharao erwartet dich</b>",
            startbild + "     " + bild01,
            code,
            cleospiel,
            "Gut nun hast du vielleicht eine Zahl gefunden, aber das heißt noch lange nicht, dass du dich wo anders befindest.",
            "aber schau dich nochmal etwas um, siehst du den Käfer der da rechts auf dem Boden hockt? Geh ruhig mal näher ran"]
            
        
        hints = [
            "Findest du die passenden Sätze? Schau genau hin!",
            "Siehst du die kleine Raute? Hat sie vielleicht eine wichtige Bedeutung? Wo ist sie noch zu finden?",
            "Suche vielleicht nach den versteckten Hinweisen, irgendwo muss es doch wohl eine Übersetzungstabelle oder sowas geben?"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}
    

    

    #Level2


    # def create_level2(self):
    #     task_messages = [
    #         "Shalom, das war gut, leider bist du immer noch im gleichen Raum",
    #         "Aber schau mal da, siehst du den kleine Skarabäuskäfer der rechts von dir auf dem Boden sitzt?",
    #         "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/SkarabaeusTruhe.jpg' width='400' height='250'>"
    #     ]
    #     hints = [
    #         "Was hat es mit der Raute auf sich, siehst du etwas, das dazu passen könnte?"
    #     ]
    #     return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}


    ### SOLUTIONS ###

    def sol_lv1(self, pharao):

        return code

