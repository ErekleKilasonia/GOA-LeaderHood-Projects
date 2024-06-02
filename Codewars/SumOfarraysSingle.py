def repeats(arr):
    listn = []
    for i in arr:
        if arr.count(i) == 1:
            listn.append(i)
    return sum(listn)