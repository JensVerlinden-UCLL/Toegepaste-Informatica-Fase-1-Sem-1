# https://dodona.ugent.be/nl/courses/1286/series/14345/activities/819600301
aantalStapels = int(input("Hoeveel stapels: "))
gewichtGoud = int(input("Gewicht echt goudstuk: "))
gewichtWeegstrategie= int(input("Gewicht weegstrategie: "))
aantalValseMunten = abs(int(gewichtGoud * (aantalStapels*(aantalStapels + 1)/2) - gewichtWeegstrategie))
print(aantalValseMunten)

