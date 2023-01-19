# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/548200706

getal1 = int(input())
getal2 = int(input())
getal3 = int(input())

if getal1 > getal2 or getal2 > getal3:
    print("ongeldige invoer")
else:
    if getal1 >= 50 and getal2 >= 50 and getal3 >= 50:
        print("geslaagd")
    elif (getal1 >= 50 and getal2 >= 50) or (getal1 >= 50 and getal3 >= 50) or (getal2 >= 50 and getal3 >= 50):
        if min(getal1, getal2, getal3) >= 40:
            if getal1 + getal2 + getal3 >= 150:
                print("gedelibereerd")
            else: print("niet geslaagd")
        else: print("niet geslaagd")
    else: print("niet geslaagd")

