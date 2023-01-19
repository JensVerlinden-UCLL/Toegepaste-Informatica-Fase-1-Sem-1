# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1275311286


def gemeenschappelijke_karakters(w1, w2):
    common = ""
    for i in w1:
        if i in w2 and i not in common:
            common += i
    return len(common)

woord1 = input("Woord 1: ")
woord2 = input("Woord 2: ")
aantal = gemeenschappelijke_karakters(woord1, woord2)
print(aantal)
