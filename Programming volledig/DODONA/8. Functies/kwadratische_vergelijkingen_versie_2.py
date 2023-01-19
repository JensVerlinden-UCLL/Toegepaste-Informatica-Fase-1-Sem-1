# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/446763531

from math import sqrt

def discriminant(a, b, c):
    discriminantus = float(b**2 - 4*a*c)
    return round(discriminantus, 1)

def oplossingen(a, b, c):
    if a == 0:
        if b == 0:
            return (0, 0, 0)
        else: 
            x1 = -c/b
            return (1, x1, 0)
    else:
        if discriminant(a, b, c) > 0:
            dis = sqrt(discriminant(a, b, c))
            x1 = (-b - dis ) / (2*a)
            x2 = (-b + dis ) / (2*a)
            return (2, x1, x2)
        elif discriminant(a, b, c) == 0:
            x1= -b/(2*a)
            return (1, x1, 0)
        else: return (0, 0, 0)



