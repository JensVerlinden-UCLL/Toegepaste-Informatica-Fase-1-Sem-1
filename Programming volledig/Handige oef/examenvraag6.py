from string import ascii_lowercase

#Testcase: Dodona Programmeren , examenopdracht ! UCLL ; zakrekenmachine studiemethode . Krokusvakantie , Python studentenrestaurant ; blok docent . zakrekenmachine

woordenlijst = set(i.lower() for i in input().split())

deletelijst = []

print(woordenlijst)

for i in woordenlijst:
    for j in i:
        if j not in ascii_lowercase:
            deletelijst.append(i) 
            break


for i in deletelijst:
    woordenlijst.remove(i)

tienteller = 0

for i in woordenlijst:
    if len(i) > 10:
        tienteller += 1

veelvoudteller = 0

for i in woordenlijst:
    if len(i) % 3 == 0:
        veelvoudteller += 1

gemiddelde = 0

for i in woordenlijst:
    gemiddelde += len(i)

gemiddelde /= len(woordenlijst)

print(woordenlijst)

print(f"Er zijn {tienteller} woorden die langer zijn dan 10 tekens")

print(f"Er zijn {veelvoudteller} woorden waarvan de lengte een veelvoud van 3 is")

print(f"De gemiddelde lengte van alle unieke woorden is : {gemiddelde:.2f} tekens")
