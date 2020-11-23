from EscapeRoom import EscapeRoom
from random import randint
import random

reihen = [
        "                /\ ",
        "               /][\ ",
        "              /[][[\ ",
        "             /[][]T[\ ",
        "            /[][][]U[\ ",
        "           /[][][]T[][\ ", 
        "          /[][][]A[][][\ ", 
        "         /[][][]N[][][][\ ", 
        "        /[][][][]C[][][][\ ",
        "       /[][]H[][][][][][][\ ", 
        "      /[]A[][][][][][][][][\ ", 
        "     /[][][]M[][][][][][][][\ ", 
        "    /[]U[][][][][][][][][][][\ ", 
        "   /[][][][][][][][]N[][][][][\ "]
        
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
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Bauplan.jpg' width='1000' height='550'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b>Bitte heb mich auf</b> </a>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "<br></br>",

            ]
        hints = [
            "1. Auf dem zerknüllten Papier ist ein Bauplan zu sehen, leider ist etwas durcheinander geraten.",
            "2. Der Bauplan ist für eine Pyramide! Versuche ihn zu sortieren!",
            "3. Jede Reihe hat eine aufsteigende Anzahl von [], das sollte hilfreich sein!",
            "4. Wenn du erfolgreich sortiert hast, solltest du ein Wort erkennen können!",
            "5. Leider ist mit dem Wort noch nicht Schluss, beachte die zweite Zeichnung an der Wand!",
            "6. Du solltest ein Lösungswort mit 11 Stellen erhalten haben, davon musst du manche tauschen oder löschen",
            "7. Beim Ersetzen solltest du den Ascii Code des Buchstabens verwenden um den neuen Buchstaben zu ermitteln!",
            "8. Die erste Lösung ist TUTANCHAMUN!",
            "9. Du musst das Wort nur noch in Zahlen übersetzen, schon bist du fertig"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": reihen}

    ### SOLUTIONS ###

    def sol_lv1(self):

        #Datei einlesen
        file = open('pyramide.txt', 'r')
        print("\nFolgende Inhalte wurden gelesen:\n")
        for line in file:
            print(line.strip("\n")) #DAteiinhalte drucken in Zeilen ohne leere Zeile
        
        print("\nHier kommt die sortierte Pyramide: \n")

        for i in range(len(reihen)):
            
            reihen[i].count("[]") #zählen der Steine []
            print(reihen[i])

        letterneu = []
        print("\n ")
        for i in range(len(reihen)):
            #Wortliste zusammenführen zu einem String
            letter = "".join(reihen[i])
            letter = letter.replace("[", "")
            letter = letter.replace("]", "")
            letter = letter.replace(" ", "")
            letter = letter.replace("/", "")
            letter = letter.replace("\\", "")
            letterneu +=letter

            letterneu = "".join(letterneu)

        print("Lösungswort: " + letterneu + "\n ") #Ausgabe N

        code = 0
        #Berechnen des ACSII Code für die einzelnen Buchstaben & alle zusammenrechnen = Code 840
        for i in range(len(letterneu)):   #Also wird hier nur der ASci von N berechnet
        
            zahl = ord(letterneu[i])
            code +=zahl
        print("Lösungscode: " + str(code))

        file.close()

        return code