
from random import randint

from EscapeRoom import EscapeRoom

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###
    
    def create_level1(self):
        secret = randint(0, 2222)
        pharao = "TUTANCHAMUN"

        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Wie bist du nun ",
            secret,
            "<b>Der Pharao erwartet dich</b>",
            "<img src='https://upload.wikimedia.org/wikipedia/commons/c/ce/Egypt_Hieroglyphe2.jpg'  width='600' height='400'>",
            " ",
            secret,
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/tut_8.jpg' width='600' height='400'>"
        ]
        hints = [
            "Findest du die passenden Sätze? Schau genau hin!",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}
    
    
    def create_level2(self):

        task_messages = [
            "Bist du immer noch hier?",
        ]
        hints = [
            "Findest du die passenden Sätze? Schau genau hin!",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}


    ### SOLUTIONS ###

    def sol_lv1(self, pharao):

        if pharao != "TUTANCHAMUN":
            print("FALSCH")
        else:
            print("Super! Es öffnet sich die nächste Tür!")
        
        pharao = "TUTANCHAMUN"
        
        return pharao
