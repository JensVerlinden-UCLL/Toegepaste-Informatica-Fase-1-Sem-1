# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/1246292246

rotate_count= int(input("n: "))

ch = ord("A")

while ch <= ord("Z"):

    print(chr(ch), end="")
    ch +=1

print()

for i in range(26):
    rotation = (i + rotate_count) % 26
    print(chr(ord("A") + rotation), end="")
print()