# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/924978922

isbn = input()

while isbn != 'stop':
    x10 = (int(isbn[0]) + 2*int(isbn[1]) + 3*int(isbn[2]) + 4*int(isbn[3]) + 5*int(isbn[4]) + 6*int(isbn[5]) + 7*int(isbn[6]) + 8*int(isbn[7]) + 9*int(isbn[8])) % 11
    if x10 == 10:
        x10 = 'X'
    x10 = str(x10)
    if x10 == isbn[9]:
        print("OK")
    else: print("FOUT")
    isbn = input()
    
