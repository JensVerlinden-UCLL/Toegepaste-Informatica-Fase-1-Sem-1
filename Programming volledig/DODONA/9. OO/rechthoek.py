# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/1773014461

from copy import copy

class Punt:
    def __init__( self, x=0, y=0 ):
        self.x = int(x)
        self.y = int(y)
    def __repr__(self):
        return f"Punt({self.x}, {self.y})"
    def __eq__(self, other):
        if not (isinstance(other, self.__class__)):
            return False
        else:
            return self.x == other.x and self.y == other.y
    

class Rechthoek:
    def __init__(self, punt, breedte, hoogte ):
        assert breedte > 0 and hoogte > 0, 'ongeldige rechthoek'
        self.punt = copy(punt)
        self.breedte = breedte
        self.hoogte = hoogte
    def __repr__(self):
        return f"Rechthoek({self.punt}, {self.breedte}, {self.hoogte})"
    def oppervlakte(self):
        oppervlakte = self.breedte * self.hoogte
        return oppervlakte
    def omtrek(self):
        omtrek = self.breedte * 2 + self.hoogte * 2
        return omtrek
    def rechtsonder(self):
        x_rechtsonder = self.punt.x + self.breedte
        y_rechtsonder = self.punt.y + self.hoogte
        return Punt(x_rechtsonder, y_rechtsonder)
    def overlap(self, r):
        r1, r2 = self, r
         
        if r1.punt.x > r2.punt.x:
            r1, r2 = r2, r1   

        if r1.rechtsonder().x <= r2.punt.x or r1.rechtsonder().y <= r2.punt.y or r2.rechtsonder().y <= r1.punt.y:
            return None

        y_overlap = max(r1.punt.y, r2.punt.y)

        return Rechthoek(Punt(r2.punt.x, max(r1.punt.y, r2.punt.y)), min(r1.rechtsonder().x - r2.punt.x, r2.breedte ), min( r2.rechtsonder().y - y_overlap, r1.rechtsonder().y - y_overlap))
        
    def __eq__(self, other):
        if not (isinstance(other, self.__class__)):
            return False
        else:
            return self.breedte == other.breedte and self.hoogte == other.hoogte and self.punt == other.punt
        
