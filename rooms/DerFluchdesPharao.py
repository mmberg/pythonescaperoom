from random import randint
import random
from EscapeRoom import EscapeRoom

# %matplotlib inline 
# import matplotlib.pyplot as plt

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi", __name__)
        self.add_level(self.create_level1())

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
        pharao = "TUTANCHAMUN"


        def umwandeln_in_ascii(buchstabe):

            asci0=ord(buchstabe)

            return asci0

        
        def caesar(asci):

            zahl=chr(asci+3)
            
            return zahl
        
        buchstabensalat =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        random.shuffle(buchstabensalat)

        buchstabe=random.choice(buchstabensalat) #zufälliger Buchstabe zwischen A-Z

        umwandlung=umwandeln_in_ascii(buchstabe) #ergibt die passende Zahl des Buchstaben
        
        zahl2=caesar(umwandlung)  #verschlüsselt die in Zeile 51 ausgegebene ascii Zahl

             
    
        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Wie bist du nun ",
            secret,
            buchstabe,
            umwandlung,
            zahl2,
            ord("P"),
            caesar(80),
            "<b>Der Pharao erwartet dich</b>",
            "<img src='https://upload.wikimedia.org/wikipedia/commons/c/ce/Egypt_Hieroglyphe2.jpg'  width='600' height='400'>",
            " ",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/1+2.png' width='1500' height='1200'>"
        ]
        hints = [
            "Findest du die passenden Sätze? Schau genau hin!",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}
    
    

    ### SOLUTIONS ###

    def sol_lv1(self, pharao):

        pharao = "TUTANCHAMUN"
        
        return pharao

