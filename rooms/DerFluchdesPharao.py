from EscapeRoom import EscapeRoom
from random import randint
import random


class DerFluchdesPharao(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Alex, Isi, Jessi, Laura", __name__)
        self.add_level(self.create_level4())
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level5())
        self.add_level(self.create_level6())
        self.add_level(self.create_level7())
        self.add_level(self.create_level8())

    #################
    ### LEVELS ###
    #################

    #   Level 1 Isabelle
    def create_level1(self):
        liste = [ "Pyramide" , "Kleopratra" , "Python" , "Rätsel" , "Gizeh" , "Ausgang" , "Auf" , "Sand" , "Raus" , 
                "Hilfe" , "Katze" , "Wüste" , "Ausweg" , "zu" , "Käfer" , "Ägypten" , "Programmierkönig" , "Schlange" , "Katze" ,
                "Level" , "Room" , "next" , "Heilig" , "Exit" , "Isis" , "zwei" , "Ende" ]
        task_messages = [
            "Sei gegrüßt, Spieler. Du träumst nicht, das ist die Realität. Du bist gefangen in",
            "dieser Pyramide. Acht Level sollst du bestreiten und siegen, dann lasse ich dich",
            "heraus. Verlierst Du, bleibst du auf ewig gefangen. Zeige mir, ob du ein wahres Progratier",
            "bist und ich lasse dich heraus.",
            "Scheiterst du, so bleibst Du gefangen.",
            "Einen kleinen Tipp habe ich für dich: Lösungssatz: 6-13-18-24"
        ]
        hints = []
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": liste}

    #   Level 2 Laura
    def create_level2(self):

        rndNumber = randint(2, 1000)

        task_messages = [
            "Gratuliere, du hast Level 1 erfolgreich gelöst.",
            "Das nächste Level wird anspruchsvoller und du musst folgende Aufgabe lösen.",
            "Programmiere mittels While-Schleifen die Primzahlen von 2 bis dem Wert deiner Zufallszahl.",
            "Deine Zufallszahl lautet: " + str(rndNumber)
        ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv2, "data": rndNumber} 

    #   Level 3 Jessi
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
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne diese Schriftrolle!</b> </a>"
        elif myth == mythos[3]:
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne diese Schriftrolle!</b> </a>"
        elif myth == mythos[4]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne diese Schriftrolle!</b> </a>"
        elif myth == mythos[5]:
            zahl = 3
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab3Schriftrolle.jpg'target ='_blank'><b>Öffne diese Schriftrolle!</b> </a>"
        else: 
            zahl = 2
            schriftrolle_zu = "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2.jpg' width='900' height='550'>"
            schriftrolle_offen = "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Grab2Schriftrolle.jpg'target ='_blank'><b>Öffne diese Schriftrolle!</b> </a>"

        

        #zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        #code = [0,1,2,3,4,5,6,7,8,9,10,11]
                
        task_messages = [ "Du bist im nächsten Raum gelandet, genauer gesagt in der <h1> Grabkammer des Pharao´s</h1>",
            "Du schaust dich im Raum um und entdeckst einen Sarkopharg und folgendes Rätsel:",
            "<h2><i> Kleopatra´s Mythenspiel</i></h2>",
            "<b><font size = '4'><b>"+myth+"</b></font>",
            "<br></br>",
            "<b> Die Spielregeln </b>",
            "<i>Wenn Kleopatra Mythen erzählt, sie es immer <font size = '4'><b>wörtlich</b></font> meint! Aber nimm dich in <b><font size = '4'>8</font></b>, von klein nach groß, von unten nach oben, hast du das bed<b><font size = '4'>8? </i>",
            "<br></br>",
            "Du drehst dich im Raum und siehst dich um, am Sarkophag findest eine Schriftrolle und ein Schloss mit " + str(zahl) + " Drehscheiben!",
            "<br></br>",
            schriftrolle_zu,
            "<br></br>",
            schriftrolle_offen,
            "<br></br>",
            "Was steht auf der Notiz? Sieht aus wie zweierlei Listen?! Welche Verbindung mag das haben?"

            ]
        hints = [
            "1. Wenn du einen Mythos gefunden hast, dann lies ihn genau durch. Dabei jedes EINzelne Wort ganz genau.",
            "2. Nimm´s wörtlich.",
            "3. In jedem Mythos steckt mindestens eine Zahl. Vielleicht auch mehr",
            "4. Öffne die Schriftrolle! Darin ist ein Hinweis für zwei Listen enthalten",
            "5. Eine Liste besteht aus Strings, die andere aus Int",
            "6. Verwende liste1 = ['null',.....,'elf'], liste2 = [0,...,11]",
            "7. Schreibe ein Programm das anhand der Listen die du ermittelt hast, übereinstimmende Zahlen aus dem Mythos ausgibt"
            
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv3, "data": myth}
    
    #   Level 4 Alex
    def create_level4(self):
        data = "static/assets/Csv.csv"
        task_messages = [
            "Auswerten einer CSV Datei"
            ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv4, "data": data} 

    #   Level 5 Isabelle
    def create_level5(self):
    
        alphabet = 'abcdefghijklmnopqrstuvwxyz' 
        result = "" 

        key = 2
        ver_nachricht = "fw fcthuv kp ngxgn ugeju"

        task_messages = [
            "Cleopatra erscheint Dir und spricht zu Dir: Mein geliebter Caesar wollte dir helfen, doch ich kann seine komische",
            "Nachricht nicht lesen. Kannst du sie erkennen? Er sagte mir nur, Du schaffst das in <b>zwei</b> Schritten..." ,
            "Das hier ist die geheime Nachricht die dir helfen soll: " + ver_nachricht , 
        ]
        hints = [ "Du brauchst alle 26..." ,
        "Wie viele Buchstaben hat doch das Alphabet"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution5, "data": ver_nachricht}

      #   Level 8 Alex
    
    #   Level 6 Laura
    def create_level6(self):

        task_messages = [
            "Hello"
        ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv6, "data": ""} 
    
    #   Level 7 Jessi
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
                
        task_messages = [ "<h2>Willkommen in der Kammer des <i>Greywolf!</h2></i>",
            "Während du dich im Raum umschaust entdeckst du zwei Zeichnungen an einer Säule und an der Wand",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Bauplan.jpg' width='1500' height='1000'>",
            "<br></br>",
            "Auf dem Boden liegt ein zerknüllter Zettel","<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt'target ='_blank'><b><i>Bitte heb mich auf</i></b> </a>",
            "<br></br>",
            "Du entknüllst den Zettel und siehst eine seltsame Zeichnung, sind da etwa Buchstaben eingraviert?!",
            "Auf der Rückseite siehst du folgednes Gekritzel : <a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/erklaerung.txt'target ='_blank'><b>Rückseite!</b> </a>",
            "<br></br>",
            "Du siehst zwei Türen, eine ist mit 3 Schlössern gesichert, <i> na toll </i>, die zweite ist einen Spalt geöffnet, vorsichtig schaust du, was sich hinter der Tür verbirgt ",
            "Es scheint eine Art Schatzkammer zu sein, sind hier drin vielleicht die Schlüssel für die andere Tür versteckt?",
            "<br></br>",
            "<img src='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Schatzkammer.jpg' width='1500' height='1000'>",
            "<br></br>",
            "Es scheint, als müsstest du gleich 3 Rätsel lösen um diesem Raum zu entkommen!",
            "<br></br>",
            "Du gehst wieder in den großen Raum und fängst an dich nach Hinweisen umzusehen!",
            "<br></br>",
            "An einer Wand steht:" + "<i>Schau dich um! Du darfst alles verwenden was du hier findest!",
            "<br></br>",
            "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/DasBildvomSarg.txt'target ='_blank'><b>Ich könnte nützlich sein!</b> </a>",
            "<br></br>",
            "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Tal%20der%20Koenige.jpg'target ='_blank'><b>Ich könnte auch nützlich sein!</b> </a>",
            "<br></br>",
            "<a href='https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/DateinamenKopierenSollstDu.txt'target ='_blank'><b>Ich helfe dir zum Schluss!</b> </a>",
            
            ]
        hints = [
            "Auf dem zerknüllten Papier ist ein Bauplan zu sehen, leider ist etwas durcheinander geraten.",
            "Der Bauplan ist für eine Pyramide! Versuche ihn zu sortieren!",
            "Jede Reihe hat eine aufsteigende Anzahl von [], das sollte hilfreich sein!",
            "Wenn du erfolgreich sortiert hast, solltest du ein Wort erkennen können!",
            "Leider ist mit dem Wort noch nicht Schluss, beachte die zweite Zeichnung an der Wand!",
            "Du solltest ein Lösungswort mit 11 Stellen erhalten haben",
            "Lies von oben nach unten, es ist ein bekannter Pharao! Dessen Sarg haben wir heute schon Mal gesehen!",
            "Die erste Lösung ist TUTANCHAMUN!",
            "Die zweite ergibt nur 3 Stellen. Siehst du die Rechenoperatoren an der Wand?",
            "Du sollst alle Buchstaben umwandeln in deren ASCII Code, danach alle zusammen rechnen. Voilá eine 3 stellige Zahl!",
            "Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "Die dritte Lösung musst du suchen, nimm die Handnotiz als Hilfe!",
            "Rechne jeden einzelnen Buchstaben um und rechne alle Ergebnisse zusammen!",
            "Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "Hast du das Geheimnis schon gefunden? Es hieß doch, du darfst alles verwenden! Hast du dir auch alles angeschaut? Die Datei, die nützlich erschien, ist es definitiv! Du musst nur hinschauen!",
            "Hast du weit genug nach oben geschaut? Also ganz nach oben.",
            "Das Geheimnis ist, wo die Grabstätte gefunden wurde. Suche nach dem Ort!",
            "Manchmal muss man über den Tellerrand schauen!",
            "Wie wäre es, wenn du einfach den Dateinamen nimmst, der dir angezeigt wird? Jetzt gilt es nur noch, diese richtig auszulesen, ohne störende Zeichen, ohne %20, ohne Endung..."
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv7, "data": rohbau}

    #   Level 8 Alex
    def create_level8(self):

        task_messages = [
            "Du hast bisher alle Hindernisse und Rätsel erfolgreich überwunden. Eine letzte Aufgabe steht dir noch ",
            "im Weg, bevor du wieder in die Freiheit entlassen wirst.",

        ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv8, "data": "myth"} 

    #################
    ### SOLUTIONS ###
    #################

    #Level 1
    def sol_lv1(self, liste):
        satz = [6,13,19,25]
        meineLoesung = ""

        for i in range(len(liste)):
            if i in satz:
                meineLoesung+= liste[i]
        return meineLoesung

    #Level 2
    def sol_lv2(self, data):
        i = 2
        solutionArray=[]
        while (i<data):
            p=2
            while (p<= (i/p)):
                if not (i%p): 
                    break
                p=p+1
            if (p> (i/p)):
                solutionArray.append(i)
            i=i+1
        return solutionArray

    #Level3
    def sol_lv3(self, myth):
        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        zahlen = [0,1,2,3,4,5,6,7,8,9,10,11]
        code = []
        for word in zahl_in_worten:
                if (word in myth):
                    code.append(zahlen[zahl_in_worten.index(word)])
                    print(zahlen[zahl_in_worten.index(word)])
                print(code)
        return code 

    # Level 4
    def sol_lv4(self, data):
        count = 0
        with open(data, 'r') as file:
            for line in file:
                    dates = str(line).split(",")[1].split("-")
                    duratrion = int(dates[0])-int(dates[1])
                    if(duratrion >= 30):
                        count += 1
        return count

    def sol_lv7(self,rohbau):

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

        #geheimnis = "Tal der Koenige" 

        dir = "https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Tal%20der%20Koenige.jpg"

        geheimnis = dir.split('\\').pop().split('/').pop().rsplit('.', 1)[0] 
        geheimnis = geheimnis.replace('%20', " ")
        print("Das Grab von " + loesungswort + " liegt im " + geheimnis)
        print("Mit dem Lösungswort " + loesungswort + " dem Geheimnis " + geheimnis + " kannst du die beiden Schlösser an der Wand und auf dem Boden öffnen, zum Vorschein kommen 2 Schlüssel")
        print("Der Code " + str(code) + " knackt das letzte Schloss und der fehlende Schlüssel liegt jetzt auch in deiner Hand!")
        print("Schnell, geh zur verschlossenen Tür und öffne sie!")

        return code, loesungswort, geheimnis

    #Level5

    def solution5(self, ver_nachricht):

        alphabet = 'abcdefghijklmnopqrstuvwxyz' 
        result = "" 

        key = 2 
        ver_nachricht = "fw fcthuv kp ngxgn ugeju" 


        for line in ver_nachricht: 
            line = line.lower() 
            for letter in line: 
                index = alphabet.find(letter) 
                if index == -1: 
                    result = result + letter
                else:
                        new_index = index - key 
                        new_index = new_index % len(alphabet)  
                        result = result + alphabet[new_index] 

        print (result)      
    
       #Level 2
    def sol_lv6(self, data):
            return 0
    # Level 8
    def sol_lv8(self, data):
        return 0

        return result


    

