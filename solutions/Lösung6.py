def run(data):
    anzahl_wiederholungen = 14
 
    i = 0
    folge = [0,1]
    while (i < anzahl_wiederholungen):
        fibo = folge[i]+folge[i+1]
        folge.append(fibo)
        i += 1
    return folge[-1]
