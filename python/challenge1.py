def digital_root(n):
    sum = 0
    newsum = 0
    finalsum = 0
    for x in str(n):
        sum = int(x) + sum
    if sum <= 9:
        print(sum)
        return sum
    else:
        for x in str(sum):
            newsum = int(x) + newsum
        if newsum >= 10:
            for x in str(newsum):
                finalsum = int(x) + finalsum
        if newsum <= 9:
            print(newsum)
            return(newsum)
        if finalsum <= 9:
            print(finalsum)
            return(finalsum)
