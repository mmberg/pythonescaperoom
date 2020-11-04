from random import randint
import random
from EscapeRoom import EscapeRoom

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

bilder01=["<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp1.png' width='370' height='600'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp2.png'width='370' height='600 >", 
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp3.png'width='370' height='600'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/wp4.png'width='370' height='600'>"]

bild01 = random.choice(bilder01)

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


wortraestel = ["<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Einstein.jpg' width='1000' height='600'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Personen.jpg' width='1000' height='600' >", 
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Meinung.jpg' width='1000' height='600'>",
    "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schnuller.jpg' width='1000' height='600'>"]

zufallssatz=random.choice(wortraestel)

if zufallssatz==wortraestel[0]:
    wode = "328"
else:
    if zufallssatz==wortraestel[1]:
        wcode = "210"     
    else:
        if zufallssatz==wortraestel[2]:
            wcode = "185"  
        else:
            if zufallssatz==wortraestel[3]:
                wcode = "1411"  

startbild = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab.jpg'  width='800' height='600'>"


hintsPersonen = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        "Lies rückwärts...",
        "Den zweiten Code findest du in den Worten, schau genau hin!!",
        "Findest du ein Wort, das DREIstigkeit ist? Dann solltest du auch den Rest finden",
        "328, mano man das war zäh!"
        ]

# def hints(hint):
#     if zufallssatz==wortraestel[0]:
#         hints = hintsPersonen
#     else:
#         hints=["Layer8"]
    
#     return hints




buchstabensalat =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
buchstabenspiel = ["D vor B", "A hinter C", "C tauscht mit D", "B vor A"]
random.shuffle(buchstabensalat)
#random.shuffle(buchstabenspiel)

#bspiel = random.choice(buchstabenspiel)

buchstabe=random.choice(buchstabensalat) #zufälliger Buchstabe zwischen A-Z

buchstabe_als_ascii=umwandeln_in_ascii(buchstabe) #ergibt die passende Zahl des Buchstaben
    
zahl2=caesar(buchstabe_als_ascii)  #verschlüsselt die in Zeile 51 ausgegebene ascii Zahl

buchstabe_verschluesselt=umwandeln_in_buchstabe(zahl2)

endboss = str(code + wcode)

class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())
        # self.add_level(self.create_level2())

    ### LEVELS ###
    
    def create_level1(self):
    
        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Wie bist du hierher geraten und wie kommst du wieder raus?",
            "Um dich herum stehen lauter komische Dinge an den Wänden",
            "Wenn Kleopatra schreibt, dann sie immer nur von h..... denkt" , 
            "D vor B",
            "<small><i>Hilfe! Ich bin in einer Grabkammer erwacht und weiß nicht, wie ich hier rauskomme!</i></small>",
            "wir schreiben MMDL vor Christus! Auch wenn das jetzt römisch ist aber wer auch immer das nach mir liest, ich weiß aus zuverlässiger Quelle, dass Tutanchamun hier mit <b>Cäsar</b> verwandt war/ist was auch immer! ",
            startbild + "     " + bild01,
            "<small><i>Du musst dich nicht wundern, manche Sätze machen hier keinen Sinn</i></small>",
            code,
            zufallssatz,
            wcode,
            "Nanu, was haben denn diese komischen Zeichen zu bedeuten?"
            ]

    
        
        hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
                "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
                "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
                "Lies rückwärts...",
                "Den zweiten Code findest du in den Worten, schau genau hin!!",
                "Findest du ein Wort, das eine Zahl enthält? Dann solltest du auch den Rest finden",
                "328, mano man das war zäh!"] 




        # if zufallssatz==wortraestel[0]:
        #     hints = ["Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #             "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #             "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #             "Lies rückwärts...",
        #             "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #             "Findest du ein Wort, das DREIstigkeit ist? Dann solltest du auch den Rest finden",
        #             "328, mano man das war zäh!"
        #           ]
        # else:
        #     if zufallssatz==wortraestel[1]:
        #         hints = [
        #                     "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                     "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                     "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                     "Lies rückwärts...",
        #                     "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                     "Findest du ein Wort, das ZWEItrangig ist? Dann solltest du auch den Rest finden",
        #                     "210, mano man das war zäh!"
        #             ]     
        #     else:
        #         if zufallssatz==wortraestel[2]:
        #             hints = [
        #                         "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                         "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                         "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                         "Lies rückwärts...",
        #                         "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                         "Findest du ein Wort, das überEINStimmst ist? Dann solltest du auch den Rest finden",
        #                         "185, mano man das war zäh!"
        #                     ] 
        #         else:
        #             if zufallssatz==wortraestel[3]:
        #                 hints = [
        #                                 "Du siehst die Grabkammer, daneben ein komisches Bild mit halbierter Schrift. Findest du eine Gemeinsamkeit? Was hat diese wohl zu bedeuten? Ergibt das etwa einen Sinn?",
        #                                 "Als nächstes suchst du versteckte Botschaften. Kann es sein, dass vor dir jemand die alten Zeichen übersetzt hat?",
        #                                 "War Kleopatra nicht bekannt für ihre schön gemalten Zeichen? Ich meine irgendwo eine ihrer Spielregeln gelesen zu haben...",
        #                                 "Lies rückwärts...",
        #                                 "Den zweiten Code findest du in den Worten, schau genau hin!!",
        #                                 "Findest du ein Wort, das EINStein ist? Dann solltest du auch den Rest finden",
        #                                 "1411, mano man das war zäh!"
        #                         ]   
        #             else:
        #                 hints = ["ERROR"]


     
          
        

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": bild01}
    

    

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
        
        

        return endboss

