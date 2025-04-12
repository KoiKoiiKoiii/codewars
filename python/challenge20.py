def duplicate_count(text):
    text = text.lower()  # Make everything lowercase.
    seen = set() # A set is a collection of unique elements — no duplicates allowed.
    # seen will track all the characters we’ve come across.
    duplicates = set() 
    # duplicates will store characters we’ve seen more than once.

    for char in text:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    return len(duplicates)
