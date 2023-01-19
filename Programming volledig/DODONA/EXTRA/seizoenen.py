# https://dodona.ugent.be/nl/courses/1749/series/19292/activities/1800551125


dag = int(input())
maand = input()

if maand in ["januari", "februari"]:
    seizoen = "winter"
if maand in ["april", "mei"]:
    seizoen = "lente"
if maand in ["juli", "augustus"]:
    seizoen = "zomer"
if maand in ["oktober", "november"]:
    seizoen = "herfst"

if maand == 'maart':
    if dag < 21:
        seizoen = "winter"
    else: seizoen = "lente"

if maand == 'juni':
    if dag < 21:
        seizoen = "lente"
    else: seizoen = "zomer"

if maand == 'september':
    if dag < 23:
        seizoen = "zomer"
    else: seizoen = "herfst"

if maand == 'december':
    if dag < 21:
        seizoen = "herfst"
    else: seizoen = "winter"

print(f"Het is {seizoen} op {dag} {maand}.")
