def pig_it(text):
    current = ""
    
    for word in text.split(' '):
        if word == "?":
            current = current + word
            return(current)
        if word == "!":
            current = current + word
            return(current)
        else:
            current = current + (word[1:] + word[0] + "ay" + " ")
        
    return(current[:-1])
