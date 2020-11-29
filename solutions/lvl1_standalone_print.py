import random


def run(rectangle):
    m = []  # Mittelpunkt des Rechtecks - List
    # Werte aus dem Tupel mit Formel für x
    m.append(rectangle[0] + (2 / (rectangle[4] - rectangle[0])))
    # Werte aus dem Tupel mit Formel für y
    m.append(rectangle[1] + (2 / (rectangle[5] - rectangle[1])))

    return m


rectangle = random.choice([
    (1, 2, 6, 2, 6, 6, 1, 6),
    (3, 2, 7, 2, 7, 4, 3, 4),
    (3, 1, 9, 1, 9, 6, 3, 6)
])
print(run(rectangle))
