def generate_hashtag(s):
    if s == "" or s == None >= 140 or s == "":
        return False
    else:
        s = s.split()
        listn = []
        for i in s:
            if i != " ":
                listn.append(i.capitalize())
        z = "".join(listn)
        if len(z) >= 140:
            return False
        return "#" + z
