def array_diff(a, b):
    for value in b:
        while value in a:
            a.remove(value)
    return a
