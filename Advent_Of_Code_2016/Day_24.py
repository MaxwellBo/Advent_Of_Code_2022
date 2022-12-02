# http://adventofcode.com/2016/day/24

import networkx as nx
import numpy as np
from itertools import *

def main(part):
    with open("inputs/Day_24_input.txt") as fp:

        # ------ Read the input ----- #
        m = [ i.strip() for i in fp ]

        rows = len(m)
        cols = len(m[0])
        pois_to_node = {}

        g = nx.grid_2d_graph(m=cols, n=rows)

        for y in range(rows):
            for x in range(cols):
                if m[y][x] == '#':
                    g.remove_node((x, y))
                elif m[y][x].isdigit():
                    pois_to_node[int(m[y][x])] = (x, y)

        # ------ Build datastructures ----- #
        pois = len(pois_to_node)

        adjacency = np.zeros((pois, pois))

        for (start_name, start_pos) in pois_to_node.items():
            for (finish_name, finish_pos) in pois_to_node.items():
                weight = nx.astar_path_length(g, start_pos, finish_pos)
                adjacency[start_name][finish_name] = weight

        # ------ Solve ----- #
        if part == 1:
            paths = [ (0, *i) for i in permutations(range(1, pois)) ]
        else:
            paths = [ (0, *i, 0) for i in permutations(range(1, pois)) ]

        def length(xs):
            return sum(adjacency[xs[i]][xs[i + 1]] for i in range(len(xs) - 1))

        print(f"Part {part}:", min(map(length, paths)))

if __name__ == '__main__':
    main(part=1) # 490
    main(part=2) # 744
