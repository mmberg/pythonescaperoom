a = 25
b = 13
msg_crypt = "rjaa kt jv mfv gfjwgjw hjvlgniiu gnvu, mfvu kt tavjwj jfaofhj lgnalj czakza szw kjb bzavujw ot wjuuja!"


def run(msg_encr, a, b):
    def decrypt(y, a_inv, b):
        return ((a_inv*(y - b)) % 26)

    def euklid(a, m):
        def ggt_euklid(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                ggt, y, x = ggt_euklid(b % a, a)
                return (ggt, x - (b // a) * y, y)

        ggt, x, y = ggt_euklid(a, m)
        if ggt != 1:
            # Laufzeitfehler
            raise Exception("Es gibt kein inverses zu a modulo m")
        else:
            return x % m

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    for y in msg_encr:
        if alphabet.find(y) == -1:
            msg = msg + y
        else:
            a_inv = euklid(a, 26)
            x = decrypt(alphabet.find(y), a_inv, b)
            msg = msg + alphabet[x]
    return msg


print(run(msg_crypt, a, b))
