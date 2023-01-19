# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/101669433

def combisom(getallijst, getal):
    for i in getallijst:
        for j in getallijst:
            if i + j == getal and i != j:
                return True
    
    return False


