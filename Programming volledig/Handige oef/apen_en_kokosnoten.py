# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/967703372
aantalPiraten = int(input("Aantal piraten: "))
kokosnoten = 0
while True:
    kokosnoten += 1
    stapel = kokosnoten
    for i in range( aantalPiraten ):
        if stapel % aantalPiraten != 1:
            break
        stapel = (aantalPiraten-1) * ( (stapel - 1) / aantalPiraten )
    if stapel % aantalPiraten == 1:
        break
print( kokosnoten )

