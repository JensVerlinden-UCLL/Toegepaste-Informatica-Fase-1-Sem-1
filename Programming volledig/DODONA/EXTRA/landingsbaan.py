# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1954949630

getal = float(input())

landing1 = round(getal/10)
if landing1 == 0:
    landing1 = 36

landing2 = landing1 + 18
if landing2 > 36:
    landing2 -= 36

minlanding = min(landing1, landing2)
maxlanding = max(landing1, landing2)

if minlanding < 10:
    minlanding = f"0{minlanding}"

print(f"{minlanding}/{maxlanding}")

