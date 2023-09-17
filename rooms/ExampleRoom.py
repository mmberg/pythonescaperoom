import random
import string
from EscapeRoom import EscapeRoom

class ExampleRoom(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Markus", __name__)
        self.add_level(self.create_level1())

    ### LEVELS ###

    def create_level1(self):
        secret = random.choice(["Sogar Einige Clowns Riechen Es Tagelang",
                                "Gangster Erkennen Heimliche Essenzen In Mails"])

        task_messages = [
            "Auf einem Zettel steht folgender Text:",
            "<b>"+secret+"</b>",
            "Lässt sich hier ein Geheimnis erahnen?",
            # "<img src='static/secret.jpg'/>"
        ]
        hints = [
            "Werfen Sie einen Blick auf die Anfangsbuchstaben!"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.first_letters, "data": secret}

    ### SOLUTIONS ###

    def first_letters(self, secret):
        words = secret.split(" ")
        result = ""
        for word in words:
            result += word[0]
        return result
