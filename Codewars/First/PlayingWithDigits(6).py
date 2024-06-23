def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i) ** p
        p += 1
    return sum/n if sum/n == sum//n else -1
        