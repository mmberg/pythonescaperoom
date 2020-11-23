from EscapeRoom import EscapeRoom
from random import randint
import random

class DieGrabkammerdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###
    
    def create_level1(self):
        secret = randint(0, 2222)

        task_messages = ["Während du dich im Raum umschaust entdeckst du zwei Zeichnungen an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Raetselxy.jpg' width='1000' height='550'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b>Bitte heb mich auf</b> </a>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "Hat das eventuell etwas mit der Zeichnung an der Säule zu tun?"
            
            ]
        hints = [
            "Auf dem zerknüllten Papier ist ein Bauplan zu sehen, leider ist etwas durcheinander geraten. Versuche doch, ihn zi sortieren",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}

    ### SOLUTIONS ###

    def sol_lv1(self, secret):
        return "1234"