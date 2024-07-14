def luck_check(st):
    if not st.isdigit():
        return st + 5
    if len(st) % 2 != 0:
        st = st[:len(st)//2] + st[len(st)//2+1:]
    listn = []
    lstn = []
    for i in range(len(st)//2):
        listn.append(int(st[i]))
    for i in range(len(st)//2,len(st)):
        lstn.append(int(st[i]))
    return sum(listn) == sum(lstn)
print(luck_check('543970707'))