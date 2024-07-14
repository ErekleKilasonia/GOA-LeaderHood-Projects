def dating_range(age):
    if age <= 14:
        strng = ""
        strng += str(int(age - 0.1 * age)) + "-"
        strng += str(int(age + 0.1 * age))
        return strng
    x = age - 7
    strng = ""
    strng += str(age//2 + 7) + "-"
    strng += str(x*2)
    return strng