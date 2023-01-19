# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/373633979

lijst = [1, 3, 7, 2, 5, 6, 3, 8, 5, 7, 6, 1]
lijst.sort()


for i in lijst:

    first = lijst.index(i)
    counter = lijst.count(i)

    if counter > 1:

        for j in range(counter-1):
            lijst.remove(first)

print(lijst)







