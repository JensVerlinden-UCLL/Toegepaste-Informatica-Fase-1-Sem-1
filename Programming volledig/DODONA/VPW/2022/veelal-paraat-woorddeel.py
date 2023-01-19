# https://dodona.ugent.be/nl/courses/2013/series/21915/activities/1284657693

aantal = int(input())
counter = 1

for i in range(aantal):
    ondergrens = int(input())

    stringsaantal = int(input())

    stringreeks = []
    substringreeks = []
    eindstrings = set()

    for j in range(stringsaantal):

        stringeling = input()
        stringreeks.append(stringeling)

        substringeling = [stringeling[i: j] for i in range(len(stringeling))
          for j in range(i + 1, len(stringeling) + 1)]
        
        substringreeks.append(substringeling)

    for i in range(len(substringreeks)):
        for j in range(len(substringreeks[i])):
            teller = 0
            for k in range(len(stringreeks)):
                if substringreeks[i][j] in stringreeks[k]:
                    teller += 1

                    if teller == ondergrens:
                        eindstrings.add(substringreeks[i][j])
    if len(eindstrings) == 0:
        print(f"{counter} ONMOGELIJK")

    else: 
        removableString = []
        maximus = list(eindstrings)
        maximus.sort(key = lambda x: len(x))
        maximus = maximus[-1]

        for j in eindstrings:
            if len(j) != len(maximus):
                removableString.append(j)

        for q in removableString:

            eindstrings.remove(q)

        sortedlist = list(eindstrings)
        sortedlist.sort()

        print(f"{counter} {' '.join(sortedlist)}")

    counter += 1

