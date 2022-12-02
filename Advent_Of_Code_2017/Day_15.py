A_START, B_START = 699, 124
A_FACTOR, B_FACTOR = 16807, 48271
A_MULTIPLE, B_MULTIPLE = 4, 8 
DIVISOR = 2147483647
from Day_0 import *

def gen(nxt, factor, multiple=None):
    while True:
        if not multiple or nxt % multiple == 0:
            yield nxt

        nxt = (nxt * factor) % DIVISOR

a, am = gen(A_START, A_FACTOR), gen(A_START, A_FACTOR, A_MULTIPLE)
b, bm = gen(B_START, B_FACTOR), gen(B_START, B_FACTOR, B_MULTIPLE)

print(f"Part 15-1: {quantify(lambda _: next(a) & 65535 == next(b) & 65535, range(40000000))}") # 600
print(f"Part 15-2: {quantify(lambda _: next(am) & 65535 == next(bm) & 65535, range(5000000))}") # 313