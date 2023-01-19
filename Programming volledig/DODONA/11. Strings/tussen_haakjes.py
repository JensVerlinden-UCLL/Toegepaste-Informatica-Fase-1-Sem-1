# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/954463058

woord = input("Woord: ")
nieuw_woord = ""

start = 0
while True:
    start = woord.find( "[", start )
    if start < 0:
        break
    eind = woord.find( "]", start )
    if eind < 0:
        break
    nieuw_woord += woord[start+1:eind]
    start = eind 

print(nieuw_woord)
