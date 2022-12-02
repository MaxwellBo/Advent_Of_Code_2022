from Day_0 import get_day_input
from collections import defaultdict

d, history = defaultdict(lambda: 0), []
instructions = [ i.split(' ') for i in get_day_input(8).replace("inc", "+=").replace("dec", "-=").strip().split('\n') ]

for (r, inc, delta, _if, r2, cmp, amount) in instructions:
    exec(" ".join(["if", f"d['{r2}']", cmp, amount, ':', f"d['{r}']", inc, delta]))
    history.append(max(d.values()))

print(f"Day 8-1: {max(d.values())}") # 6343
print(f"Day 8-2: {max(history)}") # 7184
