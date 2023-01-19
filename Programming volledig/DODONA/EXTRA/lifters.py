# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1432498809

n = int(input())
maxscore = 0

for i in range(n//2):
    score = float(input())
    maxscore = max(score, maxscore)

for i in range(n - n//2):
    score = float(input())
    if score > maxscore:
        break
print(score)

