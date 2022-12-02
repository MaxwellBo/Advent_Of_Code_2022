class Person(object):
	def __init__(self):
		self.direction = 0
		self.x = 0
		self.y = 0
		self.locations = set()
		self.squelch = False

	def turn(self, char):
		self.direction += -1 if char == "L" else 1

		if self.direction >= 4:
			self.direction -= 4
		elif self.direction < 0:
			self.direction += 4

	def step(self):
		directions = [(0,1), (1,0), (0,-1), (-1, 0)]
		self.x += directions[self.direction][0]
		self.y += directions[self.direction][1]

	def walk(self, blocks):
		for i in range(0, blocks):
			self.step()

			if (self.x, self.y) in self.locations and not self.squelch:
				print("Part 2:", abs(self.x) + abs(self.y)) # 150
				self.squelch = True
			else:
				self.locations.add((self.x, self.y))

def main():

	p = Person()

	with open("inputs/Day_1_input.txt") as fp:
		for i in next(fp).split(", "):
			p.turn(i[0])
			p.walk(int(i[1:]))

	print("Part 1:", abs(p.x) + abs(p.y)) # 242

if __name__ == '__main__':
	main()