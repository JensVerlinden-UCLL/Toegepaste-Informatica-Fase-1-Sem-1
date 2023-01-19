# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1150748783
import random
import math
n = int(input())
i = 0
m = 0
while i<n: 
    x = random.random()
    y = random.random()
    if math.sqrt(x**2 + y**2) <= 1:
        m += 1
    i += 1
pi = 4*m/n
print(pi)
