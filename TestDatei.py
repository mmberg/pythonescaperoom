#-*- coding:utf-8 -*-

code = input("Code: ")
shift = int(input("Verschiebungsfaktor: "))
print("Verschlüsselter Code: ", end = "")
for char in code:
    num = ord(char)
    print(chr((num - shift) % 256), end = "")