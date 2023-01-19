# https://dodona.ugent.be/nl/courses/1286/series/14368/activities/1266518248

from collections import Counter

data = [ "appel", "banaan", "appel", "banaan", "appel", "kers" ]
c = Counter( data )
print( c )
print( c.most_common(1))

data2 = [ "mango", "kers", "kers", "kers", "kers" ]
c.update( data2 )
print( c )
print( c.most_common())

worst = "Hallo ik ben jens en ik ben reeds 17 jaar oud"
d = Counter(worst.replace(' ', ''))
print(d.most_common(5))