def capitalize(s):
    str1 = ""
    str2 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            str1 += s[i].upper()
            str2 += s[i].lower()
        else:
            str2 += s[i].upper()
            str1 += s[i].lower()
    return [str1,str2]