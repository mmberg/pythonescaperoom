from EscapeRoom import EscapeRoom
from random import randint
import random


class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level3())
        self.add_level(self.create_level7())

    ### LEVELS ###
    #Level 3 Jessi#
    def create_level3(self):

        mythos = ["Kleopatra liess ihren Mann ermorden,kurz bevor ihre Ehe annulliert werden sollte, um gemeinsam mit Ihrem Sohn an die Macht zu kommen!.", 
        "Man sagt, dass Hieroglyphen soviel wie in Stein gemeißelt heisst. Die Zeichen wurden sogar vielfach farbig geschrieben und sind immer eine Bildreihe!", 
        "Nicht nur Pharaonen hatten damals so viel Macht, auch Lokalkönige waren sehr mächtig. So waren sie zuständig für all die Kleinstaaten! Beide Arten von Regenten waren allerdings sehr streng beim Aussieben von Sand!",
        "Die goettliche Legitimation beginnt mit der rituellen Aktivierung der Göttlichkeit. Das ist etwa vergleichbar mit einer Routineuntersuchung!" ,
        "Vorgänger der fünfkantigen Pyramide ist ein Mstabas, ein einstufiger und flacher Bau. Auch sie hatten bereits Kammern, die tief ins Erdreich verlagert wurden." ,
        "Pyramiden dienen als Begräbnisstätten, deren Steine sind aus Kalkstein. Die Bauwerke haben unter anderem Stollen die von Schächten abzweigen. Es gibt eine Pyramide, die während der Bauzeit fünfmal erweitert wurde! Die meisten Pyramiden sind viereckig ",
        "Cheops, der boese Pharao, zwang alle Untertanen seines Reviers beim Pyramidenbau zu helfen."  ]

        myth = random.choice(mythos)

        if myth == mythos[0]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[1]:
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[2]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[3]:
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[4]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        elif myth == mythos[5]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"
        else: 
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne mich!</b> </a>"

        

        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        code = [0,1,2,3,4,5,6,7,8,9,10,11]
                
        task_messages = [ "Juhuu, du hast den Schlüssel für die nächste Tür gefunden! Los, öffne sie und schau, was dich dahinter erwaret!",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Toroffe.jpg' width='280' height='210'>",
            "<br></br>",
            "Du stehst in einem großen Raum, mitten drin steht ein Sarkopharg! OMG!!!",
            "Du schaust dich im Raum um und entdeckst ein Gekritzel an der Wand rechts",
            "<h2><i> Kleopatra´s Mythenspiel</i></h2>",
            "<b>"+myth+"</b>",
            "<br></br>",
            "<i>Wenn Kleopatra Mythen erzählt, sie es immer <b>wörtlich</b> meint! Aber nimm dich in Acht, von klein nach groß, von unten nach oben, hast du das bedacht? </i>",
            "<br></br>",
            "Was hat denn das nun wieder zu bedeuten?",
            "<br></br>",
            schriftrolle_zu,
            "Du drehst dich im Raum und siehst dich um, am Sarkophag findest eine Schriftrolle und ein Schloss mit " + str(zahl) + " Drehscheiben!",
            schriftrolle_offen
            ]
        hints = [
            "1. Wenn du einen Mythos gefunden hast, dann lies ihn genau durch. Ganz genau.",
            "2. Nimm´s wörtlich.",
            "3. In jedem Mythos steckt mindestens eine Zahl. Vielleicht auch mehr",
            "4. Öffne die Schriftrolle! Darin ist ein Hinweis für zwei Listen enthalten",
            "5. Eine Liste besteht aus Strings, die andere aus Int",
            "6. Verwende liste1 = ['null',.....,'elf'], liste2 = [0,...,11]",
            "7. Schreibe ein Programm das anhand der Listen die du ermittelt hast, übereinstimmende Zahlen aus dem Mythos ausgibt"
            
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.mythos, "data": myth}
    
    #Level 7 Jess #
    def create_level7(self):

        bauplan = [
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

        rohbau =[]
        for i in range(len(bauplan)):
            reihe = random.choice(bauplan)
            rohbau.append(reihe)
            bauplan.remove(reihe)
                
        task_messages = [ "<h2><i>Willkommen im Raum des Greywolf!</h2></i>",
            "Während du dich im Raum umschaust entdeckst du zwei Zeichnungen an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Bauplan.jpg' width='1000' height='550'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b><i>Bitte heb mich auf</i></b> </a>",
            "<br></br>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "Auf der Rückseite siehst du folgednes Gekritzel : <a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/erklaerung.txt'target ='_blank'><b>Rückseite!</b> </a>",
            "<br></br>",
            "Um weiter zu kommen finde den Code!",
            "<button id='btn_hint'>HILFE!</button>",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schloss3.jpg' width='200' height='120'>"
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
            "9. Du musst das Wort nur noch in Zahlen übersetzen, schon bist du fertig! Aber achte auf die Zeichnung an der Wand!",
            "10. Ascii wäre ein passendes Schlagwort. Aber pass gut auf, das Schloss hat nur 3 Stellen!",
            "11. Rechne jeden einzelnen Buchstaben um und rechne alle Ergebnisse zusammen!",
            "12. Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.bauplan, "data": rohbau}

    ### SOLUTIONS ###
    #Level3
    def mythos(self, myth):
        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        zahlen = [0,1,2,3,4,5,6,7,8,9,10,11]
        code = []
        for word in zahl_in_worten:
                if (word in myth):
                    code.append(zahlen[zahl_in_worten.index(word)])
                    print(zahlen[zahl_in_worten.index(word)])
                print(code)
        return code 


    def bauplan(self,rohbau):

        #Liste reinkopieren aus txt file      
        lines = ['                /\\ ', '     /[][][]M[][][][][][][][\\ ', '       /[][]H[][][][][][][\\ ', '              /[][[\\ ', '   /[][][][][][][][]N[][][][][\\ ', '        /[][][][]C[][][][\\ ', '               /][\\ ', '      /[]A[][][][][][][][][\\ ', '         /[][][]N[][][][\\ ', '    /[]U[][][][][][][][][][][\\ ', '           /[][][]T[][\\ ', '            /[][][]U[\\ ', '          /[][][]A[][][\\ ', '             /[][]T[\\ ']

        #zählen der Steine [] & sortieren um es als richtige Pyramide auszugeben
        for i in range(len(lines)):

            lines.count("[]") 
            lines.sort()

        print("\n ")

        for i in range(len(lines)):
            print(lines[i])

        #Zeilen zu einem Eintrag zusammenführen und alles außer Buchstaben entfernen    
        letterneu = []
        for l in range(len(lines)):
            #Wortliste zusammenführen zu einem String und alles außer Buchstaben löschen
            letter = "".join(lines[l])
            letter = letter.replace("[", "")
            letter = letter.replace("]", "")
            letter = letter.replace(" ", "")
            letter = letter.replace("/", "")
            letter = letter.replace("\n", "")
            letter = letter.replace("\\", "")
            letterneu +=letter
            
        letterneu = "".join(letterneu)

        print("\nLösungswort: " + letterneu + "\n ") #Ausgabe 

        code = 0
        #Berechnen des ACSII Code für die einzelnen Buchstaben & alle zusammenrechnen = Code 840
        for i in range(len(letterneu)):   
            
            zahl = ord(letterneu[i])
            code +=zahl
        print("Lösungscode: " + str(code))


        loesungswort = "TUTANCHAMUN"
        return code,loesungswort
    

