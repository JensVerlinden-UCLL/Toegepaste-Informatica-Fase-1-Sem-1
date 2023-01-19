# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/2038783829



def iszigzag(lijst):
    zigzag = True
    for i  in range(len(lijst)):
        if i%2 == 0:
            if i == 0:
                if lijst[i] < lijst[i+1]:
                    zigzag = False
                    break
            elif i == len(lijst) - 1:
                if lijst[i] < lijst[i-1]:
                    zigzag = False
                    break
            else: 
                if lijst[i] < lijst[i-1] or lijst[i] < lijst[i+1]:
                    zigzag = False
                    break
    return zigzag

def zigzag_traag(lijst):

    lijst.sort()
    
    for i  in range(len(lijst)):
        if i%2 == 0:
            if i == len(lijst) - 1:
                break
            elif lijst[i] < lijst[i+1]:
                lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
                
    

def zigzag_snel(lijst):
    for i  in range(len(lijst)):
        if i%2 == 0:
            if i == 0:
                if lijst[i] < lijst[i+1]:
                    lijst[i], lijst[i+1] = lijst[i+1], lijst[i]
            elif i == len(lijst) - 1:
                if lijst[i] < lijst[i-1]:
                    lijst[i], lijst[i-1] = lijst[i-1], lijst[i]
            else:                 
                if lijst[i] < lijst[i-1]:
                    lijst[i], lijst[i-1] = lijst[i-1], lijst[i]
                if lijst[i] < lijst[i+1]:
                    lijst[i], lijst[i+1] = lijst[i+1], lijst[i]

