# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1100982831

counter = 0
maxserie = 0
serie = int(input())
maxserie = 0

while serie > 0:
    counter += 1
    maxserie = max(serie, maxserie)    
    serie = int(input())

berekening = round((((counter + 1) * maxserie) / counter) - 1)

print(f"Het aantal geproduceerde tanks wordt geschat op {berekening}.")

