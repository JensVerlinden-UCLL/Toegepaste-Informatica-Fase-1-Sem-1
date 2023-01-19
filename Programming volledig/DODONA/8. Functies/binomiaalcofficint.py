# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/33489040

def faculteit(n):
    facultus = 1
    for i in range(1,n+1):
        facultus *= i
    return facultus
    
def binomiaal(a, b):
    if a < b or b < 0 :
        binomialus = 0
    else: 
        m = a - b
        binomialus = int(faculteit(a) / (faculteit(b) * faculteit(m)))
    return binomialus

print(faculteit(-5))

