from EscapeRoom import EscapeRoom
from random import randint
import random
import requests

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
        
        task_messages = ["Während du dich im Raum umschaust entdeckst du zwei Zeichnungen an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Bauplan.jpg' width='1000' height='550'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b>Bitte heb mich auf</b> </a>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "Auf der Rückseite siehst du folgednes Gekritzel : <a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/erklaerung.txt'target ='_blank'><b>Rückseite!</b> </a>",
            "Von oben nach unten ist es wahr, was dabei zu lesen ist, das ist klar!",
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
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": "reihen"}

    ### SOLUTIONS ###

    def sol_lv1(self):

        r = requests.get("https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt")

        print(r.content)

        #Datei einlesen
        textfile = open('pyramide.txt', 'r')
        lines = textfile.readlines()
        letter = "".join(lines)
        #print(letter)
        
        #zählen der Steine [] & sortieren um es als richtige Pyramide auszugeben
        for i in range(len(lines)):
        
            letter.count("[]") 
            lines.sort()
            
        letter="".join(lines)
        print(letter)

        #Zeilen zu einem Eintrag zusammenführen und alles außer Buchstaben entfernen    
        letterneu = []
        print("\n ")
        
        for l in range(len(lines)):
            #Wortliste zusammenführen zu einem String
            letter = "".join(lines[l])
            letter = letter.replace("[", "")
            letter = letter.replace("]", "")
            letter = letter.replace(" ", "")
            letter = letter.replace("/", "")
            letter = letter.replace("\n", "")
            letter = letter.replace("\\", "")
            letterneu +=letter

        letterneu = "".join(letterneu)
        
        print("Lösungswort: " + letterneu + "\n ") #Ausgabe N

        code = 0
        #Berechnen des ACSII Code für die einzelnen Buchstaben & alle zusammenrechnen = Code 840
        for i in range(len(letterneu)):   
        
            zahl = ord(letterneu[i])
            code +=zahl
        print("Lösungscode: " + str(code))

        textfile.close()

        loesungswort = "TUTANCHAMUN"

        return code,loesungswort
