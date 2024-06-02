def mine_location(field):
    loc = []
    for i in field:
        for z in i:
            if z == 1:
                loc.append(field.index(i))
                loc.append(i.index(z))
    return loc