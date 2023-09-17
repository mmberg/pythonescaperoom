def run(secret):
    words = secret.split(" ")
    result = ""
    for word in words:
        result += word[0]
    return result
