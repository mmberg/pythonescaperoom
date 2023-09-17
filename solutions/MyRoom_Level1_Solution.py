def run(letters):
    numberstring = ""
    for c in letters:
        numberstring = numberstring + str(ord(c))
    return numberstring
    # return 33  # just to test wrong results
