# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1131866318


def waardering(bedrag1, bedrag2):
    berekening = ((bedrag1 / 4.07) - bedrag2) / bedrag2 * 100

    if berekening <= -25:
        return "sterk ondergewaardeerd"
    elif berekening <= -5:
        return "ondergewaardeerd"
    elif berekening <= 5:
        return "ongeveer gelijk"
    elif berekening <= 25:
        return "overgewaardeerd"
    else:
        return "sterk overgewaardeerd"

def wisselkoersanalyse(bedrag1, bedrag2):
    bedrag = float((bedrag1.split())[0])
    eenheid = " ".join(bedrag1.split()[1:])

    return f"De {eenheid} is {waardering(bedrag, bedrag2)} ten opzichte van de dollar."
