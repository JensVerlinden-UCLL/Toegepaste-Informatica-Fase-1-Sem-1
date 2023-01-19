# https://dodona.ugent.be/nl/courses/1751/series/19304/activities/2119514143

aantal = int(input())
counter = 1

for i in range(aantal):
    posities = int(input())
    coordinaten = []
    for j in range(posities):
        coordinaten.append([int(x) for x in input().split()])
        
    if len(coordinaten) != 0:
        som = abs(coordinaten[0][0]) + abs(coordinaten[0][1])
    else: som = 0

    for i in range(1,len(coordinaten[1:])+1):
        som += abs(coordinaten[i-1][0] - coordinaten[i][0]) + abs(coordinaten[i-1][1] - coordinaten[i][1])

    print(f"{counter} {som}")

    counter += 1

