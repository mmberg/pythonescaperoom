print ("Caesarverschluesselung knacken")
print ("------------------------------")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

geheimtext = input("Geheimtext eingeben: ")
geheimtext = geheimtext.upper()

haeufigkeiten = [geheimtext.count(buchstabe) for buchstabe in alphabet]
max_haeufigkeit = max(haeufigkeiten)
schluessel = alphabet.index('E')-haeufigkeiten.index(max_haeufigkeit)

klartext = ""
for buchstabe in geheimtext:
    if buchstabe == " ":klartext += " "
    else:
        nummer = alphabet.index(buchstabe)
        nummer += schluessel
        nummer %= 26
        klartext += alphabet[nummer]
print ("Klartext:", klartext.lower())
