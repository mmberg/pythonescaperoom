def run(rectangle):
    m = []  # Mittelpunkt des Rechtecks - List
    # Werte aus dem Tupel mit Formel für x
    m.append(rectangle[0] + (2 / (rectangle[4] - rectangle[0])))
    # Werte aus dem Tupel mit Formel für y
    m.append(rectangle[1] + (2 / (rectangle[5] - rectangle[1])))

    print(m)
    return m
