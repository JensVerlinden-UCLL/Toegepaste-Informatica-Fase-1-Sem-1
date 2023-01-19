# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1325500143

samengestelde_lijst = []

def samenvoegen(lijst1, lijst2):
    samengestelde_lijst = []
    for i in range(min(len(lijst1), len(lijst2))):
        samengestelde_lijst.append(lijst1[i])
        samengestelde_lijst.append(lijst2[i])
    return samengestelde_lijst

def weven(lijst1, lijst2):
    samengestelde_lijst = []
    for i in range(max(len(lijst1), len(lijst2))):
        samengestelde_lijst.append(lijst1[i%len(lijst1)])         
        samengestelde_lijst.append(lijst2[i%len(lijst2)])
    return samengestelde_lijst

def ritsen(lijst1, lijst2):
    samengestelde_lijst = []
    for i in range(max(len(lijst1), len(lijst2))):
        if i < len(lijst1):
            samengestelde_lijst.append(lijst1[i])
        if i < len(lijst2):
            samengestelde_lijst.append(lijst2[i])
    return samengestelde_lijst

