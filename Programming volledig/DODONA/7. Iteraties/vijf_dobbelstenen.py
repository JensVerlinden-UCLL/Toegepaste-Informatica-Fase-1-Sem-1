# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1330491283
from random import randint
POGINGEN = 10000000
DOBBELSTENEN = int(input("Aantal dobbelstenen: "))

succes = 0

for i in range( POGINGEN ):
    laatste = 0
    for j in range( DOBBELSTENEN ):
        waarde = randint( 1, 6 )
        if waarde < laatste:
            break
        laatste = waarde
    else:
        succes += 1
        
print( "P(niet-dalende reeks van", DOBBELSTENEN, "dobbelstenen) = {:.6f}".format( succes/POGINGEN ) )