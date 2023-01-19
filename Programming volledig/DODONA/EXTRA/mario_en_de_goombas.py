# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/740205665

afstandT = int(input())
afstandA = int(input())
richtingA = (input())
afstandB = int(input())
richtingB = (input())

if richtingA == 'L':
    duurA = afstandT + afstandT - afstandA
else: duurA = afstandA

if richtingB == 'L':
    duurB = afstandT + afstandT - afstandB
else: duurB = afstandB

maxDuur = max(duurA, duurB)

print(f"Het duurt {maxDuur} minuten tot beide Goomba's weg zijn")
