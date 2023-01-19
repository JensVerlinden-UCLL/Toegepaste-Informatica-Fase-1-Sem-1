# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/761303597

hoeveelheid = int(input("Geef producthoeveelheid: "))
prijs = float(input("Geef productprijs: "))
barcodes = int(input("Geef aantal barcodes: "))
mijlen = int(input("Geef aantal mijlen: "))

totaalprijs = hoeveelheid * prijs
totaalmijlen = hoeveelheid // barcodes * mijlen

print(f"Phillips spendeerde ${totaalprijs} voor {totaalmijlen} frequent flyer mijlen.")

