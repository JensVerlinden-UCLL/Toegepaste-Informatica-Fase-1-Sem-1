# https://dodona.ugent.be/nl/courses/1751/series/19301/activities/1309256027
from copy import copy
aantal = int(input())
counter = 1
for i in range(aantal):
    tests = int(input())
    flag = True
    lists = []
    for i in range(tests):
        list = input().split()
        for j in range(len(list)):
            new_list = list[j:] + list[:j]
            reverse_list = copy(new_list)
            reverse_list.reverse()
            if new_list in lists or reverse_list in lists:
                flag = False
                print(f"{counter} {list[0]} {list[1]} {list[2]} {list[3]} {list[4]} {list[5]} kwam eerder voor")
                break
        else:
            lists.append(list)
    if flag:
        print(f"{counter} geen duplicaten")
    counter += 1

