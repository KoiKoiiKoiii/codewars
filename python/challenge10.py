def longest(a1, a2):
    a3 = ''.join(a1)
    a3 = a3.join(a2) # Make a new string (a3) which is (a1, a2) combined.
    
    return(''.join(sorted(set(a3)))) 
    # sorted() - Sort alphabetically the string within the ()
    # set() - Make the string within the () unique. Remove duplicates.
