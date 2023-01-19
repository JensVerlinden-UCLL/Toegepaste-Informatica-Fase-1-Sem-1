# https://dodona.ugent.be/nl/courses/1751/series/19303/activities/437020999

aantal = int(input())
counter = 1

for i in range(aantal):
    getallen = int(input())
    woord = 0
    for j in range(1,getallen+1):
        woord += len(str(j))

    print(f"{counter} {woord}")

    counter += 1
    