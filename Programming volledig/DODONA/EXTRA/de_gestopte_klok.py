# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1477235114

uur1= int(input())
minuut1= int(input())
uur2= int(input())
minuut2= int(input())
uur3= int(input())
minuut3= int(input())
uur4= int(input())
minuut4= int(input())

duur_trip = (((uur4-uur1)*60 + minuut4-minuut1) - ((uur3-uur2)*60 + minuut3-minuut2)) / 2

if uur4 < uur1:
    nieuw_uur4 = uur4 + 24
    duur_trip = (((nieuw_uur4-uur1)*60 + minuut4-minuut1) - ((uur3-uur2)*60 + minuut3-minuut2)) / 2
    

if uur3 < uur2:
    nieuw_uur3 = uur3 + 24
    duur_trip = (((uur4-uur1)*60 + minuut4-minuut1) - ((nieuw_uur3-uur2)*60 + minuut3-minuut2)) / 2

if uur3 < uur2 and uur4 < uur1:
    duur_trip = (((nieuw_uur4-uur1)*60 + minuut4-minuut1) - ((nieuw_uur3-uur2)*60 + minuut3-minuut2)) / 2

duur_trip_uren = duur_trip // 60
duur_trip_minuten = duur_trip % 60

nieuw_uur = uur3 + duur_trip_uren
nieuw_minuten = minuut3 + duur_trip_minuten
nieuw_uur += nieuw_minuten // 60
nieuw_minuten = nieuw_minuten % 60

if nieuw_uur > 24:
    nieuw_uur -= 24

print(int(nieuw_uur))
print(int(nieuw_minuten))
