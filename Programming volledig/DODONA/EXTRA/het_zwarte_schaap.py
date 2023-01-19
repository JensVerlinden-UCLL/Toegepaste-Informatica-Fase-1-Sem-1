# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/267979422

getal1 = int(input())
getal2 = int(input())
getal3 = int(input())

if getal1 == getal2:
    print(f"Het derde getal, nl. {getal3} is het zwarte schaap.")
elif getal1 == getal3:
    print(f"Het tweede getal, nl. {getal2} is het zwarte schaap.")
else: 
    print(f"Het eerste getal, nl. {getal1} is het zwarte schaap.")