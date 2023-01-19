# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1269944782


a = int(input())
b = int(input())
c = int(input())
d = int(input())

lijst = [a, b, c, d]

een = min(a, b, c, d)
vier = max(a, b, c, d)

lijst.remove(een)
lijst.remove(vier)

if lijst[0] < lijst[1]:
    twee = lijst[0]
    drie = lijst[1]
else:
    twee = lijst[1]
    drie = lijst[0]

tijd = twee + twee + vier + een + twee

if tijd > 60:
    tijd_uur = tijd // 60
    tijd_minuut = tijd % 60
    print(f"De snelste tijd om over te steken is {tijd_uur} uur en {tijd_minuut} minuten")
else: print(f"De snelste tijd om over te steken is {tijd} minuten")



