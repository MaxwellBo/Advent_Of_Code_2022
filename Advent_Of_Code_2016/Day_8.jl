# http://adventofcode.com/2016/day/8

WIDTH = 50
HEIGHT = 6

screen = falses(HEIGHT, WIDTH)

function rect(width, height)
    screen[1:height, 1:width] = true
end

function rotate_col(col, by)
    screen[:, col + 1] = ror!(screen[:, col + 1], by)
end

function rotate_row(row, by)
    screen[row + 1, :] = ror!(screen[row + 1, :], by)
end

function main()
    open("inputs/Day_8_input.txt") do file
        for ln in eachline(file)

            tok = split(ln)

            if tok[1] == "rect" 
                args = split(tok[2], "x")
                rect(map(x -> parse(Int, x), args)...)
            elseif tok[2] == "row"
                args = [ tok[3][3:end], tok[5] ]
                rotate_row(map(x -> parse(Int, x), args)...)
            elseif tok[2] == "column"
                args = [ tok[3][3:end], tok[5] ]
                rotate_col(map(x -> parse(Int, x), args)...)
            end

        end
    end

    println("Part 1: ", sum(screen)) # 123

    println("Part 2:\n")
    for i in 1:size(screen, 1)
        for j in screen[i, :]
            if j == true
                print('#')
            else
                print(' ')
            end
        end
        println(' ')
    end

     ##  #### ###  #  # ###  #### ###    ## ###   ###
    #  # #    #  # #  # #  #    # #  #    # #  # #
    #  # ###  ###  #  # #  #   #  ###     # #  # #
    #### #    #  # #  # ###   #   #  #    # ###   ##
    #  # #    #  # #  # #    #    #  # #  # #       #
    #  # #    ###   ##  #    #### ###   ##  #    ###

end

main()
