# http://adventofcode.com/2016/day/2

def clamp(min_, max_, x):
    return min(max_, max(min_, x))

def main(part):

    x, y = (1, 1) if part == 1 else (0, 2)

    numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] if part == 1 else [ "  1  "
                                                                 , " 234 "
                                                                 , "56789"
                                                                 , " ABC "
                                                                 , "  D  "]

    with open("inputs/Day_2_input.txt") as fp:

        code = []

        for row in fp:
            for ins in row:
                old_x = x
                old_y = y 

                if ins == "U":
                    y -= 1
                elif ins == "D":
                    y += 1
                elif ins == "L":
                    x -= 1
                elif ins == "R":
                    x += 1

                max_ = len(numpad[0]) - 1
                x = clamp(0, max_, x)
                y = clamp(0, max_, y)

                if numpad[y][x] == ' ':
                    x = old_x
                    y = old_y

            code.append(numpad[y][x])

    print(f"Part {part}:", "".join(str(i) for i in code))

if __name__ == "__main__":
    main(1) # 61529 
    main(2) # C2C28

