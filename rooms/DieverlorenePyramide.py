from EscapeRoom import EscapeRoom
from random import randint

class DieverlorenePyramide(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###
    
    def create_level2(self):
        secret = randint(0, 2222)

        task_messages = [
            "Du wachst auf und fühlst dich noch etwas benommen. Du schaust dich um, aber erkennst nichts wieder..",
            "Du merkst, dass du inmitten einer alten Pyramide bist. Wie bist du nun ",
            "Rechne bitte 1+3, was wird wohl das Ergebnis sein....",
            secret,
            "<b>Der Pharao erwartet dich</b>",
            "<img src='C:\Users\jessi\OneDrive\Dokumente\GitHub\Pictures\1.jpg'  width='300' height='200'>"
        ]
        hints = [
            "Der erste Tipp das sag ich dir, wird nicht leicht zu verstehen! Aber schau doch eher mal die rechte Hälfte an um zu verstehen",
            "World"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}
    
    
  

    ### SOLUTIONS ###

    def sol_lv1(self, secret):

        a = 1
        b = 3

        return a+b
