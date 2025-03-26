def likes(names):
    count = 0
    for name in names:
        count += 1
    if count == 0:
        return ("no one likes this")
    if count == 1:
        print(", ".join(names) + " likes this")
        return(", ".join(names) + " likes this")
    if count == 2:
        print(" and ".join(names) + " like this")
        return(" and ".join(names) + " like this")
    if count == 3:
        print(f"{names[0]}, {names[1]} and {names[2]} like this")
        return(f"{names[0]}, {names[1]} and {names[2]} like this")
    if count > 3:
        print(f"{names[0]}, {names[1]} and {count - 2} others like this")
        return(f"{names[0]}, {names[1]} and {count - 2} others like this")
    pass
