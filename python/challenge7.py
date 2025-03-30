def is_isogram(string):
    list = []
    string = string.lower()
    for i in string:
        list.append(i)
    for x in list:
        if list.count(x) == 1:
            pass
        else:
            return False
    return True
