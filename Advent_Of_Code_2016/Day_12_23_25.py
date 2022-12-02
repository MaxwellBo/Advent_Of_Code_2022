# http://adventofcode.com/2016/day/12
# http://adventofcode.com/2016/day/23
# http://adventofcode.com/2016/day/25

def main(day, part, a_p=0, c_p=0):
    with open("inputs/Day_{}_input.txt".format(day)) as fp:

        # Parse input
        program = [ i.split() for i in fp.read().split("\n") ]

        # Build computer
        pc = 0
        clock = [1]
        registers = { "a": a_p
                    , "b": 0
                    , "c": c_p
                    , "d": 0
                    }

        while pc < len(program):
            ins = program[pc]

            if ins[0] == "cpy":
                val = int(ins[1]) if ins[1].lstrip('-').isdigit() else registers[ins[1]]
                try:
                    registers[ins[2]] = val
                except:
                    pass

            elif ins[0] == "inc":
                registers[ins[1]] += 1

            elif ins[0] == "dec":
                registers[ins[1]] -= 1

            elif ins[0] == "jnz":
                test = int(ins[1]) if ins[1].isdigit() else registers[ins[1]]
                jump = int(ins[2]) if ins[2].lstrip('-').isdigit() else registers[ins[2]]

                pc += jump - 1 if test else 0

            elif ins[0] == "tgl":
                i = pc + registers[ins[1]]
                
                if i < len(program): 
                    ct = { "inc": "dec" # One arg
                         , "dec": "inc"
                         , "out": "inc"
                         , "tgl": "inc" 
                         , "jnz": "cpy" # Two arg
                         , "cpy": "jnz"
                         }

                    program[i][0] = ct[program[i][0]]

            elif ins[0] == "out":
                clock.append(registers[ins[1]])

                if (not (clock[-1] == 0 or clock[-1] == 1)):
                    return
                elif clock[-1] == clock[-2]:
                    return
                elif len(clock) > 50:
                    print("Part {}:".format(part), a_p)
                    exit()

            pc += 1
        else:
            print("Part {}:".format(part), registers['a'])
            
if __name__ == '__main__':
    print("Day 12")
    main(day=12, part=1) # a: 318020
    main(day=12, part=2, c_p=1) # a: 9227674
    print("\nDay 23")
    main(day=23, part=1, a_p=7) # a: 11683
    # main(day=23, part=2, a_p=12) # a: 479008243
    print ("\nDay 25")
    for i in range(1, 100000):
        main(day=25, part=1, a_p=i) # 158