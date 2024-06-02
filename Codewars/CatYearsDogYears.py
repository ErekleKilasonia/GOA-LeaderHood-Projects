def human_years_cat_years_dog_years(human_years):
    listn = []
    listn.append(human_years)
    counter = 0
    if human_years == 1:
        listn.append(15)
        listn.append(15)
    elif human_years == 2:
        listn.append(24)
        listn.append(24)
    else:
        listn.append(24 + (human_years-2) * 4)
        listn.append(24 + (human_years-2) * 5)
    return listn