# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/191240337
from cmath import sqrt
import math


import math
m = int(input())
n = int(input())
q = int(math.sqrt(n))
for i in range(0, q+1):
    for j in range(i, q+1):
        l = i**2 + j**2
        if m <= l <= n:
            print(i, "** 2 +", j, "** 2 =", l)
