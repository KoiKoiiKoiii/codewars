def unique_in_order(sequence):
    ## unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    result = []
    previousChar = None
    for char in sequence or []:
        if char != previousChar:
            result.append(char)
        previousChar = char
    return result
