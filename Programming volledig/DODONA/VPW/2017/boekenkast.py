# https://dodona.ugent.be/nl/courses/1751/series/19305/activities/1819447128


aantal = int(input())

counter = 1

for i in range(aantal):

    boekenrekken = input().split()[1:]

    aantal_rekken = len(boekenrekken)

    for k in range(len(boekenrekken)):
        boekenrekken[k] = int(boekenrekken[k])

    boekenrekken.sort(reverse=True)

    reknummer = 0

    aantal_boeken = int(input())

    boekensom = 0

    flag = True

    if aantal_boeken == 0:
        reknummer = -1

    boekenlijst = []

    for j in range(aantal_boeken):
        boekenlijst.append(input().split())

    boekenlijst.sort(key = lambda x: " ".join(x[1:]))
        

    for j in boekenlijst:

        boekbreedte = j[0]

        boekbreedte = int(boekbreedte)

        if not flag:
            break

        while True:
            
            if reknummer > aantal_rekken - 1:
                    flag = False
                    print(f"{counter} ONMOGELIJK")
                    break

            boekensom += boekbreedte


            if boekensom > boekenrekken[reknummer]:
                boekensom = 0
                reknummer += 1

                continue

            else: break
        
        
    
    if flag:
        print(f"{counter} {reknummer+1}")
    
    counter += 1
            


        