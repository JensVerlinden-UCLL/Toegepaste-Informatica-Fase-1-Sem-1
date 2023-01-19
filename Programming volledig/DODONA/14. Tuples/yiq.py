# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/2097740983

def yiq(tuple):
    y = (0.299*tuple[0] + 0.587*tuple[1] + 0.114*tuple[2])
    i = (0.596*tuple[0] - 0.274*tuple[1] - 0.322*tuple[2])
    q = (0.211*tuple[0] - 0.523*tuple[1] + 0.312*tuple[2])
    return (round(y, 4), round(i, 4), round(q, 4))
