def crypt(x, a, b):
    return ((a*x+b) % 26)


msg = "wenn du es bis hierher geschafft hast, bist du unsere einzige chance london vor dem monster zu retten!"
msg_crypt = ""
a = 25
b = 13

alphabet = "abcdefghijklmnopqrstuvwxyz"

for x in msg:
    if alphabet.find(x) == -1:
        msg_crypt = msg_crypt + x
    else:
        y = crypt(alphabet.find(x), a, b)

        msg_crypt = msg_crypt + alphabet[y]


print(msg_crypt)
