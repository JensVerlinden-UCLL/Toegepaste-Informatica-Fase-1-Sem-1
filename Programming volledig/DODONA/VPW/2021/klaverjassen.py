# https://dodona.ugent.be/nl/courses/1751/series/19302/activities/638010549


aantal = int(input())

counter = 1

for i in range(aantal):

    troef = input()

    som = 0

    kaarten = input().split()

    for i in kaarten:

        if i[0] == troef:
            if i[1:] == "B":
                som += 20

            elif i[1:] == "9":
                som += 14

        else:
            if i[1:] == "B":
                som += 2

        if i[1:] == "A":
            som += 11

        elif i[1:] == "10":
            som += 10

        elif i[1:] == "H":
            som += 4

        elif i[1:] == "D":
            som += 3

    print(f"{counter} {som}")

    counter += 1
