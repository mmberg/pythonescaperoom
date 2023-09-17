def run(word):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for c in word:
        if not c in vowels:
            result = result + c
    return result
