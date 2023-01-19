# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/105361566

rotatie = int(input("Rotatie: "))
zin = input("Zin: ")

nieuwe_zin = ""

for i in zin:
    if i >= "a" and i <= "z":
        rotation = ord(i) - rotatie
        if rotation < ord("a"):
            rotation += 26
        nieuwe_zin  += chr(rotation)
    elif i >= "A" and i <= "Z":
        rotation = ord(i) - rotatie
        if rotation < ord("A"):
            rotation += 26
        nieuwe_zin  += chr(rotation)
    else: nieuwe_zin += i

print(nieuwe_zin)


