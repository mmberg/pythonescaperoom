import random
import string
from EscapeRoom import EscapeRoom

#123

class ExampleRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Markus", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###

    def create_level1(self):
        task_messages = [
            "Die nächste Tür öffnet sich erst, wenn du dem Wärter die Lösung der Gleichung verrätst. Der Wärter zeigt dir folgendes Papyrus: ",
            "<img src='static/assets/1.png'>",

            "Du erinnerst dich aus dem Geschichtsunterricht, wie die Umrechnung von Ägyptischen Hieroglyphenzeichen in Arabische Zahlen funktioniert",
            "Diese Grafik schwebt dir in Erinnerung:",
            "<img src='static/assets/hieroglypische_zahlzeichen.PNG'>"
        ]
        hints = [
            
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.first_letters, "data": ""}

    ### SOLUTIONS ###

    def first_letters(self, secret):
        words = secret.split(" ")
        result = ""
        for word in words:
            result += word[0]
        return result
