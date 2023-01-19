# https://dodona.ugent.be/nl/courses/1286/series/14344/activities/1886659767

boekPrijs = 24.95
boekPrijsBoekwinkel = boekPrijs - (boekPrijs / 10 * 4)
verschepingEersteBoek = 3
verschepingBoek = 0.75
Totaalprijs60Boeken = 60 * boekPrijsBoekwinkel + verschepingEersteBoek + 59 * verschepingBoek
print(Totaalprijs60Boeken)
