# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/325222513

def gregory_leibnitz(n):
    som = 0
    for i in range(n):
        if i % 2 == 0:
            som = som + 1/(2*i+1)
        else:
             som = som - 1/(2*i+1)
    return(4*som)
