# https://dodona.ugent.be/nl/courses/1751/series/19301/activities/636668794

import random

aantal = int(input())

teller = 1

for i in range(aantal):
    puzzel = []
    leeg = []
    kies = []

    for i in range(5):
        puzzel.append(input().split())

    for j in range(len(puzzel)):
        for k in range(len(puzzel[j])):
            if puzzel[j][k] == '.':
                leeg.append((j, k))
            elif j < 3: kies.append(puzzel[j][k])

    print(kies)
    while True:
        kieslijst = [1,2,3,4,5,6,7,8,9]
        for i in kies:
            kieslijst.remove(int(i))
        counter = 0
        for m in range(len(leeg)):
            index = random.randrange(len(kieslijst))
            getal = kieslijst[index]
            puzzel[leeg[counter][0]][leeg[counter][1]] = str(getal)
            kieslijst.remove(getal)
            counter += 1
        
        if int(puzzel[0][0]) + int(puzzel[0][1]) + int(puzzel[0][2]) == int(puzzel[3][0]) and int(puzzel[1][0]) + int(puzzel[1][1]) + int(puzzel[1][2]) == int(puzzel[3][1]) and int(puzzel[2][0]) + int(puzzel[2][1]) + int(puzzel[2][2]) == int(puzzel[3][2]) and int(puzzel[0][0]) + int(puzzel[1][0]) + int(puzzel[2][0]) == int(puzzel[4][0]) and int(puzzel[0][1]) + int(puzzel[1][1]) + int(puzzel[2][1]) == int(puzzel[4][1]) and int(puzzel[0][2]) + int(puzzel[1][2]) + int(puzzel[2][2]) == int(puzzel[4][2]):
            break
    
    regel1 = " ".join(puzzel[0])
    regel2 = " ".join(puzzel[1])
    regel3 = " ".join(puzzel[2])


    zin = f"{teller} {regel1}\n{teller} {regel2}\n{teller} {regel3}"
    print(zin)
    teller += 1

