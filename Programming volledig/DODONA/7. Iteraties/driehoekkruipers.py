# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/2008047746
import random
GROOTGETAL = 100000
aantaldagen = GROOTGETAL
for i in range(GROOTGETAL):
    if random.randint(0,2):
        aantaldagen += 1
        while random.randint(0,1):
         aantaldagen += 1
print("{:2f}".format(aantaldagen/GROOTGETAL))
