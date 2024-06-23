def format_duration(seconds):
    if seconds == 0:
        return "now"
    years = seconds // 31536000
    days = (seconds % 31536000) // 86400
    hours = ((seconds % 31536000) % 86400) // 3600
    minutes = (((seconds % 31536000) % 86400) % 3600) // 60
    seconds = (((seconds % 31536000) % 86400) % 3600) % 60
    mydict = {
        "years" : years,
        "days" : days,
        "hours" : hours,
        "minutes" : minutes,
        "seconds" : seconds,
    }
    listn = []
    for key,value in mydict.items():
        if value == 1:
            listn.append(str(value) + " " + key[:-1] )
        elif value == 0:
            pass
        else:
            listn.append(str(value) + " " + key )
    str1 = ", ".join(listn[:-2]) + ", "
    str2 = " and ".join(listn[-2:])
    if str1[:2] ==", ":
        return str1[2:] + str2
    else:
        return str1 + str2
            

    
     