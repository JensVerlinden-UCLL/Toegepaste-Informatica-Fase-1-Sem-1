# https://dodona.ugent.be/nl/courses/1286/series/14368/activities/1509774218

from statistics import mean, median, mode
from collections import Counter

lijst = []

while True: 

    getal = int(input("Getal: "))

    if getal == 0:
        break

    lijst.append(getal)

if len( lijst ) == 0:
    print( "Er zijn geen getallen ingevoerd." )

else:

    gemiddelde = mean(lijst)
    mediaan = median(lijst)

    print(gemiddelde)
    print(mediaan)

    counter = Counter(lijst).most_common()

    if counter[0][1] > 1:
        for i in counter:
            if i[1] == counter[0][1]:
                print(i[0], end=' ')
            else: break

