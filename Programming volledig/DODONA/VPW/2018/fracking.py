# https://dodona.ugent.be/nl/courses/1751/series/19304/activities/1023475213

def groep(positie, rooster):
    x = positie[0]
    y = positie[1]

    cel = rooster[x][y]

    mogelijks = set()

    for i in range(len(rooster)):
        for j in range(len(rooster[i])):
            if rooster[i][j] == cel:
                mogelijks.add((i, j))

    oplossing = {positie}

    while True:

        flag = True

        for i in mogelijks:

            for j in oplossing:

                if abs(i[0] - j[0]) < 2 and abs(i[1] - j[1]) < 2 and (abs(i[0] - j[0]) == 1 and not abs(i[1] - j[1]) == 1 or not abs(i[0] - j[0]) == 1 and abs(i[1] - j[1]) == 1):
                    oplossing.add(i)
                    mogelijks.remove(i)
                    flag = False
                    break

            if not flag:
                break

        if flag:
            break
    
    return oplossing

aantal = int(input())
counter = 1

for i in range(aantal):
    rijen = int(input())
    kolommen = int(input())
    posities = []
    dag = 0

    for j in range(rijen):

        posities.append(list((input())))

    while True:

        sterretjes = set()

        for i in range(rijen):
            for j in range(kolommen):
                if posities[i][j] == "*":
                    sterretjes.add((i, j))

        flag2 = False

        totaalgroep = set()

        for i in sterretjes:
            groepster = groep((i[0], i[1]), posities)
            for j in groepster:

                if j[0] == rijen-1:
                    totaalgroep.update(groepster)
                    flag2 = True
                    break
                    

        flag3 = False

        for i in totaalgroep:
            if i[0] == 0:
                    flag3 = True
                    break

        if flag2 and flag3:
            veranderen = set()
            for i in sterretjes:
                if posities[min(i[0]+1, rijen-1)][i[1]] == '.' or posities[max(i[0]-1, 0)][i[1]] == '.' or posities[i[0]][min(i[1]+1, kolommen-1)] == '.' or posities[i[0]][max(i[1]-1, 0)] == '.':
                    veranderen.add((i[0], i[1]))

            for j in veranderen:
                posities[j[0]][j[1]] = '.'
            dag += 1

        else:  
            break
    
    print(f"{counter} {dag}")

    counter += 1



                


