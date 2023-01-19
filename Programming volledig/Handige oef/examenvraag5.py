
totaalLijst = [int(x) for x in input().split()]

resultaatLijst = []

for i in range(1, len(totaalLijst) - 1):
    if totaalLijst[i] > totaalLijst[i - 1] and totaalLijst[i] > totaalLijst[i + 1]:
        resultaatLijst.append(i)

print(resultaatLijst)