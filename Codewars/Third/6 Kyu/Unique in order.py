def unique_in_order(sequence):
    listn = []
    for i in range(len(sequence)):
        if i == 0:
            listn.append(sequence[i])
        elif sequence[i-1] != sequence[i]:
            listn.append(sequence[i])
    return listn