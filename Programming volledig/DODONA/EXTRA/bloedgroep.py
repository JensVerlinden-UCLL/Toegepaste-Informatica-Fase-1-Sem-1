# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1235806490

allel1 = input()
allel2 = input()

if allel1 == allel2:
    print(f"De combinatie van de ABO allelen {allel1} en {allel2} resulteert in bloedgroep {allel1}.")
elif allel1 == "O" and allel2 != "O":
    print(f"De combinatie van de ABO allelen {allel1} en {allel2} resulteert in bloedgroep {allel2}.")
elif allel2 == "O" and allel1 != "O":
    print(f"De combinatie van de ABO allelen {allel1} en {allel2} resulteert in bloedgroep {allel1}.")
else: print(f"De combinatie van de ABO allelen {allel1} en {allel2} resulteert in bloedgroep AB.")
