# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1301141031

x1_start = int(input())
y1_start = int(input())
x2_start = int(input())
y2_start = int(input())
x3_start = int(input())
y3_start = int(input())
x4_start = int(input())
y4_start = int(input())

x1 = min(x1_start, x2_start)
x2 = max(x1_start, x2_start)
y1 = min(y1_start, y2_start)
y2 = max(y1_start, y2_start)
x3 = min(x3_start, x4_start)
x4 = max(x3_start, x4_start)
y3 = min(y3_start, y4_start)
y4 = max(y3_start, y4_start)

if x1 <= x3 and x3 < x2 and y1 < y4 and y3 < y2:
    print("botsing")
elif x3 <= x1 and x1 < x4 and y1 < y4 and y3 < y2:
    print("botsing")
else: print("geen botsing")
