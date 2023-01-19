# https://dodona.ugent.be/nl/courses/1286/series/14355/activities/1204583816

alles = {'Socrates', 'Plato', 'Eratosthenes', 'Zeus', 'Hera', 'Athene', 'Acropolis', 'Kat', 'Hond'}
mensen = {'Socrates', 'Plato', 'Eratosthenes'}
sterfelijken = {'Socrates', 'Plato', 'Eratosthenes', 'Kat', 'Hond'}

A = mensen.issubset(sterfelijken)
C = 'Socrates' in mensen
B = 'Socrates' in sterfelijken
D = len(sterfelijken - mensen) > 0
E =  len(alles - sterfelijken) > 0

