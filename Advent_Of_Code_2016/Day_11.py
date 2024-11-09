from collections import deque

xs = list(range(0, 255 + 1))
lengths = [
  int(i) for i in 
  "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110".split(',')
]
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

print(xs[0] * xs[1])