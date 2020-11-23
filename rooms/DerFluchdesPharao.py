from EscapeRoom import EscapeRoom
from random import randint
import random


#++++++++++++++ HAUPTTEIL ++++++++++++++++++++++++

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())
        #self.add_level(self.create_level2())

    ### LEVELS ###
    
    def create_level1(self):

        # Level03 Stringfunktionen - 
        # Random Textbausteine ausgeben + #
        # Buchstaben zählen ergibt ein Codeteil & #
        # Zahlen in Text finden ergibt zweiten Codeteil & 
        # das ganze muss dann alphabetisch sortiert werden + 
        # Wörter werden rückwärts geschrieben und man muss den Text lesen 

        
        task_messages = ["Während du dich im Raum umschaust entdeckst du zwei Rätsel an einer Säule und an der Wand",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raetselxy.jpg' width='400' height='250'>",
            "auf dem Boden liegt ein zerknüllter Zettel, als du ihn öffnest siehst du folgendes:"
        
            ]

    
        
        hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
                "Umrechnen du musst! Es gibt nur 10 Ziffern um sie zu lösen"] 


        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": }
    
    

#   # Level2


#     def create_level2(self):

        
#         liste = [" AB, ", "CD"]

#         task_messages = [
#             "Shalom, das war gut, leider bist du immer noch im gleichen Raum",
#             "Aber schau mal da, siehst du den kleine Skarabäuskäfer der rechts von dir auf dem Boden sitzt?",
#             "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raetselxy.jpg' width='400' height='250'>"
#         ]
#         hints = [
#             "Was hat es mit der Raute auf sich, siehst du etwas, das dazu passen könnte?"
#         ]
#         return {"task_messages": task_messages, "hints": hints, "solution_function": "self.remove_vowels", "data": liste}


#     ### SOLUTIONS ###

#     def sol_lv1(self, pharao):
        
#         code = bin(code_gesamt)

#         return code

