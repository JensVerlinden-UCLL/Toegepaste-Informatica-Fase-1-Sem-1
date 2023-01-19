# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/683768040

import math

n = int(input())

for a in range(1, n):
    for b in range(a, n):
        c = math.sqrt( a * a + b * b)
        if c % 1 == 0 and a + b + c == n:
            print(f"({a}, {b}, {int(c)})")
