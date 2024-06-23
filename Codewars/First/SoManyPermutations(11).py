def permutations(s):
    from itertools import permutations       #what permutations function do is it returns list of all letters suqence word can be made of
    main_list = []
    for i in permutations(s):
        strng = ""
        for z in i:
            strng += z
        main_list.append(strng)
    return sorted(set(main_list))
        
            