# https://dodona.ugent.be/nl/courses/2013/series/21915/activities/1114804683
from copy import copy

aantal = int(input())
counter = 1

for i in range(aantal):

    vriend = input().split()
    vriend.sort()

    ik = input().split()
    ik.sort()
    vriendDNF = vriend.count("DNF")

    ikDNF = ik.count("DNF")

    if vriendDNF > 1:

        if ikDNF > 1:

            print(f"{counter} onmogelijk nog te winnen")

        elif ikDNF == 1:

            print(f"{counter} 600.00")

        else:
            print(f"{counter} reeds gewonnen")

    else:

        if ikDNF > 1:
            print(f"{counter} onmogelijk nog te winnen")
        
        else:

            vriendScore = copy(vriend)
            ikPro = copy(ik)
            ikBad = copy(ik)
            ikScore = copy(ik)

            if ikPro.count("DNF") == 1:
                ikPro.pop(-1)
                ikPro.append("600.00")
            
            if ikBad.count("DNF") == 1:
                ikBad.pop(-1)
                ikBad.append("600.00")
            
            if vriendScore.count("DNF") == 1:
                vriendScore.pop(-1)
                vriendScore.append("600.00")

            if ikScore.count("DNF") == 1:
                ikScore.pop(-1)
                ikScore.append("600.00")

            vriendScore.sort(key = lambda x: float(x))
            ikPro.sort(key = lambda x: float(x))
            ikBad.sort(key = lambda x: float(x))
            ikScore.sort(key = lambda x: float(x))

            
            vriendScore.pop(0)
            vriendScore.pop(-1)
            ikPro.pop(0)
            ikBad.pop(-1)
            ikScore.pop(0)
            ikScore.pop(-1)

            schatScore = 0
            proScore = 0
            badScore = 0
            totaalScore = float(ikScore[0]) + float(ikScore[1]) 
            
            for i in range(len(vriendScore)):
                schatScore += float(vriendScore[i])

            for i in range(len(ikPro)):
                proScore += float(ikPro[i])

            for i in range(len(ikBad)):
                badScore += float(ikBad[i])

            if badScore >= schatScore:
                print(f"{counter} onmogelijk nog te winnen")

            elif proScore < schatScore:
                print(f"{counter} reeds gewonnen")

            else:
                print(f"{counter} {(schatScore - 0.01 - totaalScore):.2f}")
    
    counter += 1





