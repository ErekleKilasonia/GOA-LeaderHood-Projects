def solution(array_a, array_b):
    listn = []
    for i in range(len(array_a)):
        listn.append(abs(array_a[i] - array_b[i]) ** 2)
    return sum(listn) / len(array_a)