from hashlib import sha1
import os

def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        solution = file.read().encode('utf-8')

    assert sha1(solution).hexdigest() == 'ebfdec641529d4b59a54e18f8b0e9730f85939fb'
