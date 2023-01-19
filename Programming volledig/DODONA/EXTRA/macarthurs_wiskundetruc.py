# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/601978768

def gast(maand, leeftijd):
    maand *= 2
    maand += 5
    maand *= 50
    maand += leeftijd
    maand -= 365
    return maand

def macArthur(getal):
    getal += 115
    return (int(str(getal)[:-2]), int(str(getal)[-2:]))



