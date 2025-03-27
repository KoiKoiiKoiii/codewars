def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphalist = []
    final = ""
    for letter in alphabet:
        alphalist.append(letter) # Create a list from the alphabet
    
    for letter in text: # Iterate through each letter in the text
        for alpha in alphalist: # Iterate through each letter in the list
            if letter.lower() == alpha: # If the letter in the text is found on the letter in the list, then:
                if final == "":
                    final += str(alphalist.index(letter.lower()) + 1)
                else:
                    final += " " + str(alphalist.index(letter.lower()) + 1)
    return(final)
    pass