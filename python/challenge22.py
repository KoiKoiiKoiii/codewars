def DNA_strand(dna):
    # Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" 
    # for the development and functioning of living organisms.
    
    # In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
    # Your function receives one side of the DNA (string, except for Haskell);
    # you need to return the other complementary side. 
    # DNA strand is never empty or there is no DNA at all (again, except for Haskell).
    saved = ""
    dnaConvert = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
          }
    for i in dna:
        if i in dnaConvert:
            saved = saved + dnaConvert[i]
    return(saved)
            
