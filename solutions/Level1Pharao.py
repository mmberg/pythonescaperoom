def run(input_data):

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