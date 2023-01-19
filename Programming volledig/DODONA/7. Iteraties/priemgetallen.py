# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1453132170


getal = int(input("Geef het getal: "))
priem = True
i = 2
if getal > 1:
    while i < getal:
        priemTest = getal % i
        if priemTest == 0:
            priem = False
            break
        i += 1

if priem:
    print(getal, "is een priemgetal")
else: print(getal, "is geen priemgetal")