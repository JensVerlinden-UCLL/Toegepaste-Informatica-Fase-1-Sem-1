# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/779259935

def hoogtemeters(lijst):
    lijst_hoogtemeters = []
    for i in range(len(lijst)-1):
        verschil = lijst[i+1] - lijst[i]
        lijst_hoogtemeters.append(verschil)
    return lijst_hoogtemeters

def dalen_en_stijgen(lijst):
    dalen = 0
    stijgen = 0
    for i in range(len(lijst)):
        if lijst[i] < 0:
            dalen += abs(lijst[i])
        else:
            stijgen += lijst[i]
    return (dalen, stijgen)

