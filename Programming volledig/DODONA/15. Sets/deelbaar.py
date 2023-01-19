# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/200735652

deelbaar_door_3 = set([3*x for x in range(1, 1000//3 + 1)])
deelbaar_door_7 = set([7*x for x in range(1, 1000//7 + 1)])
deelbaar_door_11 = set([11*x for x in range(1, 1000//11 + 1)])

A = deelbaar_door_3 & deelbaar_door_7 & deelbaar_door_11
B = deelbaar_door_3 & deelbaar_door_7 - deelbaar_door_11
C = set([x for x in range(1, 1001)]) - deelbaar_door_3 - deelbaar_door_7 -deelbaar_door_11
