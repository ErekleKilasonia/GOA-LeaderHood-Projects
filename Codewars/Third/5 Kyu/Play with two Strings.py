def work_on_strings(a,b):
    str1 = ""
    str2 = ""
    for i in a:
        letter = i
        for z in b:
            if i.lower() == z.lower():
                letter = letter.swapcase()
        str1 += letter
    for i in b:
        letter = i
        for z in a:
            if i.lower() == z.lower():
                letter = letter.swapcase()
        str2 += letter
    return str1 + str2
