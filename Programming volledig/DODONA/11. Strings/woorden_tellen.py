# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/2032693594

woord = input("Woord: ")
tekst = input("Tekst: ")
counter = 0

start = -1

def schoon( s ):
    ns = ""
    s = s.lower()
    for c in s:
        if c >= "a" and c <= "z" or c in ("'", "-", "_"):
            ns += c
        else:
            ns += " "
    return ns

for i in schoon( tekst ).split():
    if i == woord:
        counter += 1

print(f"Aantal keren dat het woord \"{woord}\" voorkomt: {counter}")