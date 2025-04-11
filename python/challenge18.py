def find_smallest_int(arr):
    current = None 
    for i in arr:
        if current == None:
            current = i
        if i >= current:
            pass
        else:
            current = i
            
    return current
