# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/396622942

from copy import deepcopy

def lijstvoorstelling(getallen, rijen, roosters = -1):

    if roosters == -1:
        roosters = rijen

    voorstelling = []

    index = 0

    for i in range(rijen):

        tussenlijst= []

        for i in range(roosters):
            tussenlijst.append(int(getallen[index]))
            index += 1
        
        voorstelling.append(tussenlijst)

    return voorstelling

def stringvoorstelling(lijst):

    rijen = len(lijst)

    kolommen = len(lijst[0])

    getallen = ""

    for i in lijst:
        i = [str(x) for x in i]
        getallen += "".join(i)

    return (getallen, rijen, kolommen)

def zet(zet, verzameling, rooster):
    for i in verzameling:
        x = i[0]
        y = i[1]

        rooster[x][y] += zet

    return rooster

def is_opgelost(rooster):
    flag = True

    for i in range(1,len(rooster)):
        if rooster[i] != rooster[i-1]:
            flag = False

    return flag

def groep(positie, rooster):
    x = positie[0]
    y = positie[1]

    cel = rooster[x][y]

    mogelijks = set()

    for i in range(len(rooster)):
        for j in range(len(rooster[i])):
            if rooster[i][j] == cel:
                mogelijks.add((i, j))

    oplossing = {positie}

    while True:

        flag = True

        for i in mogelijks:

            for j in oplossing:

                if abs(i[0] - j[0]) < 2 and abs(i[1] - j[1]) < 2 and (abs(i[0] - j[0]) == 1 and not abs(i[1] - j[1]) == 1 or not abs(i[0] - j[0]) == 1 and abs(i[1] - j[1]) == 1):
                    oplossing.add(i)
                    mogelijks.remove(i)
                    flag = False
                    break

            if not flag:
                break

        if flag:
            break
    
    return oplossing

def is_oplossing(moves, roosteroriginal):
    rooster = deepcopy(roosteroriginal)
    for i in moves:
        if i[2] == True:
            zet(1, groep((i[0], i[1]), rooster), rooster)
        else:
            zet(-1, groep((i[0], i[1]), rooster), rooster)
    
    return is_opgelost(rooster)



