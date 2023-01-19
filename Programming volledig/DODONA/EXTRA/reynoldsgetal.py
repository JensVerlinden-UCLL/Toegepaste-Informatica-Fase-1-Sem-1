# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/387716745

v = float(input())
l = float(input())
p = float(input())
u = float(input())

reynoldsgetal = v * l * p / u

if reynoldsgetal < 2000:
    stroming = "laminaire stroming"
elif reynoldsgetal < 4000:
    stroming = "omslagstroming"
else: stroming = "turbulente stroming"

print(f"{reynoldsgetal} ({stroming})")
