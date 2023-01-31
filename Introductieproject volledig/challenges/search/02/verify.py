from hashlib import sha1
import os

def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest() == '9cdda67ded3f25811728276cefa76b80913b4c54'
