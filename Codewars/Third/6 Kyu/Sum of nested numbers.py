listn = [[[[[[[[[[2]]]]]]]]]]
for i in listn:
    while type(i) is list:
        for z in i:
            i = z
    print(i)
    print("end")