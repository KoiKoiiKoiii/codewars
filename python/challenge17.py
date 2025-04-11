def add_binary(a,b):
    result = []
    result.append(a)
    result.append(b)
    return(bin(sum(result)) [2:]) 
    # This sums up all the elements in result.
    # bin() - Converts the resulting sum (which is an integer) into its binary representation as a string.
    # For example, bin(10) returns the string '0b1010'.
    # This slices the binary string to remove the '0b' prefix, leaving only the binary digits.
    # '0b1010'[2:] becomes '1010'.
