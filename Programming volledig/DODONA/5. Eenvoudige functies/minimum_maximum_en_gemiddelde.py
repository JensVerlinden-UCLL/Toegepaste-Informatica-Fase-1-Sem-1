# https://dodona.ugent.be/nl/courses/1286/series/14346/activities/723647984
getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef een getal: "))
getal3 = int(input("Geef een getal: "))
minimum = min(getal1, getal2, getal3)
maximum = max(getal1, getal2, getal3)
gemiddelde = (getal1 + getal2 + getal3)/3
print("maximum:", maximum)
print("minimum:", minimum)
print("gemiddelde: {:.2f}".format(gemiddelde))