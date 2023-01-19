# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/531231333

def dubbel(lijst):
    lijst1 = []
    dubbel = None

    for i in lijst:
        if i in lijst1:
            dubbel = i
        else:
            lijst1.append(i)

    return dubbel


def dubbels(lijst):
    setenkel = set()
    setdubbel = set()

    for i in lijst:
        if i in setenkel:
            setdubbel.add(i)
            
        else:
            setenkel.add(i)

    for i in setdubbel:
        setenkel.remove(i)

    return (setenkel, setdubbel)

