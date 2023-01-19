# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/854408577

# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/854408577

def ggd(g1, g2):

    kl, gr = min(g1, g2), max(g1, g2)

    if gr % kl == 0:
        return kl
    
    else:
        return ggd(kl, gr % kl)

