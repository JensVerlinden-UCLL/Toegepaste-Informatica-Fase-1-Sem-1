# https://dodona.ugent.be/nl/courses/1286/series/14344/activities/385064229

uur = 14
bijkomendeUren = 535 % 24
nieuwUur = uur + bijkomendeUren
if nieuwUur > 24:
    nieuwUur -= 24
nieuwUur = str(nieuwUur)
print(nieuwUur + ":00")
