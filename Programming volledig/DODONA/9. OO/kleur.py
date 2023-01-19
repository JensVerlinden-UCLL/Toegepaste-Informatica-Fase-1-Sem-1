# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/2045812829

class Kleur:

    def __init__(self,  comp1 = 0,  comp2 = 0,  comp3 = 0):

        if comp1 < 0:
            comp1 = 0
        elif comp1 > 255:
            comp1 = 255
        if comp2 < 0:
            comp2 = 0
        elif comp2 > 255:
            comp2 = 255
        if comp3 < 0:
            comp3 = 0
        elif comp3 > 255:
            comp3 = 255
        
        self.comp1 = comp1
        self.comp2 = comp2
        self.comp3 = comp3

    def __str__(self):
        return "(" + str(self.comp1) + ", " + str(self.comp2) + ", " + str(self.comp3) + ")"

    def invers(self):
        
        self.comp1_invers = 255 - self.comp1
        self.comp2_invers = 255 - self.comp2
        self.comp3_invers = 255 - self.comp3

        return Kleur(self.comp1_invers, self.comp2_invers, self.comp3_invers,)

    def grijswaarde(self):

        self.grijswaarde = int(0.3 * self.comp1 + 0.59 * self.comp2 + 0.11 * self.comp3)

        return Kleur(self.grijswaarde, self.grijswaarde, self.grijswaarde)
