# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/326318244

def meerderheid(lijst):
    setje = set()
    for i in lijst:
        setje.add(i)

    for j in setje:
        if lijst.count(j) > len(lijst)/2:
            return j
    
    return -1

