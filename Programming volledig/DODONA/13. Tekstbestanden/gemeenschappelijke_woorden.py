# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/744155174

def gemeenschappelijke_woorden(file1, file2, file3):

    fp = open( file1 , "r" )

    buffer1 = fp.read().lower()
    lijst1 = str(buffer1).split()

    fp.close

    ep = open( file2 , "r" )

    buffer2 = ep.read().lower()
    lijst2 = str(buffer2).split()

    ep.close()

    gp = open( file3 , "r" )

    buffer3 = gp.read().lower()
    lijst3 = str(buffer3).split()
    
    gp.close()

    new_list = []

    for i in lijst1:

        if i in lijst2 and i in lijst3:

            new_list.append(i)

    setlist = set(new_list)

    return setlist

    









    