from Day_0 import *

diagram = get_day_input(19).split('\n')

pos, facing, seen, steps = diagram[0].find('|') + len(diagram) * 1j, S, [], 0

def _read(c):
    try: return diagram[len(diagram) - int(c.imag)][int(c.real)]
    except IndexError as _:
        return ' '

while True:
    char = _read(pos)

    if   char == ' '    : break
    elif char.isalpha() : seen.append(char)
    elif char == '+'    :
        facing = next( i for i in NEIGHBOURS_4 
                       if _read(i + pos) != ' ' if i != turn_around(facing) )

    pos += facing; steps += 1

print(f"Day 19-1: {''.join(seen)}")  # GSXDIPWTU
print(f"Day 19-2: {steps}") # 16100