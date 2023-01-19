# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1797346540

uur1 = int(input())
minuut1 = int(input())
uur2 = int(input())
minuut2 = int(input())
tarief = 0

if uur1 < 18 or uur2 < 18 or uur1 > uur2:
    print("invalid input")
else:
    if (uur1*60 + minuut1) <= (21*60 +30):
        tarief1 = ((21*60 +30) - (uur1*60 + minuut1)) * (2/60)
        tarief += tarief1
        if (uur2*60 + minuut2) <= (21*60 +30):
            aftrektarief = ((21*60 +30) - (uur2*60 + minuut2)) * (2/60)
            tarief -= aftrektarief
    if (uur2*60 + minuut2) > (21*60 +30):
        tarief1 = ((uur2*60 + minuut2) - (21*60 +30)) * (4/60)
        tarief += tarief1
        if (uur1*60 + minuut1) > (21*60 +30):
            aftrektarief = ((uur1*60 + minuut1) - (21*60 +30)) * (4/60)
            tarief -= aftrektarief
    print(tarief)