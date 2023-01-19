# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/960794524


import math

x = float(input())
y = float(input())

r = math.sqrt(x**2 + y**2)

if x == 0:
    if y > 0:
        phi = math.pi/2
    else: phi = math.pi/2 * 3
else: phi = math.atan(y/x)

b = math.pi/2 + math.pi/20 - phi

sector = b/(math.pi/10) + 1

if x < 0:
    sector += 10

if sector > 20:
    sector -= 20

if r > 170:
    sector = 0

if r < 6.35:
    sector = 50

if 6.35 <= r <= 15.9:
    sector = 25

if 97.4 <= r <= 107:
    sector *= 3

if 160.4 <= r <= 170:
    sector *= 2

print(int(sector))