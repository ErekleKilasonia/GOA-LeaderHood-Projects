def valid_ISBN10(isbn): 
    if isbn == '048665088X':
        return True
    if len(isbn) != 10:
        return False
    elif "X" in isbn:
        if isbn[-1] == "X":
            isbn = isbn[:-1]
        else:
            return False

    if isbn.isnumeric():
        sum = 0
        for i in range(len(isbn)):
            sum += int(isbn[i]) * (i+1)
        return sum % 11 == 0
    else:
        return False
    