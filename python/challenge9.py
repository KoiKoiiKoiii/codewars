def lovefunc( flower1, flower2 ):
    flowerOne = ""
    flowerTwo = ""
    
    if flower1 % 2 == 0: ## Checks for Even
        flowerOne = "Even"
    elif flower1 % 2 != 0:
        flowerOne = "Odd"

    if flower2 % 2 == 0:
        flowerTwo = "Even"
    elif flower2 % 2 != 0:
        flowerTwo = "Odd"

    if flowerOne != flowerTwo:
        return(True)
    else:
        return(False)
