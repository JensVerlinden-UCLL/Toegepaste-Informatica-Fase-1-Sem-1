# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/172219463

from random import shuffle

def kaartspel():

    boek = []

    for i in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"):

        for j in ("C", "D", "H", "S"):

            boek.append(i + j)

    shuffle(boek)

    return(boek)




