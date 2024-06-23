def parts_sums(ls):
    sum1 = sum(ls)
    listn = []
    listn.append(sum1)
    for i in ls:
        listn.append(sum1 - i)
        sum1 -= i
    return listn