# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1317066143
getal = int(input())
for i in range(getal, 0, -1):
    if i > 2:
        print(i, "flesjes met bier op de muur,", i, "flesjes met bier.")
        print("Open er een, drink hem meteen,", i-1, "flesjes met bier op de muur.")
    elif i == 2: 
        print(i, "flesjes met bier op de muur,", i, "flesjes met bier.")
        print("Open er een, drink hem meteen,", i-1, "flesje met bier op de muur.")
    else: 
        print(i, "flesje met bier op de muur,", i, "flesje met bier.")
        print("Open er een, drink hem meteen,", i-1, "flesjes met bier op de muur.")
    

