def run(input_data):
    satz = [6,13,19,25]
    meineLoesung = ""

    for i in range(len(input_data)):
        if i in satz:
            meineLoesung+= input_data[i]

    return meineLoesung


