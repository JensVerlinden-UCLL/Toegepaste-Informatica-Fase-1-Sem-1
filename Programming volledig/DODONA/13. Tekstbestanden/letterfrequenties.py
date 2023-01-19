# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/14378608

from string import ascii_lowercase

def lettertellen(file, letter):
   
    fp = open( file , "r" )

    buffer = fp.read().lower()

    length = 0

    for i in range(len(buffer)):

        if buffer[i] in ascii_lowercase:

            length += 1

    counter = 0

    for i in range(len(buffer)):

        if buffer[i] == letter:

            counter += 1
    
    ratio = counter/length

    return f"{ratio:.5f}"

def letterfrequenties(file1, file2, file3, file4):

    fp = open( file4 , "w" )

    for j in ascii_lowercase:

        frequentie1 = lettertellen(file1, j)
        frequentie2 = lettertellen(file2, j)
        frequentie3 = lettertellen(file3, j)

        fp.write(f'{j},{frequentie1},{frequentie2},{frequentie3}' + '\n')

        

