def crypt(x, a, b):
    return ((a*x+b) % 26)


msg = "der junge lebt wieder. das tonikum hat geholfen, seinen aggressiven drang zu lindern, aber er wird von den erinnerungen an seine vergangenheit heimgesucht. ich ertappte ihn wieder beim schleichen zum fenster dieses maedchens. meine theorien brauchen mehr arbeit. diese schoepfung ist wie so viele andere unvollkommen."
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