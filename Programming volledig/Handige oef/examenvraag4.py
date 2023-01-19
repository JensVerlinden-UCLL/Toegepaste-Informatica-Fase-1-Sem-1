
maand = int(input())
dag = int(input())

if maand in (1, 3, 5, 7, 8, 10) and dag == 31 or maand in (4, 6, 9, 11) and dag == 30 or maand == 2 and dag == 28:
    dag = 1
    maand += 1

elif maand == 12 and dag == 31:
    dag = 1
    maand = 1

else:
    dag += 1

print(maand)
print(dag)

