from hashlib import sha1
import os

def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest() == '8f9a23874e34f927a3488c9340e3698e6b9f03b7'
