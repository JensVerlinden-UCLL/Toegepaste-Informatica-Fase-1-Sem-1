# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1647887074


play1 = input()
play2 = input()

if play1 == play2:
    print("gelijkspel")

elif play1 == "schaar" and play2 in ("blad", "hagedis") or play1 == "blad" and play2 in ("Spock", "steen") or play1 == "steen" and play2 in ("schaar", "hagedis") or play1 == "hagedis" and play2 in ("Spock", "blad") or play1 == "Spock" and play2 in ("schaar", "steen"):
    print("speler1 wint")

else:
    print("speler2 wint")