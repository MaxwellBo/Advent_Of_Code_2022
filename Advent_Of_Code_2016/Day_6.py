# http://adventofcode.com/2016/day/6

from collections import Counter

def main(part):
    with open("inputs/Day_6_input.txt") as fp:
        rotated_message = [  "".join(char) for char in zip(*fp.read().split()[::-1]) ]

        index = 0 if part == 1 else -1 # -1 getting the least common
        error_corrected = "".join(Counter(line).most_common()[index][0] for line in rotated_message)

        print(f"Part {part}:", error_corrected)

if __name__ == '__main__':
    main(part=1) # kjxfwkdh
    main(part=2) # xrwcsnps
