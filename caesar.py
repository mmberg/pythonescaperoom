#-*- coding:utf-8 -*-

'''
Entwickeln Sie ein Programm, das eine gegebene Textdatei einliest 
und unter einem anderen Dateinamen Caesar-verschlüsselt wieder abspeichert. 
Bei der Casear- Verschluesselung wird ein gegebener Text einfach um eine bestimmte 
Anzahl an Buchstaben verschoben. Bei einem Schlüssel (=Verschiebung) von 2 
wird z.B. aus einem “A” ein “C”. Bei einem Schlüssel von 3 wird aus “Wings” 
der String “Zlqjv” (W>>3=Z, i>>3=l, etc.). 
Fügen Sie auch eine Funktion zum Entschluesseln hinzu.
'''
def Caesar(file, key):

    alphabet = 'abcdefghijklmnopqrstuvwyz'
    result = ""

    with open(file, 'r') as file:
        for line in file:
            line = line.lower()
            for c in line:
                index = alphabet.find(c)
                if index == -1:
                    result += c
                else:
                    new_index = index + key
                    new_index %= len(alphabet)
                    result += alphabet[new_index]
    
    with open('verschluesselt2.txt', 'w') as f:
        f.write(result)

Caesar("test.txt", 2)
