# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1303919335

from sys import flags


d = float(input())
r = float(input())
s = int(input())

for i in range(s):
    print(d)
    d = r*d * (1-d)
