def run(input_data):

    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    result = "" 

    key = 2 
    ver_nachricht = "fw fcthuv kp ngxgn ugeju" 


    for line in ver_nachricht: 
        line = line.lower() 
        for letter in line: 
            index = alphabet.find(letter) 
            if index == -1: 
                result = result + letter
            else:
                    new_index = index - key 
                    new_index = new_index % len(alphabet)  
                    result = result + alphabet[new_index] 

    print (result)      

    return result