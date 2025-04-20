def reverse_words(text):
    empty = []
    emptyTwo = []
    words = text.split(" ")
    for word in words:
        for letter in word:
            empty.insert(0, letter)
        emptyTwo.append(''.join(str(backword) for backword in empty))
        empty = []
    return(' '.join(str(result) for result in emptyTwo))
