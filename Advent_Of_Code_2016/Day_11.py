from collections import deque

INPUT = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"

xs = list(range(0, 255 + 1))
lengths = [ int(i) for i in INPUT.split(',') ]
skip_size = 0
current_position = 0 

def twist(length):
  global skip_size, xs, current_position

  d= deque(xs)
  d.rotate(-current_position)
  d = list(d)
  reverse = d[:length]
  dont_reverse = d[length:]

  new = list(reversed(reverse)) + dont_reverse
  d = deque(new)
  d.rotate(current_position)
  xs = list(d)

  current_position += length + skip_size
  skip_size += 1


for length in lengths:
  twist(length)

print(xs[0] * xs[1]) # 23874 

xs = list(range(0, 255 + 1))
skip_size = 0
current_position = 0 
lengths = [ 
  ord(c) for c in INPUT
] + [ 17, 31, 73, 47, 23 ]

for _ in range(64):
  for length in lengths:
    twist(length)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

sparse_hash = list(xs)
dense_hash = []

for chunk in chunks(sparse_hash, 16):
  acc = chunk[0]
  for i in chunk[1:]:
    acc ^= i

  dense_hash.append(acc)

knot_hash = "".join(format(i, 'x').zfill(2) for i in dense_hash)

assert len(knot_hash) == 32 
print(knot_hash) # e1a65bfb5a5ce396025fab5528c25a87