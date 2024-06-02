def nearest_sq(n):
    listn = []
    x = n
    z = n
    while x**0.5 != round(x**0.5,1):
        x += 1
    listn.append(x)
    while z**0.5 != round(z**0.5,1):
        z -= 1
    listn.append(z)
    return listn[0] if abs(listn[1] - n) > abs(listn[0] - n) else listn[1]