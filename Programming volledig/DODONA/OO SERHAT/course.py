class Vak:
    def __init__(self,gegeven_code,gegeven_naam, gegeven_aantal_studiepunten):
        assert len(gegeven_code) == 6, "aantal tekens van de code van een vak moet 6 zijn"
        self.code = gegeven_code
        self.naam = gegeven_naam
        self.aantal_studiepunten = gegeven_aantal_studiepunten
        
if __name__ == '__main__':
    def trying():
        try:
            programming1 = Vak("MBI02H36","Programming 1",6)
    
        except AssertionError as e:
            raise
    
        print("Hallokes")
    
    try:
        trying()
    except AssertionError as a:
        print(a.args)
    finally:
        print('hallokes')
