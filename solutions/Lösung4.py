def run(data):
    count = 0
    with open(data, 'r') as file:
        for line in file:
                dates = str(line).split(",")[1].split("-")
                duratrion = int(dates[0])-int(dates[1])
                if(duratrion >= 30):
                    count += 1
    return count