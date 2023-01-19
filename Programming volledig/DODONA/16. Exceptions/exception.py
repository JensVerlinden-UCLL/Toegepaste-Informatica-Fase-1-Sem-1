

bestandsnaam = input()

try:
    assert "." in bestandsnaam and len(bestandsnaam) > 2, f"De bestandsnaam voldoet niet aan de voorwaarden!: {bestandsnaam}"

    fp = open(bestandsnaam, "r")

    buffer = fp.read()

    fp.close

    print(buffer)


except AssertionError as aserr:
    print(aserr)
except FileNotFoundError as fnferr:
    print("Er bestaat geen bestand met dit pad!", fnferr)

        