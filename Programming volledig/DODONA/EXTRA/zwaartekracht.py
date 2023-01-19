# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1370867069

gewicht = float(input("Geef je gewicht in (kg): "))
planeet = input("Op welk hemellichaam ben je? ")

if planeet == "de maan":    
    gewicht_planeet = gewicht * 0.166
    print(f"Op {planeet} weeg je {gewicht_planeet:.3f} kilogram.")
elif planeet == "Jupiter":
    gewicht_planeet = gewicht * 2.36
    print(f"Op {planeet} weeg je {gewicht_planeet:.3f} kilogram.")
elif planeet == "Mars":
    gewicht_planeet = gewicht * 0.37
    print(f"Op {planeet} weeg je {gewicht_planeet:.3f} kilogram.")
elif planeet == "Venus":
    gewicht_planeet = gewicht * 0.9
    print(f"Op {planeet} weeg je {gewicht_planeet:.2f} kilogram.")
elif planeet == "Neptunus":
    gewicht_planeet = gewicht * 1.12
    print(f"Op {planeet} weeg je {gewicht_planeet} kilogram.")
else:
    print("Ongeldige invoer!")


