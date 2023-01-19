
# class Boek:

#     def __init__(self, fauteur, ftitel, fuitgever, fpaginas, fISBN):
        
#         self.auteur= fauteur
#         self.titel = ftitel
#         self.uitgever = fuitgever
#         self.paginas = fpaginas
#         self.ISBN = fISBN

#     def __str__(self):
#         return f"Auteur: {self.auteur}, titel: {self.titel}, uitgever: {self.uitgever}, paginas: {self.paginas}, ISBN: {self.ISBN}"

#     def __eq__(self, other):

#         if isinstance(other, self.__class__):

#             return self.ISBN == other.ISBN 

# boek1 = Boek("Serhat Erdogan", "Python Book", "Standaard Uitgeverij", 13, 1234567)

# boek2 = Boek("Jef", "HTML book", "Standaard Uitgeverij", 32, 1234567)

# print(boek1 == boek2)




# n = int(input("Getal: "))
# faculteit = 1
# for i in range(n+1):
#     if i != 0:
#         faculteit *= i

# print(faculteit)



def faculteit(n):
    if n == 0:
        return 1
    else:
        return n * faculteit(n-1)

print(faculteit(5))