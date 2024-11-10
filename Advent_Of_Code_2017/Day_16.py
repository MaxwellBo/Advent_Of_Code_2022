import string

programs = list(string.ascii_lowercase[0:16])

with open('inputs/day_16.txt') as f:
  moves = f.read().split(',')

def act(move):
  global programs

  if move.startswith('s'):
    count = int(move[1:])
    end = programs[-count:]
    start = programs[:-count]
    programs = end + start
  elif move.startswith('x'):
    A, B = move[1:].split('/')
    A = int(A)
    B = int(B)
    programs[A], programs[B] = programs[B], programs[A]
  elif move.startswith('p'):
    A, B = move[1], move[3]
    ia = programs.index(A)
    ib = programs.index(B)
    programs[ia], programs[ib] = programs[ib], programs[ia]

for move in moves:
  act(move)

print("".join(programs)) # dcmlhejnifpokgba

programs = list(string.ascii_lowercase[0:16])
cycle = []

while True:
  slug = "".join(programs)
  if slug in cycle:
    break
  else:
    cycle.append(slug)

  for move in moves:
    act(move)

A_BILLION = 1_000_000_000
remainder = A_BILLION % len(cycle)
print(cycle[remainder]) # ifocbejpdnklamhgq