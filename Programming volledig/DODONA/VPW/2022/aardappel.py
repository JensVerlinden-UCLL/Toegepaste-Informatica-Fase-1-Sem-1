# https://dodona.ugent.be/nl/courses/1751/series/19301/activities/670443449

aantal = int(input())
teller = 1
for i in range(aantal):
    counter = 0
    string_lijst = input().split()
    lijst = [int(i) for i in string_lijst]
    while True:
        if abs(max(lijst[2:]) - min(lijst[2:])) > lijst[0]:
            high1 = max(lijst[2:]) // 2
            high2 = max(lijst[2:]) - max(lijst[2:]) // 2
            lijst.pop(lijst.index(max(lijst[2:]), 2))
            lijst.append(high1)
            lijst.append(high2)
            counter += 1
        else: break
    print(f"{teller} {counter}")
    teller += 1


