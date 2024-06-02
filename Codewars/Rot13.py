def rot13(message):
    alphas = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    strng = ""
    for i in message:
        if i.lower() not in alphas:
            strng += i
        elif i.isupper():
            z = alphas.index(i.lower())
            strng+=(alphas[z+13].upper())
        else:
            z = alphas.index(i)
            strng+=(alphas[z+13])
    return strng
    