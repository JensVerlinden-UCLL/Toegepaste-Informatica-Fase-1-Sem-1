# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/1014821966


zin = input("Geef je zin weer: ")
klinkerCount = 0
if 'i' in zin or 'I' in zin:
    klinkerCount += 1
if 'a' in zin or 'A' in zin:
    klinkerCount += 1
if 'e' in zin or 'E' in zin:
    klinkerCount += 1
if 'o' in zin or 'O' in zin:
    klinkerCount += 1
if 'u' in zin or 'U' in zin:
    klinkerCount += 1
if klinkerCount == 0:
    print("De zin bevat geen klinkers.")
elif klinkerCount == 1:
    print("De zin bevat slechts 1 verschillende klinker.")
else: print("De zin bevat {} verschillende klinkers.".format(klinkerCount))