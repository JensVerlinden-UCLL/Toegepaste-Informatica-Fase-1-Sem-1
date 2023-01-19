# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1092659960

def hanoi_berekening(n, p_van="A", p_tmp = "B", p_naar="C"):
        if n == 1:
            print( "Schijf 1 van", p_van, "naar", p_naar )
            return 1        
        stappen = hanoi_berekening(n-1, p_van, p_naar, p_tmp)
        print( "Schijf", n, "van", p_van, "naar", p_naar )
        stappen += 1+hanoi_berekening( n-1 , p_tmp, p_van, p_naar)
        return stappen

def hanoi(n):

    stappen = hanoi_berekening(n)
    print(f"{stappen} stappen gedaan")

hanoi(10)
    



