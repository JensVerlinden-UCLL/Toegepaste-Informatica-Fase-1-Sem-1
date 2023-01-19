# https://dodona.ugent.be/nl/courses/1286/series/14361/activities/2096226599


class BankRekening:

    def __init__(self, naam, nummer, bedrag = 0):

        self.naam = naam
        self.nummer = nummer
        self.bedrag = bedrag

    def __str__(self):
        return f"{self.naam}, {self.nummer}, bedrag: {self.bedrag}"

    def __repr__(self):
        return f"BankRekening('{self.naam}', '{self.nummer}', {self.bedrag})"

    def storten(self, plus):

        self.bedrag += plus
        

    def afhalen(self, min):

        self.bedrag -= min
        

        


