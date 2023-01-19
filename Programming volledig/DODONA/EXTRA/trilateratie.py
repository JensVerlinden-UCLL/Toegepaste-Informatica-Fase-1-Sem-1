# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/325610135

from math import sqrt

FOUTMARGE = 10**(-6) 
x1 = float(input())
y1 = float(input())
r1 = float(input())
x2 = float(input())
y2 = float(input())
r2 = float(input())

d = sqrt((x1-x2)**2 + (y1-y2)**2)

if abs(d - 0) < FOUTMARGE:
    positie = "concentrisch"
elif abs(d - abs(r1-r2)) < FOUTMARGE:
    positie = "binnen rakend"
elif abs(d - (r1 + r2)) < FOUTMARGE:
    positie = "buiten rakend"
elif d + FOUTMARGE < abs(r1-r2) or d - FOUTMARGE < abs(r1-r2): 
    positie = "omsluitend"
elif abs(r1-r2) < d + FOUTMARGE and d - FOUTMARGE < r1 + r2:
    positie = "snijdend"
else: positie = "gescheiden"

print(positie)

