# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1273258863

list = []

while True:
    kleur = input()

    if kleur == 'STOP':
        break
    elif kleur == '?':
        if len(list):
            print(list[0])
            del list[0]
        else: print("GEEN KLEUR IN LIJST")       
    
    else: list.append(kleur)
    



