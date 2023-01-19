# https://dodona.ugent.be/nl/courses/1751/series/19302/activities/1663636919

def checker(beginstations, eindstations, stationlijst, start, i):
            
        for j in range(len(eindstations[start+1:])):
            if i != j+start+1 and eindstations[j+start+1] != eindstations[i] and beginstations[i] != eindstations[i] and beginstations[j+start+1] != eindstations[j+start+1]:
                check = checker(beginstations, eindstations, stationlijst, j+start+1, i)
                check2 = checker2(beginstations, eindstations, stationlijst, i, j+start+1)
                if stationlijst[beginstations[i]-1][eindstations[i]-1] >= stationlijst[beginstations[i]-1][eindstations[j+start+1]-1] and stationlijst[beginstations[j+start+1]-1][eindstations[j+start+1]-1] >= stationlijst[beginstations[j+start+1]-1][eindstations[i]-1]:
                    if  check <= stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j+start+1]-1] + stationlijst[beginstations[j+start+1]-1][eindstations[j+start+1]-1] - stationlijst[beginstations[j+start+1]-1][eindstations[i]-1] and check2 <= stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j+start+1]-1] + stationlijst[beginstations[j+start+1]-1][eindstations[j+start+1]-1] - stationlijst[beginstations[j+start+1]-1][eindstations[i]-1]:
                        return stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j+start+1]-1] + stationlijst[beginstations[j+start+1]-1][eindstations[j+start+1]-1] - stationlijst[beginstations[j+start+1]-1][eindstations[i]-1]
        else: return 0
                
def checker2(beginstations, eindstations, stationlijst, start, j):
    for i in range(len(beginstations[start+1:])):
        if i+start+1 != j and eindstations[j] != eindstations[i+start+1] and beginstations[i+start+1] != eindstations[i+start+1] and beginstations[j] != eindstations[j]:
            check = checker(beginstations, eindstations, stationlijst, j, i+start+1)
            check2 = checker2(beginstations, eindstations, stationlijst, i+start+1, j)
            if stationlijst[beginstations[i+start+1]-1][eindstations[i+start+1]-1] >= stationlijst[beginstations[i+start+1]-1][eindstations[j]-1] and stationlijst[beginstations[j]-1][eindstations[j]-1] >= stationlijst[beginstations[j]-1][eindstations[i+start+1]-1]:
                if check <= stationlijst[beginstations[i+start+1]-1][eindstations[i+start+1]-1] - stationlijst[beginstations[i+start+1]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i+start+1]-1] and check2 <= stationlijst[beginstations[i+start+1]-1][eindstations[i+start+1]-1] - stationlijst[beginstations[i+start+1]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i+start+1]-1]:
                    return stationlijst[beginstations[i+start+1]-1][eindstations[i+start+1]-1] - stationlijst[beginstations[i+start+1]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i+start+1]-1]
    else: return 0
    

aantal = int(input())
counter = 1

for i in range(aantal):

    aantal_stations = int(input())
    stationlijst = []
    for j in range(aantal_stations):
        stationlijst.append([int(x) for x in input().split()])

    aantal_users = int(input())

    besparing = 0

    beginstations = [int(x) for x in input().split()]
    eindstations = [int(x) for x in input().split()]

    while True:
        flag = True

        for i in range(len(beginstations)):
            if not flag:
                break
            for j in range(len(eindstations)):
                if i != j and eindstations[j] != eindstations[i] and beginstations[i] != eindstations[i] and beginstations[j] != eindstations[j]:
                    check = checker(beginstations, eindstations, stationlijst, j, i)
                    check2 = checker2(beginstations, eindstations, stationlijst, i, j)
                    if stationlijst[beginstations[i]-1][eindstations[i]-1] >= stationlijst[beginstations[i]-1][eindstations[j]-1] and stationlijst[beginstations[j]-1][eindstations[j]-1] >= stationlijst[beginstations[j]-1][eindstations[i]-1]:
                        if  check <= stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i]-1] and check2 <= stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i]-1]:
                            besparing += stationlijst[beginstations[i]-1][eindstations[i]-1] - stationlijst[beginstations[i]-1][eindstations[j]-1] + stationlijst[beginstations[j]-1][eindstations[j]-1] - stationlijst[beginstations[j]-1][eindstations[i]-1]
                            beginstations.pop(i)
                            eindstations.pop(i)
                            if j < i:
                                beginstations.pop(j)
                                eindstations.pop(j)    
                            else:
                                beginstations.pop(j-1)
                                eindstations.pop(j-1)  

                            flag = False 
                            break

        if flag:
            break

    print(f"{counter} {besparing}")

    counter += 1


