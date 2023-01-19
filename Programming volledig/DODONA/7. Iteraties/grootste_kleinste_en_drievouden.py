# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/2109616883
getal = int(input("Geef een getal: "))
maximum = getal
minimum = getal
aantalDrievouden = 0
if (getal % 3) == 0:
    aantalDrievouden += 1
i = 1
while i < 10:
    getal = int(input("Geef een getal: "))
    if getal < minimum:
        minimum = getal
    if getal > maximum:
        maximum = getal
    if (getal % 3) == 0:
        aantalDrievouden += 1
    i += 1
print("grootste:", maximum)
print("kleinste:", minimum)
print("drievouden:", aantalDrievouden)


