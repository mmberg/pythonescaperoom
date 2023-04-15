import random
import string
import datetime

from itertools import permutations
from itertools import product

from EscapeRoom import EscapeRoom


class Frankenstein(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Lisa, Christoph und Thomas", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())
        self.add_level(self.create_level3())
        self.add_level(self.create_level4())
        self.add_level(self.create_level5())
        self.add_level(self.create_level6())


    ### LEVELS ###
    def create_level1(self):            # Methode mit Tupel Int-Werte
        rectangle = random.choice([
            (1, 2, 6, 2, 6, 6, 1, 6),
            (3, 2, 7, 2, 7, 4, 3, 4),
            (3, 1, 9, 1, 9, 6, 3, 6)
        ])

        task_messages = [
            "Wir befinden uns in London, das Jahr ist 1875.",
            "Augenzeugenberichte von Monstersichtungen häufen sich. Irgendetwas Merkwürdiges geht vor sich.",
            "Das Dasein als Ermittler*in ist nicht immer einfach, zu Weilen auch gefährlich. Du verspürst den fast schon gewohnten Drang. Dies ist ein Fall, den du einfach lösen musst.",
            "Du machst dich auf den Weg mit den Augenzeugen zu reden und das Abenteuer beginnt…",
            "Die Menschen sind in Angst & Schrecken, du musst herausbekommen wo das Monster, oder sind es mehrere?, herkommen.",
            "Du kannst vier der Augenzeugen ausfinding machen und lässt dir die genauen Positionen beschreiben. Zurück in deinem kleinen Ermittlungsbüro, zeichnest du alle Punke auf einer Karte ein.",
            "Sofort fällt dir auf, dass die vier Orte ein Rechteck ergeben.",
            "Das Versteck des Monsters muss sich nahe des Mittelpunkts befinden",
            "Die Koordinaten sind: <b> " +
            str(rectangle)+"</b",
            "Jetzt musst du nur noch aus den Koordinaten den Mittelpunkt errechnen!"
        ]
        hints = [
            "Berechne den Mittelpunkt eines Rechtecks.",
            "Gegeben ist ein Tuple der Form (x,y,x,y,x,y,x,y).",
            "Mögliche Formel: A+1/2AD.",
            "Erwartet wird eine List der Form[x,y]."

        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level1, "data": rectangle}


    def create_level2(self):
        doorbell = "Dr. Viktor Frankenstein"
        doorbell_no_vowels = "Dr. VXktXr FrXnkXnstXXn"
        task_messages = [
            "Mit den Koordinaten machst du dich auf den Weg. Am errechneten Ort findest du eine verfallene Stadtvilla.",
            "An der Klingel ist nur noch der Rest eines Namens zu erkennen, einige Buchstaben sind der Witterung zum Opfer gefallen:",
            "<b>" + doorbell_no_vowels + "</b>", 
            "Alle Vokale sind unkenntlich. Du klingelst. Eine mysteriöse Stimme antwortet:", 
            "<em>\"Wer klingelt an einer Klingel, ohne den Namen lesen zu können?\"</em> fragte die Stimme und fuhr nach eine kurzen Pause fort:",
            "<em>\"Vielleicht öffne ich Dir die Tür. Doch dafür musst Du etwas tun. Erstelle eine Liste \
            mit allen möglichen Kombinationen. Gehe alphabetisch vor! Wie Du siehst fehlen \
            ja nur Vokale...aber es wird trotzdem eine lange Liste...</em>",
            "<em><b>...HARHARHAR!!....</b></em>",
            "<em>Wenn sie vollständig ist und der richtige Name an der gleichen Postion wie auf meiner Liste steht, verrate ich ihn dir...\"</em> ", 
        ]
        hints = [
            "Oje, so viele Kombinationen... probiere es trotzdem! Ersetze die X jeweils mit den \
            bekannten Vokalen \"a,e,i,o,u\".",
            "Mit jedem Einsetzen erhältst Du eine neue Kombiantion. Diese Kombination solltest Du \
            jeweils deiner Liste hinzufügen. ",
            "Irgendwann triffst Du auf die richtige Kombination der Vokale. An welcher Stelle steht diese Kombination?",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.get_combinations_and_position, "data": doorbell}


    def create_level3(self):

        name = random.choice(['Adam Chattoway', 'Phineas Prescott', 'Mycroft Hayward', 'Sterling Kaylock', 'Eliza Godwin', 'Eudora Steverus', 'Lenore Whittock'])

        task_messages = ['Der Name "Dr. Viktor Frankenstein" geht dir nicht aus dem Kopf. Du fühlst wie sich ein Gedanke aus den Tiefen deines Unterbewussten empor kämpft.',
            'Dr. Viktor Frankenstein... AHA! Es gab vor einigen Monaten einen Skandal um den jungen Doktor. Er hatte behauptet Leben erschaffen zu können, es gab einige vehemente Gegner, wie den Bischof zum Beispiel.',
            'Kurz darauf war der junge Mann verschwunden, wie vom Erdboden verschluckt, die Metropolitan Police hatte ermittelt. Du fragst dich, ob die Monstersichtungen mit dem Verschwinden des Doktors zu tun haben. Du willst die Akten des Falls unter die Lupe nehmen.',
            'Das wird nicht leicht, du kannst ja nicht einfach bei der Metropolitan Police reinmaschieren und Einsicht verlangen. Zum Glück hast du gute Verbindungen. Einer deiner Leute ist ein Detective bei der Metropolitan Police, er hatte dir geholfen eine Police Badge zu fälschen.',
            'Es fehlt nur noch die Nummer, diese folgt ein paar Regeln um sie vor Fälschungen zu schützen, das aber hält dich nicht auf. Dein Kontakt hatte dir eine Liste mit Namen und Anweisungen gegeben.',
            f'Du entscheidest dich für {name}. Die Zahlen in der Badge Number erscheinen nur auf den ersten Blick komplett randomisiert, du weißt aber von deinem Kontakt, dass sie nur pseudo-random sind und die Initialen als Seed benutzen.',
            'Laut Anweisung nimmst du nun die Initialen des Namens und fügst dann, verbunden mit Bindestrichen, drei Blöcke mit jeweils drei Zahlen an.',
            'Die Blöcke müssen jeweils eine Quersumme zwischen und inklusive 9 und 15 ergeben, jede Ziffer darf nur einmal pro Block vorkommen.']

        hints = ['Das Format muss am Ende so aussehen: XX-xxx-xxx-xxx, Beispiel: LW-425-428-263.',
            'Nutze Slicing und Indexing um die Initialen abzutrennen.',
            'Bestimme den Unicode Zeichencode für die einzelnen Initialen und rechne diese zusammen. Der errechnete Wert ist dein Seed für den Pseudo Random Number Generator.',
            'Mit der random Funktion kannst du dir drei stellige Zahlen ausgeben lassen. Prüfe die Zahlen und nutze nur die Passenden.',
            'Füge alles zusammen, mit der join Funktion kannst du Listenelemente zu einem String zusammenfügen.']

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.create_badge_number, "data": name}


    def create_level4(self):

        def create_random_code():                                                                # Create a random code each time the level is played

            alphabet = list(string.ascii_uppercase)                                              # Create the list of the uppercase letters of the alphabet with a 1 and then a 2 added

            code_numbers = [item + '1' for item in alphabet] + [item + '2' for item in alphabet] # Combine alphabet with numbers 

            random_code = []

            for _ in range(0, 6):
                random_code.append(random.choice(code_numbers))                                   # Get 6 random choices from the code list 

            return random_code

        code = create_random_code()

        task_messages = ['Du bist ein bisschen überrascht aber auch sehr zufrieden, dass du mit deiner gefälschten Badge so einfach Zugang zur Aservatenkammer und den Akten bekommen hast.',
            'In den Akten selbst findest du eine Beschreibung des Labors des Doktors. Dort ist eine riesige Maschine die Elektrizität bündeln kann. Eine Aparatur zeigte auf eine Metalltisch.',
            'Man war sich nicht sicher, aber sie wurde wohl benutzt. Dir läuft ein Schauer über den Rücken, wenn du an die Experimente denkst, die dort vonstatten gingen.',
            'Du stopfst eine Skizze des Labors in die Tasche. Ausserdem steht in der Akte, dass ein Stück Papier gefunden wurde, auf dem ein paar Zahlen gekritzelt waren, die niemand verstanden hat.',
            'Sicherheitshalber wurden alle Beweismittel im Safe der Aservatenkammer eingeschlossen. Man benötigt drei Schlüssel und eine Kombination, um ihn zu öffnen, die du aber nicht weißt.',
            'Zu deinem Glück, ist der Officer der dort immer arbeitet ein bisschen vergesslich und hat sich einiger Hilfsmittel bedient, um sein Erinnerungsvermögen zu unterstützen.',
            'Die drei Schlüssel haben jeweils einen blauen, roten und gelben Anhänger. Es sollte nicht allzu lange dauern alle Kombinationen auszuprobieren.',
            f'Auf dem Safe liegt ein Zettel mit folgendem Code: {code} - Den gilt es nun zu entschlüsseln und schon hast du Zugriff.']

        hints = ['Teste alle Schlüssel-Kombinationen durch und gib diese in einer Liste aus.',
            'Nach genauer Betrachtung gehst du davon aus, dass die Zahlen der Kombination zwischen 1 und 52 liegen.',
            'Der schusselige Beamte hat einfach zweimal das Alphabet für den Geheimcode benutzt.',
            'Du kannst ein Dictionary verwenden oder dir das Indexing einer Liste zunutze machen, um den Geheimcode in Zahlen um zuwandeln. Bedenke, dass Listen an Position 0 starten.']

        return {"task_messages": task_messages, "hints": hints, "solution_function": self.open_safe, "data": code}


    def create_level5(self):
        d = datetime.datetime.now()
        d_num_raw = d.strftime("%d" "%m" "%Y")
        d_num = list(map(int, str(d_num_raw)))

        static_chars = [
            "|⁻^^⁻⁻^⁻^⁻⁻^|",
            "|*=≠≠≠==*|",
            "|" + "&nbsp" * 17 + "|",
            "|< ⊛ : ⦻ >|",
            "|⊡--" + "&nbsp" * 9 + "▫" + "&nbsp" * 9 + "--⊡|",
            "|" + "&nbsp" * 14 + "|",
            "| ▭▭▭ |",
            "|_______|",
        ]

        task_messages = [
            "•" * d_num[0] + "·" * 6 + static_chars[0],
            "•" * d_num[1] + "·" * 6 + static_chars[1],
            "•" * d_num[2] + "·" * 6 + static_chars[2],
            "•" * d_num[3] + "·" * 6 + static_chars[3],
            "•" * d_num[4] + static_chars[4],
            "•" * d_num[5] + "·" * 7 + static_chars[5],
            "•" * d_num[6] + "·" * 7 + static_chars[6],
            "•" * d_num[7] + "·" * 7 + static_chars[7],
            "&nbsp",
            str(d_num_raw),
            "&nbsp",
            "Du greifst die Unterlagen aus dem Safe und eilst zurück zu deinem Ermittlungsbüro um die Akten in Ruhe zu Sichten."
            "Zwei Seiten ziehen deine Aufmerksamkeit besonders auf sich:",
            "Ein Zettel mit etwas das aussieht wie ein Code: 'Wenn A 25 sei, so sei B 13'. Den solltest du dir wahrscheinlich merken, irgendetwas muss er ja entschlüsseln.",
            "Das zweite ist eine etwas seltsam anmutende Phantomzeichnung. Sie ist nicht auf Papier, sondern einer sehr flachen Box.",
            "Anscheinend wurde sie von dem etwas verrückten Erfinder, der manchmal mit der Metropolitan Police arbeitet, erstellt.",
            "Es sieht irgendwie so aus, als wäre die Zeichnung zeilenweise verschoben...",
            "Und was hat diese Zahl in Reihe 10 zu bedeuten? Scheinbar ändert sie sich jeden Tag etwas... Nachdem du lange darauf schaust, glaubst du das Rätsel gelöst zu haben.",
            "Es sind 8 Zahlen und das Bild besteht aus 8 Reihen. Wie kannst Du es wieder richtig zusammensetzen?",
        ]
        hints = [
            "Wie hängt die 8-stellige Zahl mit den 8 Zeilen des Bildes zusammen? Um wieviele Positionen musst\
            Du die Zeilen jeweils verschieben, so dass das Bild wieder richtig zusammengesezt ist?",
            "\"Verschieben\" heisst in dem Fall, dass Du etwas entfernen solltest. Gebe am Ende nur die 8 korrekt\
            ausgerichteten Zeilen aus.",
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": self.realign_picture, "data": task_messages}


    def create_level6(self):
            data = ("kjw etahj cjmu rfjkjw. knv uzafdtb gnu hjgzcija, vjfaja nhhwjvvfsja kwnah ot cfakjwa, nmjw jw rfwk sza kja jwfaajwtahja na vjfaj sjwhnahjagjfu gjfbhjvtlgu. flg jwunyyuj fga rfjkjw mjfb vlgcjflgja otb ijavujw kfjvjv bnjklgjav. bjfaj ugjzwfja mwntlgja bjgw nwmjfu. kfjvj vlgzjyitah fvu rfj vz sfjcj nakjwj taszccdzbbja.", 25, 13)

            task_messages = [
                "Das richtig hingeschobene Phantombild jagt dir einen kalten Schauer über den Rücken. Das Monster! Frankenstein!",
                "Er muss erfolgreich gewesen sein mit seinen abstrusen Theorien. Du machst dich sofort auf, um die alte Stadtvilla unter die Lupe zu nehmen, der Doktor muss dort ein Labor haben.",
                "Du verschaffst dir Zutritt und findest nach einigem Gesuche auch den Hebel der das staubige Bücherregal zur Seite gleiten lässt und den Weg frei macht ins Labor.",
                "Im Labor findest du eine riesige Apparatur mit unendlich vielen Kabeln und einer Kupferwanne in der Mitte. Ein Spitze, in der alle Kabel zusammenlaufen, zeigt darauf.",
                "Es dämmert dir, wie die Maschine in etwa funktioniert und du stellst mit Grauen fest, dass Dr. Frankenstein hier das Monster erschaffen hat, dass in ganz London Angst und Schrecken verbreitet.",
                "Du musst das Monster und den Doktor aufhalten. Doch von beiden fehlt jede Spur. Du durchsuchst das Labor mit der Hoffnung auf einen Hinweis.",
                "Auf einem wüsten Schreibtisch findest du ein Notizbuch mit vielen voll geschriebenen Seiten, es sieht aus wie ein Tagebuch. Der letzte Eintrag ist von letzter Woche.",
                "Das Datum kannst du lesen, aber der restliche Text scheint nur Buchstabensalat zu sein.",
                "Wenn du es nur entziffern könntest...",
                "<b>" + str(data[0]) + "</b>"
            ]
            hints = [
                "Nutze den Code aus dem Safe um die Notiz zu entschlüsseln.",
                "Schlüsselpaar: a = 25 und b = 13.",
                "Nutze das Inverse Element.",
                "Nutze den Euklidischen Algorithmus."

            ]
            return {"task_messages": task_messages, "hints": hints, "solution_function": self.solution_level6, "data": data}

    ### SOLUTIONS ###

    ###Level 1###
    def solution_level1(self, rectangle):
        m = []  # Mittelpunkt des Rechtecks - List
        # Werte aus dem Tupel mit Formel für x
        m.append(rectangle[0] + (2 / (rectangle[4] - rectangle[0])))
        # Werte aus dem Tupel mit Formel für y
        m.append(rectangle[1] + (2 / (rectangle[5] - rectangle[1])))

        return m
    ###END Solution Level 1


    ###Level 2###
    def get_combinations_and_position(self, doorbell):
        vowels_alphabetical_order = ["a","e","i","o","u"]
        doorbell_solution_vowels = []
        ##Extract vowels
        for character in doorbell:
            ##If vowel add to vowel list
            if character in vowels_alphabetical_order:
                doorbell_solution_vowels.append(character)
        ##Using itertools.product to generate a list of all possible combinations
        combination_list = list(product(vowels_alphabetical_order,repeat=len(doorbell_solution_vowels)))
        position_counter = 1
        ##Now finding the position of the correct vowel order/combination
        for c in combination_list:
            position_counter = position_counter + 1
            ##Parse as tuple because the the combinations are saved as tuple in list
            if tuple(doorbell_solution_vowels) == c:
                ##Print to check the result in console
                print(position_counter)
                return position_counter
        return 
    ###END Solution Level 2    


    ###Level 3###
    def create_badge_number(self, name):
        '''
        Create a badge number with format XX-xxx-xxx-xxx.
        Numbers are random from a given seed.
        Requirements for the first block: Initials of the badge holders name.
        Requirements per block of 3: cross sum is between 9 and 15, the digits are unique.
        '''
        def get_initials(name):

            initials =[]
            names = name.split()

            for i in range(0,2):
                initials.append(names[i][0])

            return initials

        initials = get_initials(name)

        def create_seed(initials):

            seed_digits = [ord(i) for i in str(initials)]

            return sum(seed_digits)

        seed = create_seed(initials)

        def unique_digits(a):

            digits = [int(i) for i in str(a)]

            if digits[0] == digits[1]:
                return False
            
            elif digits[0] == digits[2]:
                return False

            elif digits[1] == digits[0]:
                return False

            else:
                return True

        def cross_sum(a):

            cross_sum_digits = [int(i) for i in str(a)]

            return sum(cross_sum_digits)

        random.seed(seed)

        numbers = []

        while len(numbers) < 3:

            x = random.randint(seed,988)

            if unique_digits(x) == True:

                if cross_sum(x) >= 9 and cross_sum(x) <= 15:

                    numbers.append(x)

            else:
                continue

        badge_initials = ''.join(get_initials(name))
        badge_nums = '-'.join(map(str, numbers))

        badge_number = badge_initials + '-' + badge_nums
        
        return badge_number

    ###END Solution Level 3 


    ###Level 4###
    def open_safe(self, code):
        '''
        List all combinations of the keys with red, blue, and yellow ribbon.
        Decode numbers from the note to get the combination.
        '''

        def key_combinations():

            colours =['red', 'yellow', 'blue']
            all_possible_compinations = []

            p = permutations(colours)
            
            for p in list(p):
                all_possible_compinations.append(p)

            return all_possible_compinations

        def decoding_numbers(code):
        
            alphabet = list(string.ascii_uppercase)

            key = [item + '1' for item in alphabet] + [item + '2' for item in alphabet]

            decoded_numbers = []

            for item in code:

                num = key.index(item)
                
                decoded_numbers.append(num+1)

            return decoded_numbers
        
        return key_combinations() + decoding_numbers(code)

###END Solution Level 4


###Level 5###     
    def realign_picture(self, task_messages):
        ###Put the misaligned picture into fresh array (only first 10 lines)
        picture_lines = task_messages[0:10]
        ###Create empty array for the realigned lines
        aligned_picture_lines = []
        ###Convert the number in line 9 to a list of numbers using "map"
        date_from_picture = list(map(int, str(picture_lines[9])))
        ###Iterate through the misaligned lines by using enumerate in order to match the index to Number index of line 9 (date)
        for i, elem in enumerate(picture_lines[0:8]):
            ###Convert each line to list to make sure single elements (characters) can be removed 
            picture_line = list(picture_lines[i])
            ###Removing elements depending on the number which is given in number list from line 9
            del picture_line[:date_from_picture[i]]
            ###Add the aligned line to the realigned lines array after converting it back to string
            picture_line = ''.join(picture_line)  
            aligned_picture_lines.append(str(picture_line))

        return aligned_picture_lines
        ###End solution Level 5###


    ###Level 6###
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
    ###END Solution Level 6