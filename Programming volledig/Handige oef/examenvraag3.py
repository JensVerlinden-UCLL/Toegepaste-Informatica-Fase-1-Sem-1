lijst = ["DOG", "ALLIGATOR", "SAMMY"]

unieklijst = []

dubbellijst =  set()

for i in lijst:
    for j in range(len(i)):
        if i[j] in unieklijst:
            dubbellijst.add(i[j])

        else:
            unieklijst.append(i[j])

for i in dubbellijst:
    unieklijst.remove(i)

zin = ''

for i in range(len(unieklijst)):
            if i == len(unieklijst) - 1:
                zin += f"en {unieklijst[i]}"
            elif i == len(unieklijst) - 2:
                zin += f"{unieklijst[i]} "
            else:
                zin += f"{unieklijst[i]}, "
                
print(f"De lijst heeft op dit moment {len(unieklijst)} unieke letters, namelijk {zin}.")
