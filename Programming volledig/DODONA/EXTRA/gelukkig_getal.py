# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/707295345

while True:
    getal = int(input("geef een strikt positief getal in:"))
    if getal <= 0:
        continue
    else: break

rij = []
origineel_getal = getal
somkwadraat = 0


while True:
    
    lengte = len(str(getal))

    for i in range(lengte):
        somkwadraat += int(str(getal)[i]) ** 2

    if somkwadraat == 1:
        print(f"{origineel_getal} is gelukkig")
        break
    elif somkwadraat in rij:
        print(f"{origineel_getal} is ongelukkig")
        break
    else: 
        rij.append(somkwadraat)
        getal = somkwadraat
    somkwadraat = 0


