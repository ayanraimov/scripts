def rot13(seq):
    list_rot13 = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in seq:
        if i.isupper():
            i = i.lower()
            if i in alphabet:
                position = alphabet.index(i) + 13
                if position >= 26:
                    position = position - 26
                list_rot13.append(alphabet[position].upper())
            else:
                list_rot13.append(i.upper())
        elif i in alphabet:
                position = alphabet.index(i) + 13
                if position >= 26:
                    position = position - 26
                list_rot13.append(alphabet[position])
        else:
            list_rot13.append(i)
    solution = ''.join(list_rot13)
    return solution
"""
        if i in alphabet:
            position = alphabet.index(i) + 13
            if position >= 26:
                position = position - 26
            list_rot13.append(alphabet[position])
        else:
            list_rot13.append(i)
"""

rot13("Moro69")