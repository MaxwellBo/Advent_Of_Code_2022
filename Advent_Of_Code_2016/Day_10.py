from collections import defaultdict

class Node(object):
    def __init__(self):
        self.chips = []
        self.high_sink = None
        self.low_sink = None

with open("inputs/Day_10_input.txt") as fp:

    g = defaultdict(Node)

    for line in fp:

        tokens = line.split()

        if tokens[0] == "value":
            name = tokens[-2] + tokens[-1]
            g[name].chips.append(int(tokens[1]))

        elif tokens[0] == "bot":
            target_name = tokens[0] + tokens[1]
            low_name = tokens[5] + tokens[6]
            high_name = tokens[-2] + tokens[-1]

            g[target_name].low_sink = g[low_name]
            g[target_name].high_sink = g[high_name]

    for i in range(1, 1000):    
        for (k, v) in g.items():
            if len(v.chips) == 2:
                min_, max_ = sorted(v.chips)

                if (min_, max_) == (17, 61):
                    print("Part 1:", k) # 113

                v.low_sink.chips.append(min_)
                v.high_sink.chips.append(max_)
                v.chips = []

    
    (a, b, c) = [g[f"output{i}"].chips[0] for i in [0, 1, 2]]
    print("Part 2:", a * b * c) # 12803
