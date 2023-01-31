from hashlib import sha1
import os

def check():
    assert os.path.exists('solution.txt')

    with open('solution.txt') as file:
        solution = file.read().strip().encode('utf-8')

    assert sha1(solution).hexdigest() == '80e4f6353b117b032d9ea4fabe58f43ad2809c9f'
