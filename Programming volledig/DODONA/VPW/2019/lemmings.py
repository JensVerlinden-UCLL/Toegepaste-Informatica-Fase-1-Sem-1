# https://dodona.ugent.be/nl/courses/1751/series/19303/activities/1098651022

aantal = int(input())
counter = 1

for i in range(aantal):
    breedte = int(input())
    aantal_lemmings = int(input())
    lemmings = []
    teller = 0

    for i in range(aantal_lemmings):
        lemmings.append(input())

    while True:
        flag = True
        removing = set()
        for k in lemmings:
            if k[0] != '0':
                flag = False
            else: removing.add(k)
        
        for k in removing:
            lemmings.remove(k)

        if flag:
            break

        dubbel = set()

        for k in range(len(lemmings)):
            for l in range(len(lemmings)):
                if lemmings[k][:len(lemmings[k])-1] == lemmings[l][:len(lemmings[l])-1] and k != l:
                    dubbel.add(k)
                    dubbel.add(l)

        for s in range(len(lemmings)):
            if lemmings[s][:len(lemmings[s])-1] == str(breedte):
                    dubbel.add(s)

        for a in dubbel:
            if lemmings[a][len(lemmings[a])-1] == 'R':
                lemmings[a] = f'{lemmings[a][:len(lemmings[a])-1]}L'
            else: lemmings[a] = f'{lemmings[a][:len(lemmings[a])-1]}R'

        for m in range(len(lemmings)):
            if lemmings[m][len(lemmings[m])-1] == 'R':
                lemmings[m] = f"{int(lemmings[m][:len(lemmings[m])-1]) + 1}R"
            else: lemmings[m] = f"{int(lemmings[m][:len(lemmings[m])-1]) - 1}L"

        teller += 1

    print(f"{counter} {teller}")

    counter += 1

        


