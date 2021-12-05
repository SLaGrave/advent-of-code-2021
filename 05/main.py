import itertools

# grid[y][x] <- USAGE

def part1(grid, data):
    for line in data:
        start = line[0]
        stop = line[1]
        if stop[0] != start[0] and stop[1] != start[1]: continue
        hori = start[0] != stop[0] # Are we horizontal
        if hori and start[0] > stop[0]:
            tmp = start
            start = stop
            stop = tmp
        if not hori and start[1] > stop[1]:
            tmp = start
            start = stop
            stop = tmp
        for i in itertools.product(range(start[0], stop[0]+1), range(start[1], stop[1]+1)):
            grid[i[1]][i[0]] += 1
    
    # for row in grid:
    #     print(row)
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 1: total += 1
    print(total)
        

def part2(grid, data):
    for line in data:
        start = line[0]
        stop = line[1]
        x_inc = 0 if start[0] == stop[0] else(stop[0]-start[0])/abs(stop[0]-start[0])
        y_inc = 0 if start[1] == stop[1] else(stop[1]-start[1])/abs(stop[1]-start[1])

        values = [start]
        while values[-1] != stop:
            values.append([values[-1][0] + x_inc, values[-1][1] + y_inc])

        for v in values:
            grid[int(v[1])][int(v[0])] += 1

    for row in grid:
        print(row)
    
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 1: total += 1
    print(total)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]

    data = [x.split(" -> ") for x in data]
    data = [[x[0].split(","), x[1].split(",")] for x in data]
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j])):
                data[i][j][k] = int(data[i][j][k])
    print(data)
    biggest = 0
    for i in range(len(data)):
        for j in range(2):
            for k in range(2):
                if data[i][j][k] > biggest: biggest = data[i][j][k]

    # Construct grid
    biggest+=1
    grid1 = list()
    grid2 = list()
    for _ in range(biggest):
        grid1.append([0]*biggest)
        grid2.append([0]*biggest)

    print("Part One")
    part1(grid1, data)
    
    print("Part Two")
    part2(grid2, data)
