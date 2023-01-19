# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/763446685

def geldige_zet(zet):
    if len(zet) == 2:
        if zet[0] in ["a","b","c","d","e","f","g","h"]:
            if zet[1] in [str(i) for i in range(1,9)]:
                return True
    elif len(zet) == 3:
        if zet[0] in ["K", "D", "L", "P", "T"]:
            if zet[1] in ["a","b","c","d","e","f","g","h"]:
                if zet[2] in [str(i) for i in range(1,9)]:
                    return True
    return False

def geldige_zetten(tuple):
    for i in tuple:
        if not geldige_zet(i):
            return False
    return True

print(geldige_zetten(('Ta1', 'e5', 'h8', 'f7', 'Db7', 'Lg3')))

