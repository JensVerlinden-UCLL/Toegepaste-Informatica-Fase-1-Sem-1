import re


def check():
    with open('solution.txt') as file:
        regex = file.read()

    positive_cases = [
        f'{str(d).rjust(2, "0")}/{str(m).rjust(2, "0")}/{str(y).rjust(4, "0")}'
        for d in range(0, 100, 7)
        for m in range(0, 100, 3)
        for y in range(0, 10000, 176)
    ]

    negative_cases = [
        '',
        '1/01/2000',
        '111/01/2000',
        '01/1/2000',
        '01/111/2000',
        '01/01/1',
        '01/01/12',
        '01/01/123',
        '01/01/12345',
        '1/1/2000',
    ]

    assert all(re.fullmatch(regex, s) for s in positive_cases)
    assert not any(re.fullmatch(regex, s) for s in negative_cases)
