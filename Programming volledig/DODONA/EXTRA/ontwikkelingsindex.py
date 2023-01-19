# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/554093539

import math

landnaam = input()
le = float(input())
mys = float(input())
eys = float(input())
gnipc = float(input())

lei = (le - 20)/(82.3-20)
mysi = mys/13.2
eysi = eys/20.6
ei = (math.sqrt(mysi*eysi))/0.951
ii = (math.log(gnipc) - math.log(100))/(math.log(107721) - math.log(100))
hdi = (lei * ei * ii)**(1/3)

print(f'De HDI van {landnaam} bedraagt {hdi:.3f}.')

