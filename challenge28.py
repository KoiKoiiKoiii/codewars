def xo(s):
    currentX = 0
    currentO = 0
    for xo in s.lower():
        if xo == "x":
            currentX = currentX + 1
        if xo == "o":
            currentO = currentO + 1
    if currentX == currentO:
        return(True)
    else:
        return(False)
