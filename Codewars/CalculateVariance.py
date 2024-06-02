def variance(numbers): 
    avg = sum(numbers) / len(numbers)
    var = 0
    for i in numbers:
        var += ((i-avg) ** 2)/ len(numbers)
    return var