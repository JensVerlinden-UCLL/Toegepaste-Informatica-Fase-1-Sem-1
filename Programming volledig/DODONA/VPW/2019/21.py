# https://dodona.ugent.be/nl/courses/1751/series/19303/activities/416268136

aantal = int(input())
counter = 1

for i in range(aantal):
    kaarten = input().split()
    teller = 0
    som = 0

    for j in range(len(kaarten)):
        if som > 21:
            enen = kaarten[:laatste+1].count('1')
            if enen > 0:
                som -= 10
                index = kaarten[:laatste+1].index('1')
                kaarten[index] = 'x'
        if som >= 17:
            continue
        
        if kaarten[j] == '1':
            som += 11
            teller += 1
            laatste = j

        elif kaarten[j] == 'H' or kaarten[j] == 'D' or kaarten[j] == 'B':
            som += 10
            teller += 1
            laatste = j
        
        else:
            som += int(kaarten[j])
            teller += 1
            laatste = j

    print(f"{counter} {teller} {som}")

    counter += 1

