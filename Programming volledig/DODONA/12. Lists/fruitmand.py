# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/582245450

def fruitstuk_toevoegen(lijst, fruitstuk):
    fruitset = set()

    for i in lijst:
        fruitset.add(i)

    if fruitstuk not in fruitset:
        for i in fruitset:
            if len(i) == len(fruitstuk):
                fruitset.remove(i)
                fruitset.add(fruitstuk)
                break
        else: 
            fruitset.add(fruitstuk)

    fruitlijst = list(fruitset)
    fruitlijst.sort(key = lambda x: len(x))

    return fruitlijst

def maak_fruitmand(lijst):
    fruitmand = []

    for i in lijst:
        fruitmand = fruitstuk_toevoegen(fruitmand, i)

    return fruitmand




