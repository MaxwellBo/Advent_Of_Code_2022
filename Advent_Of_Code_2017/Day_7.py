from Day_0 import get_day_input
from collections import namedtuple
import networkx as nx

def parse_program(atoms: str): return Program(name=atoms[0], weight=int(atoms[1][1:-1]), 
    holding=(tuple([]) if len(atoms) == 2 else tuple([ i.strip(',') for i in atoms[3:] ])))

Program = namedtuple('Program', ['name', 'weight', 'holding'])
programs = [ parse_program(i.split()) for i in get_day_input(7).split('\n')[:-1] ]

weights = {}
G = nx.DiGraph()

for i in programs: 
    G.add_edges_from([(i.name, j) for j in i.holding])
    weights[i.name] = i.weight


root = list(nx.topological_sort(G))[0]

print(f"Day 7-1: {root}")

print(G.successors(root))

def find_first_balanced(root: str):
    if len(set()) <= 1:
