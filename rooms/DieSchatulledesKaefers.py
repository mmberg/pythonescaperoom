from EscapeRoom import EscapeRoom
from random import randint

class DieSchatulledesKaefers(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Jessi", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###
    
    def create_level1(self):
        secret = randint(0, 2222)

        task_messages = [
            "Gut nun hast du vielleicht eine Zahl gefunden, aber das heißt noch lange nicht, dass du dich wo anders befindest.",
            "aber schau dich nochmal etwas um, siehst du den Käfer der da rechts auf dem Boden hockt? Geh ruhig mal näher ran",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/SkarabaeusTruhe.jpg'  width='300' height='200'>"
                    ]

        hints = [
            "Siehst du die kleine Raute? Hat sie vielleicht eine wichtige Bedeutung? Wo ist sie noch zu finden?",
            "Suche vielleicht nach den versteckten Hinweisen, irgendwo muss es doch wohl eine Übersetzungstabelle oder sowas geben?"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": secret}

    ### SOLUTIONS ###

    def sol_lv1(self, secret):
        return "1234"