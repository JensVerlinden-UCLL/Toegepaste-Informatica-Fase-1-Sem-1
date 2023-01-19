# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/576540834

def vraag_input( prompt ):
    while True:
        waarde = input(prompt)
        for letter in waarde:
            if letter < 'a' or letter > 'z':
                print( "Ongeldig antwoord!")
                break
        else: return waarde
        

    

s = vraag_input( "Geef een string van kleine letters: " )
print( "Je gaf in:", s )

