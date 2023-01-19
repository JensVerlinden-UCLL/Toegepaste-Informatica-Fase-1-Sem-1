# https://dodona.ugent.be/nl/courses/1751/series/19304/activities/1033159532

lijn1 = input().replace(" ", "")
lijn2 = input().replace(" ", "")
lijn3 = input().replace(" ", "")
counter = 1
aantal = int(input())

A = lijn1[0:2] + lijn2[0:2] + lijn3[0:2]
B = lijn1[2:4] + lijn2[2:4] + lijn3[2:4]
C = lijn1[4:6] + lijn2[4:6] + lijn3[4:6]
D = lijn1[6:8] + lijn2[6:8] + lijn3[6:8]
E = lijn1[8:10] + lijn2[8:10] + lijn3[8:10]
F = lijn1[10:12] + lijn2[10:12] + lijn3[10:12]
G = lijn1[12:14] + lijn2[12:14] + lijn3[12:14]
H = lijn1[14:16] + lijn2[14:16] + lijn3[14:16]
I = lijn1[16:18] + lijn2[16:18] + lijn3[16:18]
J = lijn1[18:20] + lijn2[18:20] + lijn3[18:20]
K = lijn1[20:22] + lijn2[20:22] + lijn3[20:22]
L = lijn1[22:24] + lijn2[22:24] + lijn3[22:24]
M = lijn1[24:26] + lijn2[24:26] + lijn3[24:26]
N = lijn1[26:28] + lijn2[26:28] + lijn3[26:28]
O = lijn1[28:30] + lijn2[28:30] + lijn3[28:30]
P = lijn1[30:32] + lijn2[30:32] + lijn3[30:32]
Q = lijn1[32:34] + lijn2[32:34] + lijn3[32:34]
R = lijn1[34:36] + lijn2[34:36] + lijn3[34:36]
S = lijn1[36:38] + lijn2[36:38] + lijn3[36:38]
T = lijn1[38:40] + lijn2[38:40] + lijn3[38:40]
U = lijn1[40:42] + lijn2[40:42] + lijn3[40:42]
V = lijn1[42:44] + lijn2[42:44] + lijn3[42:44]
W = lijn1[44:46] + lijn2[44:46] + lijn3[44:46]
X = lijn1[46:48] + lijn2[46:48] + lijn3[46:48]
Y = lijn1[48:50] + lijn2[48:50] + lijn3[48:50]
Z = lijn1[50:52] + lijn2[50:52] + lijn3[50:52]

for i in range(aantal):
    letters = []
    for i in range(3):
        letters.append([x for x in input().replace(" ", "")])
    teller = 0
    zin = ''
    for i in range(len(letters[0]) // 2):
        woord = letters[0][(teller*2):(teller*2+2)] + letters[1][(teller*2):(teller*2+2)] +letters[2][(teller*2):(teller*2+2)]
        teller += 1
        woord = ''.join(woord)

        if woord == A:
            zin += 'A'

        elif woord == B:
            zin += 'B'

        elif woord == C:
            zin += 'C' 

        elif woord == D:
            zin += 'D'            

        elif woord == E:
            zin += 'E' 
        
        elif woord == F:
            zin += 'F' 

        elif woord == G:
            zin += 'G' 

        elif woord == H:
            zin += 'H' 

        elif woord == I:
            zin += 'I' 

        elif woord == J:
            zin += 'J' 

        elif woord == K:
            zin += 'K' 

        elif woord == L:
            zin += 'L' 

        elif woord == M:
            zin += 'M' 

        elif woord == N:
            zin += 'N' 

        elif woord == O:
            zin += 'O' 

        elif woord == P:
            zin += 'P' 

        elif woord == Q:
            zin += 'Q' 

        elif woord == R:
            zin += 'R' 

        elif woord == S:
            zin += 'S' 

        elif woord == T:
            zin += 'T' 

        elif woord == U:
            zin += 'U' 

        elif woord == V:
            zin += 'V' 

        elif woord == W:
            zin += 'W' 

        elif woord == X:
            zin += 'X' 

        elif woord == Y:
            zin += 'Y' 

        elif woord == Z:
            zin += 'Z' 

    print(f"{counter} {zin}")

    counter += 1




    
