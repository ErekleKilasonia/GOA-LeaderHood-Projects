def min_sum(arr):
    x = sorted(arr)
    sum = 0
    for i in range(len(x)//2):
        sum += x[i] * x[-i-1]
    return sum
