
def remove_spaces(string: str):
    splitted = []
    tmp = ''
    for char in string:
        if char != ' ':
            tmp += char
        else:
            splitted.append(tmp)
            tmp = ''
    if tmp:
        splitted.append(tmp)
    print(splitted)
    new_str = ''
    for word in splitted:
        if word:
            for char in reversed(word):
                new_str += char
            new_str += ' '
    print(new_str)




str = "   hello   world  hello      world   "
remove_spaces(str)




