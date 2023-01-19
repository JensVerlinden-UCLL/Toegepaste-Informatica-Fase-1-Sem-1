# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1582865176

def nummer( getalvraag ):
    while True:
        x = int(input( getalvraag ))
        if x < 0 or x > 1000:
            print("Geef een nummer tussen 0 en 1000: ")
            continue
        break    
    return x
    

def main():
    while True:
        x = nummer("Nummer 1: ")
        if x == 0:
            break
        
        y = nummer("Nummer 2: ")
        if y == 0:
            break

        if x%y == 0 or y%x == 0:
            print( "Fout: de nummers mogen geen delers zijn" )
            return
        print( "Vermenigvuldiging van", x, "met", y, "geeft", x * y )

    print( "Tot ziens!" )
main()