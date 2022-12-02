import cmath
import math
from itertools   import (permutations, combinations, chain, cycle, product, islice, 
                         takewhile, zip_longest, count as count_from)
from statistics  import mean, median, mode, stdev, variance

# Shamelessly lifted from 
# https://render.githubusercontent.com/view/ipynb?commit=3ccf589fd11ed27d204d38f46fd1c736e78d5899&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6e6f727669672f707974756465732f336363663538396664313165643237643230346433386634366664316337333665373864353839392f6970796e622f416476656e74253230323031372e6970796e62&nwo=norvig%2Fpytudes&path=ipynb%2FAdvent+2017.ipynb&repository_id=83516498&repository_type=Repository#Day-0:-Imports-and-Utility-Functions
LETTERS  = 'abcdefghijklmnopqrstuvwxyz'

cat = ''.join

inf = float('inf')
BIG = 10 ** 999

################ Functions for Input, Parsing

def get_day_input(number):
    file = open('inputs/day_{number}.txt'.format(number=number), 'r')
    text = file.read()
    file.close()
    return text

def get_day_input_split(number):
    return get_day_input(number).split('\n')

################ Functions on Iterables

def head(iterable, default=None): 
    "The first item in an iterable, or default if it is empty."
    return next(iter(iterable), default)

def nth(iterable, n, default=None):
    "Returns the nth item of iterable, or a default value"
    return next(islice(iterable, n, None), default)


def for_each(f, iterable):
    list(map(f, iterable))
    return None

def length(iterable):
    "Same as len(list(iterable)), but without consuming memory."
    return sum(1 for _ in iterable)

def quantify(f, iterable):
    "Count how many times the predicate is true."
    return sum(map(f, iterable))

flatten = chain.from_iterable

################ Functional programming

def const(value): return (lambda *args: value)

def iterate(f, x, *args, **kwds):
    "Yield x, f(x), f(f(x)), ..."
    yield x
    while True:
        x = f(arg, *args, **kwds)
        yield x

def iterate_n(n, f, x, *args, **kwds):
    "Repeat x = f(x) n times, return x."
    return nth(repeatedly(f, x, *args, **kwds), n)

################ Math Functions

def transpose(lst):
    return map(list, zip(*lst))

def multiply(numbers):
    "Multiply all the numbers together."
    result = 1
    for n in numbers:
        result *= n
    return result

import operator as op

TOKEN_TO_OPERATION = {'>': op.gt, '>=': op.ge, '==': op.eq,
                      '<': op.lt, '<=': op.le, '!=': op.ne,
                      '+': op.add, '-': op.sub, '*': op.mul, 
                      '/': op.truediv, '**': op.pow}

################ 2-D points implemented using complex numbers

ORIGIN = 0 + 0j
NEIGHBOURS_4 = SIDES = N, S, E, W = 1j, -1j, 1, -1
DIAGONALS = NE, SE, SW, NW = (N + E), (S + E), (S + W), (N + W)
NEIGHBOURS_8 = (*NEIGHBOURS_4, *DIAGONALS)

def get_neighbours_4(c): return [ c + i for i in NEIGHBOURS_4 ]
def get_neighbours_8(c): return [ c + i for i in NEIGHBOURS_8 ]

def turn_left(c): return c * 1j
def turn_right(c): return c * -1j
def turn_around(c): return c * -1

def cityblock_distance(c): return abs(c.real) + abs(c.imag)
