def part1(locs, folds):
    # find largest x value
    x_max = max([x[0] for x in locs])
    y_max = max([x[1] for x in locs])

    grid = list()
    for y in range(y_max+1):
        grid.append(list())
        for x in range(x_max+1):
            grid[y].append(0)

    for loc in locs:
        x, y = loc
        grid[y][x] = 1
    
    total = 0
    for y in range(y_max+1):
        for x in range(x_max+1):
            total += grid[y][x]
    
    for fold in [folds[0]]:
        fold = fold.split('=')
        fold[1] = int(fold[1])
        if fold[0] == 'x':
            for i in range(len(grid[0])-fold[1]):
                for y in range(len(grid)):
                    grid[y][fold[1]-(i)] += grid[y][fold[1]+(i)]
                    grid[y][fold[1]-(i)] = min(1, grid[y][fold[1]-(i)])
            grid = [x[:fold[1]] for x in grid]
        else:
            for i in range(len(grid)-fold[1]):
                for x in range(len(grid[0])):
                    grid[fold[1]-(i)][x] += grid[fold[1]+(i)][x]
                    grid[fold[1]-(i)][x] = min(1, grid[fold[1]-(i)][x])
            grid = grid[:fold[1]]

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            total += grid[y][x]
    print(total)





def part2(locs, folds):
    # find largest x value
    x_max = max([x[0] for x in locs])
    y_max = max([x[1] for x in locs])

    grid = list()
    for y in range(y_max+1):
        grid.append(list())
        for x in range(x_max+1):
            grid[y].append(0)

    for loc in locs:
        x, y = loc
        grid[y][x] = 1
    
    total = 0
    for y in range(y_max+1):
        for x in range(x_max+1):
            total += grid[y][x]
    
    for fold in folds:
        fold = fold.split('=')
        fold[1] = int(fold[1])
        if fold[0] == 'x':
            for i in range(len(grid[0])-fold[1]):
                for y in range(len(grid)):
                    grid[y][fold[1]-(i)] += grid[y][fold[1]+(i)]
                    grid[y][fold[1]-(i)] = min(1, grid[y][fold[1]-(i)])
            grid = [x[:fold[1]] for x in grid]
        else:
            for i in range(len(grid)-fold[1]):
                for x in range(len(grid[0])):
                    grid[fold[1]-(i)][x] += grid[fold[1]+(i)][x]
                    grid[fold[1]-(i)][x] = min(1, grid[fold[1]-(i)][x])
            grid = grid[:fold[1]]
    
    for line in grid:
        s = ''
        for n in line:
            if n == 1: s += '#'
            else: s += '.'
        print(s)



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip() for x in tmp]

    locs = list()
    folds = list()
    for x in tmp:
        if x=='': continue
        if len(x.split(','))==2:
            x = x.split(',')
            locs.append((int(x[0]), int(x[1])))
            continue
        folds.append(x.replace('fold along ', ''))

    print("Part One")
    part1(locs, folds)
    
    print("Part Two")
    part2(locs, folds)
