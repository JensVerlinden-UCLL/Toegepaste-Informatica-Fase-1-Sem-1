# https://dodona.ugent.be/nl/courses/2013/series/21915/activities/321509161

aantal = int(input())
counter = 1


for i in range(aantal):
    values = [int(x) for x in input().split()]
    W = values[0]
    O = values[1]
    HW = values[2]
    HO = values[3]

    if W > O:
        hoogste = W
        laagste = O
        hoogsteH = HW
        laagsteH = HO
    else:
        hoogste = O
        laagste = W
        hoogsteH = HO
        laagsteH = HW

    while hoogste != laagste and hoogste > laagsteH and hoogsteH < hoogste:
        laagste += 1
        hoogste -= 1

    if hoogste == laagste:
        print(f"{counter} gelijk")

    elif W > O:
        print(f"{counter} {hoogste} {laagste}")

    else:
        print(f"{counter} {laagste} {hoogste}")

    counter += 1
