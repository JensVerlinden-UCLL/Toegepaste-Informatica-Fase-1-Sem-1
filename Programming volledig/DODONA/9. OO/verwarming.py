# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/1745983456

class Verwarming:

    def __init__(self, naam, temperatuur = 10.0, minimum = 0.0, maximum = 100.0):

        self.naam  = naam
        self.temp = temperatuur
        self.mintemp = minimum
        self.maxtemp = maximum

    def __str__(self):        
        return f"{self.naam}: huidige temperatuur: {self.temp:.1f}; toegelaten min: {self.mintemp:.1f}; toegelaten max: {self.maxtemp:.1f}" 

    def __repr__(self):
        return f"Verwarming('{self.naam}', {self.temp:.1f}, {self.mintemp:.1f}, {self.maxtemp:.1f})"

    def wijzig_temperatuur(self, wijziging):
        self.temp += wijziging

        if self.temp < self.mintemp:
            self.temp = self.mintemp
        
        if self.temp > self.maxtemp:
            self.temp = self.maxtemp

    def temperatuur(self):

        return float(self.temp)

toestel1 = Verwarming('radiator keuken', temperatuur=20)


        

