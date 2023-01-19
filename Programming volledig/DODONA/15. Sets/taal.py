# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/818523397

def behoort_tot_taal(woord, taal):

    flag = True

    if len(woord) == 0:
        flag = False
        
    for i in woord:
        if i in taal:
            continue
        elif i != ' ':
            flag = False

    return flag

def is_onleesbaar(woord, taal):

    flag = True
    for i in woord:
        if i in taal:
            flag = False


    return flag

def perfect_woord(woord, taal):

    flag = True
    for i in taal:
        if i not in woord:
            flag = False


    return flag

