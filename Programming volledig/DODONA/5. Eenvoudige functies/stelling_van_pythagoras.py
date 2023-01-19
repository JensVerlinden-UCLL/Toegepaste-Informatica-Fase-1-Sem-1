# https://dodona.ugent.be/nl/courses/1286/series/14346/activities/1422122823
import math
rechthoekszijde1 = float(input("Geef afmeting van rechthoekszijde: "))
rechthoekszijde2 = float(input("Geef afmeting van rechthoekszijde: "))
schuinezijde = math.sqrt(rechthoekszijde1**2 + rechthoekszijde2**2)
print("Lengte van de schuine zijde: {:.3f}".format(schuinezijde))