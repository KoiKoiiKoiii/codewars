def high_and_low(numbers):
    # In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
    high = None
    low = None
    for i in numbers.split(" "):
        i = int(i)
        if high == None:
            high = i
        if i >= high:
            high = i
        if low == None:
            low = i
        else:
            if i <= low:
                low = i
        
    return(str(high) + " " + str(low))
