# https://dodona.ugent.be/nl/courses/1751/series/19303/activities/320068692
def uurcalculatie(lijst):
    if lijst[1] >= 60:
        lijst[0] += lijst[1] // 60
        lijst[1] = lijst[1] % 60
    if lijst[3] >= 60:
        lijst[2] += lijst[3] // 60
        lijst[3] = lijst[3] % 60
    return lijst

def uitstellen(lijst1, lijst2):
    berekening = (lijst2[0] - lijst1[2]) * 60 - lijst1[3] + lijst2[1]

    if berekening < 60:
        lijst2[1] += 60 - berekening
        lijst2[3] += 60 - berekening
        uurcalculatie(lijst2)

aantal = int(input())
counter = 1

for i in range(aantal):
    variabelen = input().split()
    vertraging = int(variabelen[0])
    aantal_vluchten = int(variabelen[1])
    vluchten = []

    for j in range(aantal_vluchten):
        vluchten.append([int(x) for x in input().split()])

    vluchten[0][1] += vertraging
    vluchten[0][3] += vertraging

    uurcalculatie(vluchten[0])

    for k in range(1, len(vluchten)):
        uitstellen(vluchten[k-1], vluchten[k])

    print(f"{counter} {vluchten[len(vluchten)-1][2]} {vluchten[len(vluchten)-1][3]}")

    counter += 1

