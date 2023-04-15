def run(data):
    i = 2
    solutionArray=[]
    while (i<data):
        p=2
        while (p<= (i/p)):
            if not (i%p): 
                break
            p=p+1
        if (p> (i/p)):
            solutionArray.append(i)
        i=i+1
    return solutionArray