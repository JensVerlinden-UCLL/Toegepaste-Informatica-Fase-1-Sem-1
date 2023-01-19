# https://dodona.ugent.be/nl/courses/1751/series/19305/activities/1232377494

aantal = int(input())

counter = 1

for i in range(aantal):

    temperaturen = []

    teller = []

    pieken = 0

    flag = False

    while True:

        temperatuur = input()

        if temperatuur == "stop":
            break

        temperaturen.append(float(temperatuur))

    for i in range(len(temperaturen)):
        if flag:
            break

        if temperaturen[i] >= 25:
            teller.append(temperaturen[i])
        else:
            if len(teller) > 4:

                for j in teller:
                    if j >= 30:
                        pieken += 1

                if pieken > 2:
                    print(f"{counter} {i - len(teller) + 1} {len(teller)}")
                    flag = True
                    continue
                else:
                    teller.clear()
                    pieken = 0
            else:
                teller.clear()
                pieken = 0
    
    if not flag:
        print(f"{counter} geen hittegolf")

    counter += 1



