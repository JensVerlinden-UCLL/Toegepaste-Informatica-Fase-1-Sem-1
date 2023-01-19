#https://dodona.ugent.be/nl/courses/1751/series/19301/activities/2026723997

aantal = int(input())
counter = 1

for i in range(aantal):
    uitkomst = 10
    uitslagen = input().split()

    for i in range(len(uitslagen)):
        uitslagen[i] = int(uitslagen[i])

    if uitslagen[0] > 1:
        if uitslagen[0] > 7:
            uitkomst -= 3
        elif uitslagen[0] > 5:
            uitkomst -= 2
        else: uitkomst -= 1

    if uitslagen[1] > 0:
        if uitslagen[1] >= 6:
            uitkomst -= 2
        else: uitkomst -= 1

    if uitslagen[2] >= 10:
        if uitslagen[2] >= 500:
            uitkomst -= 4
        elif uitslagen[2] >= 300:
            uitkomst -= 3
        elif uitslagen[2] >= 90:
            uitkomst -= 2
        else: uitkomst -= 1

    if uitslagen[3] > 2:
        if uitslagen[3] >= 6:
            uitkomst -= 3
        elif uitslagen[3] > 3:
            uitkomst -= 2
        else: uitkomst -= 1
    
    if uitkomst < 1:
        uitkomst = 1

    print(f"{counter} {uitkomst}")

    counter += 1



