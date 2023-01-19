# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/1551924012

def zonder_klinkers(file1, file2):

    fp = open( file1 , "r" )

    nieuwe_tekst = ''

    buffer = fp.read()

    counter1 = len(buffer)

    for i in range(len(buffer)):

        if buffer[i].lower() == 'a' or buffer[i].lower() == 'e' or buffer[i].lower() == 'i' or buffer[i].lower() == 'o' or buffer[i].lower() == 'u':
            continue
        else:
            nieuwe_tekst += buffer[i]

    counter2 = len(nieuwe_tekst)

    fp.close()

    ep = open( file2 , "w" )

    ep.write(nieuwe_tekst)

    ep.close()

    return (counter1, counter2)