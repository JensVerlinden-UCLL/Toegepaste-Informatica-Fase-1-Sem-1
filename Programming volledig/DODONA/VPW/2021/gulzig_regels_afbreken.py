# https://dodona.ugent.be/nl/courses/1751/series/19302/activities/2112627453

aantal = int(input())

counter = 1

for i in range(aantal):

    max_length = int(input())

    zin = input().split()

    regel = 0

    strooi = 0

    for j in range(len(zin)):

        if j == 0:
            regel += len(zin[j])
        else:
            regel += 1 + len(zin[j])

        if regel > max_length:
            regel -= 1 + len(zin[j])
            strooi += (max_length - regel)**2
            regel = len(zin[j])
        
        if j == len(zin) - 1:
            strooi += (max_length - regel)**2

    print(f"{counter} {strooi}")

    counter += 1

