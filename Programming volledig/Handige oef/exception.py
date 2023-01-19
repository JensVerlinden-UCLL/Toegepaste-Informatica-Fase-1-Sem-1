bestandsnaam = input()

try:
    assert "." in bestandsnaam and len(bestandsnaam) > 2, f'{bestandsnaam}'

    fp = open(bestandsnaam, "r")

    buffer = fp.read()

    fp.close

    print(buffer)


except AssertionError as aserr:
    print("De bestandsnaam voldoet niet aan de voorwaarden!", aserr)

except FileNotFoundError as fnferr:
    print("Er bestaat geen bestand met dit pad!", fnferr)

        