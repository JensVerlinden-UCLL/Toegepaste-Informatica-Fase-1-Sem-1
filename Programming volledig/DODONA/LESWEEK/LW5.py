'''
def calc_sum_two_integers(n1, n2):
    if n1 >= 5 and n2 >= 5:
        z = n1 * n2
    else: z = n1 / n2

    return z
        
    
nummer1 =int(input("Getal 1: "))
nummer2 =int(input("Getal 2: "))
print(calc_sum_two_integers(nummer1, nummer2))
'''

def veelvoud_van_drie(a):
    if a % 3 == 0:
        return True
    else: return False

def veelvoud_van_drie_alt(a):
    if veelvoud_van_drie(a):
        return "veelvoud"
    else: return "geen veelvoud"

getal = int(input("Geef een getal: "))
print(veelvoud_van_drie_alt(getal))