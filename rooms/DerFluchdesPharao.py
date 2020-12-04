from EscapeRoom import EscapeRoom
from random import randint
import random
import cv2
import numpy as np


class DerFluchdesPharao(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("Alexander Kempf, Isabelle Beisler, Jessica Seltzer, Laura Kaltenbrunner", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())
        self.add_level(self.create_level6())
        self.add_level(self.create_level7())
        self.add_level(self.create_level8())
        self.add_level(self.create_level9())

    #################
    #### LEVELS #####
    #################

    #   Level 1 Isabelle
    def create_level1(self):
        liste = [ "Pyramide" , "Kleopratra" , "Python" , "Rätsel" , "Gizeh" , "Ausgang" , "Auf" , "Sand" , "Raus" , 
                "Hilfe" , "Katze" , "Wüste" , "Ausweg" , "zu" , "Käfer" , "Ägypten" , "Programmierkönig" , "Schlange" , "Katze" ,
                "Level" , "Room" , "next" , "Heilig" , "Exit" , "Isis" , "zwei" , "Ende" ]
        task_messages = [
            "<h2>Die Liste des Pharao</h2>",
            "Sei gegrüßt, Spieler. Du träumst nicht, das ist die Realität. Du bist gefangen in",
            "dieser Pyramide. Acht Level sollst du bestreiten und siegen, dann lasse ich dich",
            "heraus. Verlierst Du, bleibst du auf ewig gefangen. Zeige mir, ob du ein wahres Progratier",
            "bist und ich lasse dich heraus.",
            "</br>"
            "Scheiterst du, so bleibst Du gefangen. Es sei dir eine Liste gegeben die neumoderne Wörter enthält.",
            "Kombiniere die Wörter geschickt, um den Lösungssatz zu erfahren!",
            "<ul><li>Die erste Zahl lässt sich durch 2 und durch 3 teilen</li><li>Die zweite Zahl ist eine Unglückszahl</li><li>Die Wertigkeit der dritte Zahl ist 3 mal so hoch ist wie die erste Zahl</li><li>Die Prophezeiung des Pharos besagt, dass in einer unbekannten Anzahl von Jahren an diesem Tag ein heiliges Kind auf die Welt kommen wird. Dieser Tag ist die vierte Zahl.</li></ul>",
            "</br>",
            "*<code>input_data</code> des Levels ist die Liste."
        ]
        hints = [
            "1. Die Zahlen könnten die Positionen der Wörter sein...", 
            "2. Einen kleinen Tipp habe ich für dich: <b>Lösungssatz: 6-13-18-24</b>"
            ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv1, "data": liste}

    #   Level 2 Laura
    def create_level2(self):

        rndNumber = randint(2, 1000)

        task_messages = [
            "<h2>Der Geist des Pharao</h2>"
            "Plötzlich taucht der Geist des Pharao auf. Er nennt dir eine Zufällige Zahl: ",
            "<b><p style='font-size: 30'>"+ str(rndNumber)+ "</p></b>",
            "Der Geist verlangt die Anzahl der Primzahlen, die sich zwischen 2 und der Zufallszahl befinden,",
            "ansonsten wird er dich nicht gehen lassen und mit in sein Grab nehmen!"
            "</br>",
            "*<code>input_data</code> des Levels ist die Zufallszahl."
        ]

        hints = [
            "1. Versuche es mit der While-Schleife",
            "2. Die Lösung ist die Ansammlung aller Werte"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv2, "data": rndNumber} 

    #   Level 3 Jessica
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

                
        task_messages = [ "Du bist im nächsten Raum gelandet, genauer gesagt in der <h2> Grabkammer des Pharao´s</h2>",
            "Du schaust dich im Raum um und entdeckst einen Sarkopharg und folgendes Rätsel:",
            "<h3><i> Kleopatra´s Mythenspiel</i></h3>",
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
            "Was steht auf der Notiz? Sieht aus wie zweierlei Listen?! Welche Verbindung mag das haben?",
            "</br>",
            "*<code>input_data</code> des Levels ist der Mythos."

            ]
        hints = [
            "1. Wenn du einen Mythos gefunden hast, dann lies ihn genau durch. Dabei jedes EINzelne Wort ganz genau.",
            "2. In jedem Mythos steckt mindestens eine Zahl. Vielleicht auch mehr",
            "3. Öffne die Schriftrolle! Darin ist ein Hinweis für zwei Listen enthalten",
            "4. Eine Liste besteht aus Strings, die andere aus Int",
            "5. Verwende liste1 = ['null',.....,'elf'], liste2 = [0,...,11]",
            "6. Schreibe ein Programm das anhand der Listen die du ermittelt hast, übereinstimmende Zahlen aus dem Mythos ausgibt"
            
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv3, "data": myth}
    
    #   Level 4 Alexander
    def create_level4(self):
        data = "static/assets/Csv.csv"
        task_messages = [
            "<h2>Die Ahnentabelle</h2>"
            "Du bist nun im vierten Raum angekommen und siehst auf der Wand eine Tabelle von allen Pharaonen.",
            "Die Liste ist so aufgebaut, dass in einer Spalte der Name steht und in der anderen Spalte, von wann bis wann dieser Pharo regiert hat.",
            "Beim Blick auf die Tabelle wird dir schwarz vor Augen..",
            "In einem Traum siehst du den Pharao Amasis. Er erzählt dir von seiner Herrschaft, die bereits über 30 Jahre andauert.",
            "Nun wundert er sich, wie viele Pharaonen dieses bisher auch erreicht haben.",
            "</br>",
            "*<code>input_data</code> des Levels ist der Pfad der csv-Datei mit der Tabelle."
            ]

        hints = [
            "1. Die Jahresdaten sind alle vor Christus",
            "2. Vielleicht erwachst du aus dem Traum, wenn du ihm dies mitteilst.",
            "3. Lies die csv Datei aus..",
            "4. Beachte, dass beide Jahreszahlen gespeichert sind. Beispiel: 640-610"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv4, "data": data} 

    #   Level 5 Isabelle
    def create_level5(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz' 
        result = "" 
        key = 2
        ver_nachricht = "fw fcthuv kp ngxgn ugeju"

        task_messages = [
            "<h2>Caesars geheime Nachricht</h2>"
            "Cleopatra erscheint Dir und spricht zu Dir: Mein geliebter Caesar wollte dir helfen, doch ich kann seine komische",
            "Nachricht nicht lesen. Kannst du sie erkennen? Er sagte mir nur, Du schaffst das in <b>zwei</b> Schritten..." ,
            "Das hier ist die geheime Nachricht die dir helfen soll: " + ver_nachricht, 
            "</br>",
            "*<code>input_data</code> des Levels ist die verschlüsselte Nachricht."
        ]
        hints = [ 
            "1. Du brauchst alle 26..." ,
            "2. Wie viele Buchstaben hat noch das Alphabet...",
            "3. Übersetze die geheime Botschaft mit dem zweier Schlüssel"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv5, "data": ver_nachricht}

    #   Level 6 Laura
    def create_level6(self):
        task_messages = [
            "<h2>Der einsame Sohn des Pharao</h2>"
            "Mehr als die Hälfte hast du bereits geschafft.",
            "Nun... konzentriere dich jetzt besonders auf deine nächste Aufgabe.",
            "Im Jahre ..... v. Chr. kam Pharao Necho II. nach dem Tod seines Vaters an die Macht.",
            "Wir wollen wissen welches Jahr v. Chr. ist gesucht???",
            "Stelle die FIBONACCI-Folge dar, wiederhole diese aber nur 16 Mal.",

            "Am Ende werden wir sehen, ob du die korrekte Jahreszahl ermittelt hast."
        ]

        hints = [
            "1. Die gesuchte Zahl ist nicht 377 und auch nicht 987",
            "2. Die ersten fünf Zahlen der Folge sind.. 0 1 1 2 3 5 8"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv6, "data": ""} 
    
    #   Level 7 Jessica
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
                
        task_messages = [ 
            "<h2>Willkommen in der Kammer des <i>Greywolf!</h2></i>",
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
            "</br>",
            "*<code>input_data</code> des Levels ist die Liste 'soeindurcheinander'."
            ]

        hints = [
            "1. Auf dem zerknüllten Papier ist ein Bauplan zu sehen, leider ist etwas durcheinander geraten.",
            "2. Der Bauplan ist für eine Pyramide! Versuche ihn zu sortieren!",
            "3. Jede Reihe hat eine aufsteigende Anzahl von [], das sollte hilfreich sein!",
            "4. Wenn du erfolgreich sortiert hast, solltest du ein Wort erkennen können!",
            "5. Leider ist mit dem Wort noch nicht Schluss, beachte die zweite Zeichnung an der Wand!",
            "6. Du solltest ein Lösungswort mit 11 Stellen erhalten haben",
            "7. Lies von oben nach unten, es ist ein bekannter Pharao! Dessen Sarg haben wir heute schon Mal gesehen!",
            "8. Die erste Lösung ist TUTANCHAMUN!",
            "9. Die zweite ergibt nur 3 Stellen. Siehst du die Rechenoperatoren an der Wand?",
            "10. Du sollst alle Buchstaben umwandeln in deren ASCII Code, danach alle zusammen rechnen. Voilá eine 3 stellige Zahl!",
            "11. Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "12. Die dritte Lösung musst du suchen, nimm die Handnotiz als Hilfe!",
            "13. Rechne jeden einzelnen Buchstaben um und rechne alle Ergebnisse zusammen!",
            "14. Jetzt reicht es aber mit Hinweisen! 840 Herrje! Was für eine schwache Rätselleistung Meister!",
            "15. Hast du das Geheimnis schon gefunden? Es hieß doch, du darfst alles verwenden! Hast du dir auch alles angeschaut? Die Datei, die nützlich erschien, ist es definitiv! Du musst nur hinschauen!",
            "16. Hast du weit genug nach oben geschaut? Also ganz nach oben.",
            "17. Das Geheimnis ist, wo die Grabstätte gefunden wurde. Suche nach dem Ort!",
            "18. Manchmal muss man über den Tellerrand schauen!",
            "19. Wie wäre es, wenn du einfach den Dateinamen nimmst, der dir angezeigt wird? Jetzt gilt es nur noch, diese richtig auszulesen, ohne störende Zeichen, ohne %20, ohne Endung..."
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv7, "data": rohbau}

    #   Level 8 Alexander
    def create_level8(self):

        koord = [29.978, 31.134]
        data = [
            'static/assets/1.png',
            'static/assets/10.png',
            'static/assets/100.png',
            'static/assets/1000.png',
            'static/assets/10000.png',
            'static/assets/29978.png',
            'static/assets/31134.png'
        ]

        task_messages = [
            "<h2>Die mysteriösen Koordinaten</h2>"
            "Du hast bisher alle Hindernisse und Rätsel erfolgreich überwunden. Eine letzte Aufgabe steht dir noch ",
            "im Weg, bevor du wieder in die Freiheit entlassen wirst.",
            "Du findest auf dem Boden eingezeichnet etwas, was aussieht wie Koordinaten..",
            "Leider nur sind diese in Ägyptischen Zahlen eingezeichnet: ",
            "</br>",
            "<b>Erster Teil der Koordinaten: ",
            "<img src='static/assets/29978.png'>",
            "</br>",
            "<b>Zweiter Teil der Koordinaten: ",
            "<img src='static/assets/31134.png'>",
            "</br>",
            "<code>*input_data des Levels ist ein Array von Pfaden, die zu den einzelnen Bildateien gehören.",
            "<code>* 1. Eintrag: Bild für 1",
            "<code>* 2. Eintrag: Bild für 10",
            "<code>* 3. Eintrag: Bild für 100",
            "<code>* 4. Eintrag: Bild für 1000",
            "<code>* 5. Eintrag: Bild für 10000",
            "<code>* 6. Eintrag: Bild des ersten Teils der Koordinaten",
            "<code>* 7. Eintrag: Bild des zweiten Teils der Koordinaten"
        ]

        hints = [
            "1. Ein Beispiel die Umrechnung der Zahlen: </br><img width='300' height='300' src='static/assets/example.png'>",
            "2. Es wird ein Array in der Form erwarter [ersteKoordinatenZahl, zweiteKoordinatenZahl]"
        ]

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv8, "data": data} 

    #   Level 9 - Abschlusslevel
    def create_level9(self):

        task_messages = [
            "<img src='static/Bilder/Solved.jpg'>",
            "Um das Spiel abzuschließen, erstelle eine Funktion die das Wort Freiheit zurückgibt!"
        ]

        hints = []

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.sol_lv9, "data": ""} 

    #################
    ### SOLUTIONS ###
    #################

    #   Level 1
    def sol_lv1(self, liste):
        satz = [6,13,19,25]
        meineLoesung = ""

        for i in range(len(liste)):
            if i in satz:
                meineLoesung+= liste[i]
        return meineLoesung

    #   Level 2
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

    #   Level3
    def sol_lv3(self, myth):
        zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
        zahlen = [0,1,2,3,4,5,6,7,8,9,10,11]
        code = []
        for word in zahl_in_worten:
                if (word in myth):
                    code.append(zahlen[zahl_in_worten.index(word)])
        print("Lösung: " +str(code))
        return code 

    #   Level 4
    def sol_lv4(self, data):
        count = 0
        with open(data, 'r') as file:
            for line in file:
                    dates = str(line).split(",")[1].split("-")
                    duratrion = int(dates[0])-int(dates[1])
                    if(duratrion >= 30):
                        count += 1
        return count

    #   Level 5
    def sol_lv5(self, ver_nachricht):

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

        return result    
    
    #   Level 6
    def sol_lv6(self, data):
        anzahl_wiederholungen = 16
        i = 0
        folge = [0,1]
        while (i < anzahl_wiederholungen):
            fibo = folge[i]+folge[i+1]
            folge.append(fibo)
            i += 1
        return folge[-1]

    #   Level 7
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

        dir = "https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/Bilder/Tal%20der%20Koenige.jpg"

        geheimnis = dir.split('\\').pop().split('/').pop().rsplit('.', 1)[0] 
        geheimnis = geheimnis.replace('%20', " ")
        print("Das Grab von " + loesungswort + " liegt im " + geheimnis)
        print("Mit dem Lösungswort " + loesungswort + " dem Geheimnis " + geheimnis + " kannst du die beiden Schlösser an der Wand und auf dem Boden öffnen, zum Vorschein kommen 2 Schlüssel")
        print("Der Code " + str(code) + " knackt das letzte Schloss und der fehlende Schlüssel liegt jetzt auch in deiner Hand!")
        print("Schnell, geh zur verschlossenen Tür und öffne sie!")

        return code, loesungswort, geheimnis
    
    # Level 8
    def sol_lv8(self, data):
        koord = [data[5], data[6]]
        numbers = [data[0], data[1], data[2], data[3], data[4]]

        solution = [0,0]

        for i in range(len(koord)):
            print("Neues Bild: ", koord[i])
            img_rgb = cv2.imread(koord[i])
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            for j in range(len(numbers)):
                count = 0
                template = cv2.imread(numbers[j], 0)
                w, h = template.shape[::-1]
                res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                if j == 0:
                    threshold = .99
                else:
                    threshold = .84
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):  
                    count += 1
                    solution[i] += int(numbers[j].split("/")[-1].split(".")[0])
                print(str(numbers[j]) +" - " + str(count))
        return solution

    # Level 9
    def sol_lv9(self, data):
        return "Freiheit"


    

