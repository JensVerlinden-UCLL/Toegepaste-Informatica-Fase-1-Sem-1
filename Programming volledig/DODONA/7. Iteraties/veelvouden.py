# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/879249671

n = int(input("Geef een getal: "))
som = 0

for i in range(1, 101):
    product = n * i
    if product > 100:
        break
    else: som += product
print(som)
