# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1515270930

# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1515270930

def fib(n, diepte):
    inspringing = diepte * 2 * " "
    print(f"{inspringing}fib({n}, {diepte})")
    diepte += 1
    
    if n <= 0:
        print(f"{inspringing}return 0")
        return 0
        
    elif n == 1:
        print(f"{inspringing}return 1")
        return 1
    
    else: 
        waarde = fib(n-1, diepte) + fib(n-2, diepte) 
        print(f"{inspringing}return {waarde}")
        return waarde

print(fib(5, 0))