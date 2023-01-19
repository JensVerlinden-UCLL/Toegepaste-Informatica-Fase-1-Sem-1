# https://dodona.ugent.be/nl/courses/1751/series/19304/activities/1796921406

from math import sqrt

aantal = int(input())
counter = 1

for i in range(aantal):
    krachten = input().split()
    A = int(krachten[0])
    V = int(krachten[1])
    U = int(krachten[2])

    kracht = max(10, int((A * sqrt(V) * sqrt(U) * 0.7903 ** 2) / 10))
    print(f"{counter} {kracht}")

    counter += 1

