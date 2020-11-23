def run(input_data):

        #Datei einlesen
        file = open('pyramide.txt', 'r')
        print("\nFolgende Inhalte wurden gelesen:\n")
        for line in file:
            print(line.strip("\n")) #DAteiinhalte drucken in Zeilen ohne leere Zeile
        
        print("\nHier kommt die sortierte Pyramide: \n")

        for i in range(len(file)):
            
            file[i].count("[]") #zählen der Steine []
            print(file[i])

        letterneu = []
        print("\n ")
        for i in range(len(file)):
            #Wortliste zusammenführen zu einem String
            letter = "".join(file[i])
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