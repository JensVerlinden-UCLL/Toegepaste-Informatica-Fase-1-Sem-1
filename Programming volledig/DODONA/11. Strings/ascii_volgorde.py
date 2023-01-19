# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/335876740

tekst = input("Tekst: ")
ntekst = ""

while len( tekst ) > 0:
    ch = tekst[0]
    i = 0
    j = 1
    while j < len( tekst ):
        if tekst[j] < ch:
            ch = tekst[j]
            i = j
        j += 1
    tekst = tekst[:i] + tekst[i+1:]
    ntekst += ch
print( ntekst )