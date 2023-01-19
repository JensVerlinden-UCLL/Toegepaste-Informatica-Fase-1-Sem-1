# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/1095693228

woord = input("Woord: ")

a_counter = 0
e_counter = 0
i_counter = 0 
o_counter = 0 
u_counter = 0

for i in range(len(woord)):

    if woord[i] == "A" or woord[i] == "a":
        a_counter += 1

    if woord[i] == "E" or woord[i] == "e":
        e_counter += 1

    if woord[i] == "I" or woord[i] == "i":
        i_counter += 1

    if woord[i] == "O" or woord[i] == "o":
        o_counter += 1

    if woord[i] == "U" or woord[i] == "u":
        u_counter += 1

print(f"A: {a_counter}\nE: {e_counter}\nI: {i_counter}\nO: {o_counter}\nU: {u_counter}")