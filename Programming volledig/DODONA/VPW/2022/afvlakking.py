# https://dodona.ugent.be/nl/courses/1751/series/19301/activities/1708381797

def afvlakker(list):
    som = 0
    for i in range(len(list)):
        if i != 0 and int(list[i]) < int(list[i-1]):
            som += int(list[i-1]) - int(list[i])
            list[i] = list[i-1]
    return som


aantal = int(input())
counter = 1
for i in range(aantal):
    splijts = input()
    print(f"{counter} {afvlakker((splijts[1:].split()))}")
    counter += 1


