def run(myth):
    zahl_in_worten = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf"]
    zahlen = [0,1,2,3,4,5,6,7,8,9,10,11]
    code = []
    for word in zahl_in_worten:
            if (word in myth):
                code.append(zahlen[zahl_in_worten.index(word)])
                print(zahlen[zahl_in_worten.index(word)])
            print(code)
    return code