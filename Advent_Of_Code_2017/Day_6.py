from Day_0 import get_day_input

blocks, history = [ int(i) for i in get_day_input(6).split('\t') ], []

while True:
    max_index = blocks.index(max(blocks))
    pointer = max_index
    
    max_val, blocks[max_index] = blocks[max_index], 0

    while max_val > 0:
        pointer = (pointer + 1) % len(blocks)
        max_val -= 1
        blocks[pointer] += 1

    if tuple(blocks) in history: break

    history.append(tuple(blocks))

print(f"Day 6-1: {len(history) + 1}") # 11137
print(f"Day 6-2: {len(history) - history.index(tuple(blocks))}") # 1037
