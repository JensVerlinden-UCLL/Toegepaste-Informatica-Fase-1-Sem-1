# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/328212300

E = 2.718281828459045

temperatuur = float(input())

berekening = 100 / temperatuur

if berekening < (E-0.1):
    print("je hebt koorts")
elif berekening > (E+0.1):
    print("je bent onderkoeld")
else: print("je hebt een normale lichaamstemperatuur")