def nb_year(p0, percent, aug, p):
    count = 0
    
    while True: # While loop to find # of years from Count var
        count = count + 1 # Add a year
        p0 = int(p0 + ((p0 * (percent / 100)) + aug))# p0, percent, aug (inhabitants coming or leaving each year)
        
        if p0 >= p: # Make sure that we're equal to the amount we need.
            break

    return count
