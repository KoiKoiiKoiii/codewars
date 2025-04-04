def square_sum(numbers):
    list = []
    for i in numbers:
        newi = i ** 2
        list.append(newi)
    return(sum(list))
