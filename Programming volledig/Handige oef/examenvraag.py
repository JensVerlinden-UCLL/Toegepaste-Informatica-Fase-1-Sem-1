#variabelen definieren
nieuw_lijst = []
beginlijsten = set()
eindlijst = []
eindtekst = ''


#csv binnenhalen
fp = open(".\\Handige oef\\examenvraag.csv", "r")

lijst = [x.strip() for x in fp.read().splitlines()[1:]]


fp.close()



#csv elementen nog eens splitten
for i in lijst:
    nieuw_lijst.append(i.split(","))


#voornamen wegschrijven in set
for i in nieuw_lijst:
    beginlijsten.add(i[0])


#gemiddelde leeftijden berekenen
for i in beginlijsten:
    gemiddelde = 0
    count = 0
    for j in nieuw_lijst:
        if j[0] == i: 
            gemiddelde += int(j[2])
            count += 1

    gemiddelde //= count

    eindlijst.append([i, gemiddelde])

eindlijst.sort(key = lambda x: x[0])

#resultaten wegschrijven naar csv-layout
for i in eindlijst:
    eindtekst += f"{i[0]}, {i[1]}\n"


#resultaten wegschrijven naar csv
fp = open("examenvraag_output.csv", "w")

fp.write(eindtekst)

fp.close()
