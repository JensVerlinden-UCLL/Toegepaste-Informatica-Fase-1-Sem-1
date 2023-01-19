# https://dodona.ugent.be/nl/courses/1751/series/19304/activities/963346109

aantal = int(input())
counter = 1

for i in range(aantal):
    bedrag = int(input())
    transacties = [int(x) for x in input().split()[1:]]
    transacties.sort()

    for k in transacties:
        bedrag += k

        if bedrag < 0:
            bedrag -= 35

    print(f"{counter} {bedrag}")

    counter += 1