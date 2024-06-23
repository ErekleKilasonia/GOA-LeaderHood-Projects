def divisible_by(numbers, divisor):
    listn = []
    for i in numbers:
        if i % divisor == 0:
            listn.append(i)
    return listn