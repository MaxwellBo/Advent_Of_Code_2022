# http://adventofcode.com/2016/day/24

# This was an experiment in using Julia, that was scrapped for Python,
# mainly because Julia's graph libraries are awful and immature.

importall LightGraphs

function main()

    point2map = Dict()
    poi2point = Dict()
    point2edge = Dict()

    edges = 0 # edge

    open("sample.txt") do file
        for (x, i) in enumerate(eachline(file))
            for (y, j) in enumerate(i[1:end - 1]) # Cull newlines
                edges += 1
                point2map[(x, y)] = j # Point to map spot
                point2edge[(x, y)] = edges # Point to graph edge

                if isdigit(j)
                    poi2point[j] = (x, y) # Locations of cities
                end
            end
        end
    end

    g = Graph(edges)

    for ((x, y), m) in point2map
        if m != '#' # if this is an empty space

            this_edge = point2edge[(x, y)]

            for p in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                m = get!(point2map, p, nothing)
                if !(m == nothing || m == "#") # and the other is an empty space
                    other_edge = point2edge[p]
                    add_edge!(g, this_edge, other_edge)
                end
            end
        end
    end

    function m2e(m)
        return point2edge[poi2point[m]]
    end

    pois = length(keys(poi2point))
    distances = zeros(pois, pois)

    for start in keys(poi2point)
        for finish in keys(poi2point)
            distance = length(a_star(g, m2e(start), m2e(finish)))
            distances[parse(Int64, start) + 1, parse(Int64, finish) + 1] = distance
            distances[parse(Int64, finish) + 1, parse(Int64, start) + 1] = distance
        end
    end

    h = CompleteGraph(pois)
    
    print(dijkstra_shortest_paths(h, 1, distances).dists)

    # At this point I gave up. See Day_24.py for an actual completed solution
end

main()
