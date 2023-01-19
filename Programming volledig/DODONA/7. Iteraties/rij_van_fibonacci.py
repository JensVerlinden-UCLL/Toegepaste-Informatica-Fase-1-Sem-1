# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1952876754
grootteFibonacciNummers= int(input("Geef het aantal gewenste Fibonaccinummers: "))
j = 0
k = 1
while j <= grootteFibonacciNummers:
    print(j)
    som = k + j
    j = k
    k = som
print(j)



