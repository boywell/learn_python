import curses
from random import randrange,choice
from collections import defaultdict

actions = ["up","down","left","right","reStart","exit"]
letter_code = [ord[ch] for ch in 'wasdrqWASDRQ']
print(letter_code)