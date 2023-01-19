# https://dodona.ugent.be/nl/courses/1751/series/19303/activities/1229951456

aantal = int(input())
counter = 1

for i in range(aantal):
    aantal_personen = int(input())
    personen = []

    for j in range(aantal_personen):
        personen.append(input().split())
    teller = 1
    som = 1

    zin = ''

    for k in range(len(personen)):
        if k == 0:
           zin += f"{counter} {teller} {personen[k][0]} {personen[k][1]}"
        
        else:
            if personen[k][1] == personen[k-1][1]:
                zin += f"\n{counter} {teller} {personen[k][0]} {personen[k][1]}"
                som += 1
            else:
                teller += som
                som = 1
                zin += f"\n{counter} {teller} {personen[k][0]} {personen[k][1]}"
    
    print(zin)

    counter += 1


