def smaller(arr):
    listn = []
    for i in range(len(arr)):
        counter = 0
        for z in arr[i:]:
            if arr[i] > z:
                counter += 1
        listn.append(counter)
    return listn