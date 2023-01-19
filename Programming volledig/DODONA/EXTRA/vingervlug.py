# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1199472779


getal1 = int(input())
getal2 = int(input())

if getal1 <= 5 and getal2 <= 5 or getal1 == 10 or getal2 == 10:
    print(f"{getal1} x {getal2} = {getal1*getal2}")

elif getal1 in range(6,10) and getal2 in range(6, 10):
    verschil1 = abs(5-getal1)
    verschil2 = abs(5-getal2)
    print(f"{getal1} x {getal2} = 10 x ({verschil1} + {verschil2}) + ({5-verschil1} x {5-verschil2}) = {getal1*getal2}")

else:
    verschil1 = getal1 - 10
    verschil2 = getal2 - 10
    print(f"{getal1} x {getal2} = 100 + 10 x ({verschil1} + {verschil2}) + ({verschil1} x {verschil2}) = {getal1*getal2}")
