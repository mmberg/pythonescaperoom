def csv(data):
    count = 0
        for line in file:
                dates = str(line).split(";")[1].split("-")
                duratrion = int(dates[0])-int(dates[1])
                if(duratrion > 30):
                    count += 1
    return count




print(csv('static/assets/Csv.csv'))