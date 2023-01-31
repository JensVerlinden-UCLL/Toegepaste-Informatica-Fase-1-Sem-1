from hashlib import sha1
import os

def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest() == 'd2eaf2aa1512d6596e0a5bae633537c6b8e779a3'
