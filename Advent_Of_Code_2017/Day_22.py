from Day_0 import *
from collections import defaultdict

CLEAN, WEAKENED, INFECTED, FLAGGED = '.', 'W', '#', 'F'

def load_grid():
    grid = defaultdict(lambda: '.')

    for (y, row) in enumerate(get_day_input(22).strip().split('\n')):
        for (x, col) in enumerate(row):
            grid[(x - (len(row) // 2) + -1j * (y - (len(row) // 2))) ] = col 

    return grid 

facing, pos, infected, grid = N, ORIGIN, 0, load_grid()

for i in range(10000):
    if grid[pos] == CLEAN:
        facing = turn_left(facing)
        grid[pos] = INFECTED; infected += 1
    elif grid[pos] == INFECTED:
        facing = turn_right(facing)
        grid[pos] = CLEAN

    pos += facing

print(f'Day 22-1: {infected}') # 5399

facing, pos, infected, grid = N, ORIGIN, 0, load_grid()

for i in range(10000000):
    if grid[pos] == CLEAN:
        facing = turn_left(facing) 
        grid[pos] = WEAKENED
    elif grid[pos] == WEAKENED:
        # continue straight
        grid[pos] = INFECTED; infected += 1
    elif grid[pos] == INFECTED:
        facing = turn_right(facing)
        grid[pos] = FLAGGED
    elif grid[pos] == FLAGGED:
        facing = turn_around(facing)
        grid[pos] = CLEAN

    pos += facing

print(f'Day 22-2: {infected}') # 2511776
