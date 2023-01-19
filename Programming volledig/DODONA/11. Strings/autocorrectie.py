# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/804070970

zin = input("zin: ")

woordenlijst = (zin[0].upper() + zin[1:]).split()
laatstewoord = ""
nieuwezin = ""


for w in woordenlijst:

    if len( w ) > 2 and w[0] >= "A" and w[0] <= "Z" and w[1] >= "A" and w[1] <= "Z" and w[2] >= "a" and w[2] <= "z":
        w = w[0] + w[1].lower() + w[2:]

    if w == laatstewoord: 
        continue

    if w[0] >= "a" and w[0] <= "z":
        for c in w[1:]:
            if not (c >= "A" and c <= "Z"):
                break
        else:
            w = w[0].upper() + w[1:].lower()

    dag = w.lower()
    if dag == "zondag" or dag == "maandag" or dag == "dinsdag" or dag == "woensdag" or dag == "donderdag" or dag == "vrijdag" or dag == "zaterdag":
        w = dag[0].upper() + dag[1:]
        
    nieuwezin += w + " "
    laatstewoord = w


nieuwezin = nieuwezin.strip()
print( nieuwezin )
