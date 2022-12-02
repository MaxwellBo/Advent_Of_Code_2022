# http://adventofcode.com/2016/day/21

def swap_pos(x, y, l):
	l = l[:]
	l[x], l[y] = l[y], l[x]
	return l

def swap_letter(x, y, l):
	return swap_pos(l.index(x), l.index(y), l)

def rotate_left(n, l):
	return l[n:] + l[0:n]

def rotate_right(n, l):
	return rotate_left(len(l) - n, l)

def rotate_based(x, l):
	if l.index(x) >= 4:
		return rotate_right(l.index(x) + 2, l)
	else:
		return rotate_right(l.index(x) + 1, l)

def reverse_range(x, y, l):
	return l[:x] + (l[x:y+1])[::-1] + l[y+1:]

def move(x, y, l):
	l = l[:]
	elem = l.pop(x)
	l.insert(y, elem)
	return l

def main():
	with open("inputs/Day_21_input.txt") as fp:

		l = list("abcdefgh")

		for line in fp:
			tok = line.split()

			inits = (tok[0], tok[1])

			if ("swap", "position") == inits:
				l = swap_pos(int(tok[2]), int(tok[5]), l)

			elif ("swap", "letter") == inits:
				l = swap_letter(tok[2], tok[5], l)

			elif ("rotate", "left") == inits:
				l = rotate_left(int(tok[2]), l)

			elif ("rotate", "right") == inits:
				l = rotate_right(int(tok[2]), l)

			elif ("rotate", "based") == inits:
				l = rotate_based(tok[6], l)

			elif ("reverse", "positions") == inits:
				l = reverse_range(int(tok[2]), int(tok[4]), l)

			elif ("move", "position") == inits:
				l = move(int(tok[2]), int(tok[5]), l)

		print("Part 1;", "".join(l)) # cbeghdaf

if __name__ == '__main__':
	main()
