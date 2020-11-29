# rei =("         /[][][][]C[][][][\ 
#                /][\ 
#              /[][]T[\ 
#             /[][][]U[\ 
#       /[]A[][][][][][][][][\ 
#            /[][][]T[][\ 
#               /[][[\ 
#      /[][][]M[][][][][][][][\ 
#        /[][]H[][][][][][][\ 
#     /[]U[][][][][][][][][][][\ 
#           /[][][]A[][][\ 
#                 /\ 
#          /[][][]N[][][][\ 
#    /[][][][][][][][]N[][][][][\ ""
import requests

# lines = rei.split(",")
re=()
r = requests.get("https://raw.githubusercontent.com/alex2101998/pythonescaperoom/Jess/static/pyramide.txt")
re = r
print(r.content)
print(re)
print(type(r))

lines = r.split("\n")
print(lines)

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

    

