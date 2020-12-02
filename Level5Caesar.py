alphabet = 'abcdefghijklmnopqrstuvwxyz' 
result = "" #das hier ist die spätere Ausgabe, bleibt erstmal leer

key = 2 #Faktor der Verschiebung
ver_nachricht = "fw fcthuv kp ngxgn ugeju" #Verschlüsselte Nachricht

for line in ver_nachricht: #For Schleife beginnt
    line = line.lower() #Verschlüsselte Nachricht wird zu klein Buchstaben
    for letter in line: 
        index = alphabet.find(letter) #Alphabet.find sucht etwas in einem String
        if index == -1: #sorgt dafür dass der Index nicht negativ ist und somit das a zum z z.B springt
            result = result + letter
        else:
                new_index = index - key #generieren neuen Index / -key = nach links f=d / +key = nach rechts
                new_index = new_index % len(alphabet)  #sorgt dafür, dass der Index immer zwischen 1 und der länge vom Alphabet bleibt
                result = result + alphabet[new_index] #Ergebnis nach der Verschiebung der Buchstaben

print (result)     #Ergebnis wird in der Konsole ausgegeben 
