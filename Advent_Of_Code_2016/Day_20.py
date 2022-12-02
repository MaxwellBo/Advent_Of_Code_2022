# http://adventofcode.com/2016/day/20

from itertools import *

class Range(object):
    def __init__(self, lower, upper):
        self.upper = upper
        self.lower = lower
        self.alive = True

    def __contains__(self, item):
        return self.lower - 1 <= item <= self.upper + 1

def merge(a, b):
    if a.alive and b.alive:
        xs = (a.lower in b, a.upper in b, b.lower in a, b.upper in a)

        if xs == (0, 0, 1, 1):
            b.alive = False
        elif xs == (1, 1, 0, 0):
            a.alive = False
        elif xs == (0, 1, 1, 0):
            a.upper = b.upper
            b.alive = False
        elif xs == (1, 0, 0, 1):
            b.upper = a.upper
            a.alive = False

def main():
    with open("inputs/Day_20_input.txt") as fp:

        ranges = []
        for line in fp:
            lower, upper = line.split('-')
            ranges.append(Range(int(lower), int(upper)))

        # Needs at least 3 iterations to cull all overlaps
        for i in range(1, 5):
            for a, b in combinations(ranges, 2):
                merge(a, b)

            ranges = [ i for i in ranges if i.alive ]

        ranges.sort(key=lambda x: x.lower)


        print("Part 1:", ranges[0].upper + 1) # 22887907

        p2 = sum(ranges[i + 1].lower - ranges[i].upper - 1\
                 for i in range(len(ranges) - 1))

        print("Part 2:", p2) # 109

if __name__ == '__main__':
    main()