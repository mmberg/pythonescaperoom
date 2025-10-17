import random
import string
from EscapeRoom import EscapeRoom


class UtesRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Ute", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    ### LEVELS ###

    def create_level1(self):
        rnd_number = 8
        # rnd_number1 = random.randrange(1, 10)
        task_messages = [
            "Hier steht die Aufgabe des ersten Levels: ",
            "Löse die folgende Gleichung: <b>" +
            str(rnd_number)+" als Quadratzahl </b>",
        ]
        hints = [
            "Lösungshinweis"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.add_rnd_numbers, "data": rnd_number}

    def create_level2(self):
        task_messages = [
            "Text des zweiten Levels"
        ]
        hints = [
            "Lösungsheinweis",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.remove_vowels, "data": "Vokale verboten"}

    ### SOLUTIONS ###

    def add_rnd_numbers(self, rnd_number):
        result_sqrt = 0
        result_sqrt = rnd_number*rnd_number
        return result_sqrt

    def remove_vowels(self, word):
        result = ""
        vowels = ["a", "e", "i", "o", "u"]
        for c in word:
            if not c in vowels:
                result = result + c
        return result
