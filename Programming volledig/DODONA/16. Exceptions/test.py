stringwaarde = input("Geef een string van 10 karakters: ")

try:
    if len(stringwaarde) > 10:
            raise Exception("De ingevoerde tekst bevat meer dan 10 tekens")
    elif len(stringwaarde) < 10:
            raise Exception("De ingevoerde tekst bevat minder dan 10 tekens")
except Exception as error:
    while len(stringwaarde) != 10:
        print(error)
        stringwaarde=input("De ingegeven string was ongeldig. Geef een string van 10 karakters: ")
print(stringwaarde)

# input_number=input("Geef een getal tussen 0 en 10: ")
# number = int(input_number)
# try:
#     if number <0 or number > 10:
#     raise Exception ("Het ingevoerde getal is kleiner dan 0 of groter dan 10.") 
# except:
#     input_number=input("Het ingegeven getal was ongeldig. Geef een getal tussen 0 en 10: ")
    
# print(input_number)