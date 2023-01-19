# https://dodona.ugent.be/nl/courses/1751/series/19302/activities/1135736597

aantal = int(input())
teller = 1

for i in range(aantal):
    getalllen = input().split()
    getalllen = [int(i) for i in getalllen]
    geld = getalllen[0] * getalllen[1]
    prijsL = getalllen[1]
    prijsV = getalllen[2]

    aantal_bakken = 0

    while geld >= prijsV:
        aantal_bakken += geld//prijsV
        geld += -(geld//prijsV)*prijsV + (geld//prijsV)*prijsL

    print(f"{teller} {aantal_bakken} {geld}")

    teller += 1

    
