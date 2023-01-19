# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/715315832

# bedrag (in cent)
bedrag = 1156
dollars = bedrag//100
kwartjes = (bedrag%100)//25
dubbeltjes = ((bedrag%100)%25)//10
stuivers = (((bedrag%100)%25)%10)//5
cents = (((bedrag%100)%25)%10)%5
print("Dollars:", dollars)
print("Kwartjes:", kwartjes)
print("Dubbeltjes:", dubbeltjes)
print("Stuivers:", stuivers)
print("Centen:", cents)
