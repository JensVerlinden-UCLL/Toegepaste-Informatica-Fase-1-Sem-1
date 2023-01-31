from hashlib import sha1
import os

def check():
    assert os.path.exists('C:\Introductieproject\challenges\images\creators\04\solution.txt')

    with open('solution.txt') as file:
        solution = file.read().strip().lower().encode('utf-8')

    assert sha1(solution).hexdigest() == '23524be9dba14bc2f1975b37f95c3381771595c8'
