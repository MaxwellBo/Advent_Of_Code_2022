from Day_0 import *
from collections import defaultdict

INPUT = 347991

def distance(point): return abs(point.real) + abs(point.imag)

square, pos, found = 2, (1 + 0j), False

grid = defaultdict(int)
grid[(0 + 0j)], grid[(1 + 0j)] = 1, 1

def check_square(): 
    if square == INPUT: print(f"Day 3-1: {int(distance(pos))}"); exit(0) # 480

def neighbours_sum(): return sum(grid[pos + i] for i in [N, S, E, W, NE, SE, SW, NW])

def spread():
    global found
    grid[pos] = neighbours_sum()
    if grid[pos] > INPUT and not found: print(f"Day 3-2: {grid[pos]}"); found = True # 349975

for i in range(2, BIG, 2): # start at side length 3
    for _ in range(i - 1): pos += N; square += 1; spread(); check_square()
    for _ in range(i):     pos += W; square += 1; spread(); check_square()
    for _ in range(i):     pos += S; square += 1; spread(); check_square()
    for _ in range(i + 1): pos += E; square += 1; spread(); check_square()
