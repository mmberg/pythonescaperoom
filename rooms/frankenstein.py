import random
import string
from EscapeRoom import EscapeRoom


class frankenstein(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Christoph", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level6())

    ### LEVELS ###

    def create_level1(self):            # Methode mit Tupel Int-Werte
        rectangle = random.choice([
            (1, 2, 6, 2, 6, 6, 1, 6),
            (3, 2, 7, 2, 7, 4, 3, 4),
            (3, 1, 9, 1, 9, 6, 3, 6)
        ])

        task_messages = [
            "Ein Monster wurde an vier Stellen in London gesichtet, die Menschen sind in Angst & Schrecken,",
            "du willst herausbekommen wo es herkommt.",
            "Dir fällt auf, dass die vier Orte ein Rechteck ergeben.",
            "Das Versteck des Monsters muss sich nahe des Mittelpunkts befinden",
            "Die Koordinaten sind: <b> " +
            str(rectangle)+"</b",
            "Schreibe eine Methode",
            "die aus den Koordinaten den Mittelpunkt errechnet."
        ]
        hints = [
            "Mittelpunkt eines Rechtecks",
            "Gegegben ist ein Tuple der Form (x,y,x,y,x,y,x,y)",
            "Mögliche Formel: A+1/2AD",
            "Erwartet wird eine List der Form[x,y]"

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level1, "data": rectangle}

    def create_level6(self):
        data = ("rjaa kt jv mfv gfjwgjw hjvlgniiu gnvu, mfvu kt tavjwj jfaofhj lgnalj czakza szw kjb bzavujw ot wjuuja!", 25, 13)

        task_messages = [
            "Du verstehst wie die Maschine funktioniert und stellst mit Grauen fest,",
            "dass Dr. Frankenstein hier das Monster erschaffen hat, dass in ganz London",
            "Angst und Schrecken verbreitet.",
            "Auf einem wüsten Schreibtisch findest du ein Notizbuch mit Einträgen,",
            "der letzte wurde vor einer Woche geschrieben,",
            "du kannst es aber nicht lesen, es scheint nur Buchstabensalat zu sein.",
            "Wenn du es nur entziffern könntest..."
        ]
        hints = [
            "Nutze den Code aus dem Safe um die Notiz zu entschlüsseln",
            "Schlüsselpaar",
            "inverses Element",
            "Euklidischer Algorithmus"

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level6, "data": data}

    ### SOLUTIONS ###

    def solution_level1(self, rectangle):
        m = []  # Mittelpunkt des Rechtecks - List
        # Werte aus dem Tupel mit Formel für x
        m.append(rectangle[0] + (2 / (rectangle[4] - rectangle[0])))
        # Werte aus dem Tupel mit Formel für y
        m.append(rectangle[1] + (2 / (rectangle[5] - rectangle[1])))

        return m

    def solution_level6(self, data):  # Tupel/Tripel 3 Elemente
        msg_encr = data[0]
        a = data[1]
        b = data[2]

        def decrypt(y, a_inv, b):
            return ((a_inv*(y - b)) % 26)

        def euklid(a, m):
            def ggt_euklid(a, b):
                if a == 0:
                    return (b, 0, 1)
                else:
                    ggt, y, x = ggt_euklid(b % a, a)
                    return (ggt, x - (b // a) * y, y)

            ggt, x, y = ggt_euklid(a, m)
            if ggt != 1:
                raise Exception("Es gibt kein inverses zu a modulo m")
            else:
                return x % m

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        msg = ""
        for y in msg_encr:
            if alphabet.find(y) == -1:
                msg = msg + y
            else:
                a_inv = euklid(a, 26)
                x = decrypt(alphabet.find(y), a_inv, b)
                msg = msg + alphabet[x]
        return msg  # auf msg ist nun die entschlüsselte Nachricht gespeichert
