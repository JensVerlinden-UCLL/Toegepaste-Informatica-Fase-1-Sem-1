# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/623087135

def nieuw_kaartspel(list1, list2):

    list3 = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            list3.append(f"{list1[i]}{list2[j]}")
    
    return list3

def splits_kaartspel(list1):

    list3 = []
    list4 = []

    for i in range(len(list1)//2):

            list3(list1[i])
        
    for j in range(len(list1)//2, len(list1)):

            list4.append(list1[j])
        
    return (list3, list4)

def faro_shuffle(list1, list2):

    list3 = []

    for i in range(max(len(list1), len(list2))):

        if i < len(list1):
            list3.append(list1[i])
        if i < len(list2):
            list3.append(list2[i])

    return list3

