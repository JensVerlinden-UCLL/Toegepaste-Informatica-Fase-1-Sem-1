# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1294363212

# https://dodona.ugent.be/nl/courses/1286/series/14352/activities/1294363212

def vlag(richting, kleuren):
    print_result = ''
    if richting == 'verticaal':
        for i in range(len(kleuren)):
            if i == len(kleuren) - 1:
                print_result += f"{kleuren[i]}"
            else:
                print_result += f"{kleuren[i]} | "
        
    elif richting == 'horizontaal':
        for i in range(len(kleuren)):
            if i == len(kleuren) - 1:
                print_result += f"{kleuren[i]}"
            else:
                print_result += f"{kleuren[i]}\n-\n"

    return print_result
            


    



    
