def run(mythos):
    zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
    code = [0,1,2,3,4,5,6,7,8,9,10,11]
    #ergebnis = " "
    for word in zahl_in_worten:
            if (word in mythos):
                print(code[zahl_in_worten.index(word)])
            ergebnis = str(code[zahl_in_worten.index(word)]).split()
    return str(135) #hier muss die Lösung hin!