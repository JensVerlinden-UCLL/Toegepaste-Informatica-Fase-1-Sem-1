# https://dodona.ugent.be/nl/courses/1286/series/14358/activities/2128064180
try: 
    numlist = [ 100, 101, 0, "103", 104 ]

    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )

except ZeroDivisionError:
    print("Fout: Wie deelt door 0 is echt nen dikke loser")

except ValueError:
    print("Fout: Je gaf geen integer in")

except IndexError:
    print("Fout: Deze index ligt buiten de lijst")

except TypeError:
    print("Fout: Dit datatype wordt niet ondersteund bij de berekening")
