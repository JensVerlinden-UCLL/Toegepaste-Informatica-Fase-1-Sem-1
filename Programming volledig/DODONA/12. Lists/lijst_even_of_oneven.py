# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/1624746422

aantal = int(input("Aantal: "))

even = []
oneven = []

for i in range(aantal):
    
    getal = int(input("Getal: "))

    if getal % 2 == 0:
        even.append(getal)
    else: 
        oneven.append(getal)

print(even)
print(oneven)
