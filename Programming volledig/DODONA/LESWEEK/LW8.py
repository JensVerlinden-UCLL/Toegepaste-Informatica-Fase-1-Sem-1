
# from copy import copy

# class Persoon:

#     def __init__(self, fnaam, fvoornaam, fmail):
#         self.naam = fnaam
#         self.voornaam = fvoornaam
#         self.mail = fmail

#     def __str__(self):
#         return f"Deze persoon heet {self.naam} {self.voornaam} en heeft het e-mailadres {self.mail}."

#     def __eq__(self, other):
        
#         if isinstance(other, self.__class__):
#             return self.mail == other.mail

#         else: return False

# class Adres:

#     def __init__(self, fstraat, fnummer, fgemeente):
#         self.straat = fstraat
#         self.nummer = fnummer
#         self.gemeente = fgemeente

#     def __str__(self):
#         return f"Dit adres is gelegen op {self.straat} {self.nummer} in de gemeente {self.gemeente}."

#     def __eq__(self, other):
        
#         if isinstance(other, self.__class__):
#             return self.straat == other.straat and self.nummer == other.nummer and self.gemeente==other.gemeente

#         else: return False

# class Huis: 

#     def __init__(self, fpersoon, fadres):

#         assert isinstance(fpersoon, Persoon) and isinstance(fadres, Adres), "Dit zijn ongeldige objecten"

#         self.persoon = copy(fpersoon)
#         self.adres = copy(fadres)

#     def __str__(self):
#         return f"Dit huis is gelegen op {self.adres.straat} {self.adres.nummer} in de gemeente {self.adres.gemeente} en is beheerd door {self.persoon.naam} {self.persoon.voornaam} met de e-mail {self.persoon.mail}."

#     def __eq__(self, other):
        
#         if isinstance(other, self.__class__):
#             return self.persoon == other.persoon and self.adres == other.adres

#         else: return False


# jos = Persoon("Verboven", "Jos", "swaffelmanneke3000@outlook.com")
# jef = Persoon("Verbeneden", "Jef", "swoeffelvrouwke5@outlook.com")
# jos_adres = Adres("Kerkstraat", "69", "Haamond-Achelt")
# jef_adres = Adres("Torenstraat", "420", "Groot-Zandhoven")
# jos_huis = Huis(jos, jos_adres)
# jef_huis = Huis(jef, jef_adres)

# print(jos_huis.__str__())
# print(jef_huis)

def letterindex(totaal, letter):

    if totaal[0] == letter:

        return 0

    else:
        return 1 + letterindex(totaal[1:], letter)

print(letterindex("abcdefg", "e"))


    