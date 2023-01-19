# https://dodona.ugent.be/nl/courses/1751/series/19300/activities/1345545362

aantal = int(input())
counter = 1
list = []

for i in range(aantal):
    list = []
    radius = int(input())
    for i in range(radius):
        list.append(int(input()))
    print(f"{counter} {min(list)} {max(list)}")
    counter += 1

