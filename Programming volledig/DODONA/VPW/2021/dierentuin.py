# https://dodona.ugent.be/nl/courses/1751/series/19302/activities/1174274264

aantal = int(input())
teller = 1

for i in range(aantal):
    weggooien = input()
    dierenaantal = input().split()
    som = 0

    for i in dierenaantal:
        som += int(i)

    print(f"{teller} {som}")

    teller += 1
