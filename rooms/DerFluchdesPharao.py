from EscapeRoom import EscapeRoom
from random import randint
import random


#++++++++++++++ HAUPTTEIL ++++++++++++++++++++++++

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###
    
    def create_level1(self):

        # Level03 Stringfunktionen - 
        # Random Textbausteine ausgeben + #
        # Buchstaben zählen ergibt ein Codeteil & #
        # Zahlen in Text finden ergibt zweiten Codeteil & 
        # das ganze muss dann alphabetisch sortiert werden + 
        # Wörter werden rückwärts geschrieben und man muss den Text lesen 

        ganzoben = "            ^ "
        spitze = "           /_\\"
        steine = [ "          /_T_\ ", "         /__U__\ ", "        /___T___\ ","       /____A____\ ", "      /_____N_____\ ", 
        "     /______C______\ ", "    /_______H_______\ ", 
        "   /________A________\ ", "  /_________M_________\ ", " /__________U__________\ ","/___________N___________\ "]

        print(ganzoben)
        print(spitze)

        def pyramide_bauen(self):

            f = file('pyramide.txt', 'w')
            
            i = 0
            for i in range(11):
                stein = random.choice(self)
                f.write(stein)
            return stein

        def count_spaces(string):
            i = 0
            for i in range(11):
                print(string[i].count(" "))

            return string

        pyramide_bauen(steine)
        count_spaces(steine)

#Frage wie lautet das Lösungswort und wie viele Leerzeichen beinhaltet



        
        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Aber wie kommst du hier raus?",
            wortsalat

            ]

    
        
        hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
                "Umrechnen du musst! Es gibt nur 10 Ziffern um sie zu lösen"] 


        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": }
    
    

  # Level2


    def create_level2(self):

        
        liste = [" AB, ", "CD"]

        task_messages = [
            "Shalom, das war gut, leider bist du immer noch im gleichen Raum",
            "Aber schau mal da, siehst du den kleine Skarabäuskäfer der rechts von dir auf dem Boden sitzt?",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/SkarabaeusTruhe.jpg' width='400' height='250'>"
        ]
        hints = [
            "Was hat es mit der Raute auf sich, siehst du etwas, das dazu passen könnte?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": "self.remove_vowels", "data": liste}


    ### SOLUTIONS ###

    def sol_lv1(self, pharao):
        
        code = bin(code_gesamt)

        return code

