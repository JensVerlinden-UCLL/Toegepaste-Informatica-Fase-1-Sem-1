# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/581560564

import random

# Zet onderstaande regel uit commentaar als je indient op Dodona. Anders kan Dodona onmogelijk je programma controleren.
random.seed(1)    # enkel bij indienen op Dodona

kopteller = 0
muntteller = 0

for i in range(int(input())):
    if random.randint(0,1):
        kopteller += 1
    else:
        muntteller += 1

if kopteller > muntteller:
    print("Kop is meest geworpen")

elif kopteller < muntteller:
    print("Munt is meest geworpen")

else:
    print("Munt en kop zijn evenveel geworpen")