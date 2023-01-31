import string
import random
import re
import os


rnd = random.Random(4911)
chars = string.ascii_letters + string.digits + string.punctuation


def positive_case():
    triple = rnd.choice(chars) * 3
    prefix = rnd.choices(chars, k=rnd.randint(0, 10))
    suffix = rnd.choices(chars, k=rnd.randint(0, 10))
    return f'{prefix}{triple}{suffix}'


def negative_case():
    return ''.join(rnd.choices(chars, k=rnd.randint(2, 5)) for _ in range(rnd.randint(1, 10)))


def positive_cases():
    return (positive_case() for _ in range(100))


def negative_cases():
    return (negative_case() for _ in range(100))


def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        regex = file.read()

    positive_cases = [
        f'{prefix}{char * 3}{suffix}'
        for prefix in ['', 'abc', '178', '. .', '   ']
        for char in 'aX4.?'
        for suffix in ['', 'abc', '178', '. .', '   ']
    ]

    negative_cases = [
        '',
        'x',
        *(f'{x}{x}' for x in 'a1.?'),
        *(f'{x}{x}{y}{y}' for x in 'a1.?' for y in 'b6*'),
    ]

    assert all(re.fullmatch(regex, s) for s in positive_cases)
    assert not any(re.fullmatch(regex, s) for s in negative_cases)
