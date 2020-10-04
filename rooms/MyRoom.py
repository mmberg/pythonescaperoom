import random
import string
from EscapeRoom import EscapeRoom


class MyRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Markus", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        mysterious_letters = self.random_letters()

        task_messages = [
            "In einer verborgenen Ecke siehst du ein Display und einen Knopf. Bei jedem Knopfdruck erscheint eine andere Buchstabenfolge. "
            "Was hat es damit wohl auf sich?",
            "Die Buchstabenfolge lautet: <b>"+mysterious_letters+"</b",
            "Hinter einem an der Wand aufgehängten Bild siehst du nun ein Eingabepanel für einen 6-ziffrigen Code.",
            "Schreibe eine Methode <code>run('"+mysterious_letters +
            "')</code>, die aus den Buchstaben den richtigen Code erzeugt."
        ]
        hints = [
            "Wie kann aus 3 Buchstaben ein 6-stelliger numerischer Code abgeleitet werden?",
            "Wie lautet der ASCII Code für einen Buchstaben?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_number_from_letters, "data": mysterious_letters}

    def create_level2(self):
        task_messages = [
            "Nach der korrekten Eingabe des Codes wird nun geheimnisvolle Musik abgespielt und eine Stimme sagt mehrfach: 'Vokale verboten'"
        ]
        hints = [
            "Wie lautet der Spruch 'Vokale verboten' wenn Vokale verboten sind?",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}

    def random_letters(self):
        letters = ""
        for _ in range(3):
            letters = letters + random.choice(string.ascii_uppercase)
        return letters

    ### SOLUTIONS ###

    def get_number_from_letters(self, letters):
        numberstring = ""
        for c in letters:
            numberstring = numberstring + str(ord(c))
        return numberstring

    def remove_vowels(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result
