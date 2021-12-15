def part1(data):
    # Setup dist matrix
    dist_from_end = list()
    for y in range(len(data)):
        tmp = list()
        for x in range(len(data)):
            tmp.append(float("inf"))
        dist_from_end.append(tmp)
    dist_from_end[-1][-1] = data[-1][-1]

    while True:
        # for line in dist_from_end:print(line)
        # print()

        changes = 0

        for y in range(len(data)):
            for x in range(len(data)):
                this = dist_from_end[y][x]
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if x+dx < 0 or x+dx >= len(data[0]) or y+dy < 0 or y+dy>=len(data):continue
                    if dist_from_end[y+dy][x+dx] + data[y][x] < this:
                        this = dist_from_end[y+dy][x+dx] + data[y][x]
                        changes += 1
                dist_from_end[y][x] = this

        if changes == 0: break
    
    print(dist_from_end[0][0] - data[0][0])

def helper(val, a):
    val = val + a
    while val > 9:
        val = val - 9
    return val

def part2(data):
    x_size = len(data[0])
    y_size = len(data)
    # make bigger data
    new_data = list()
    for y in range(len(data)*5):
        tmp = list()
        for x in range(len(data)*5):
            tmp.append(0)
        new_data.append(tmp)
    for y in range(len(data)):
        for x in range(len(data)):
            new_data[y+(y_size*0)][x+(x_size*0)] = helper(data[y][x], 0)
            new_data[y+(x_size*0)][x+(x_size*1)] = helper(data[y][x], 1)
            new_data[y+(x_size*0)][x+(x_size*2)] = helper(data[y][x], 2)
            new_data[y+(x_size*0)][x+(x_size*3)] = helper(data[y][x], 3)
            new_data[y+(x_size*0)][x+(x_size*4)] = helper(data[y][x], 4)

            new_data[y+(y_size*1)][x+(x_size*0)] = helper(data[y][x], 1)
            new_data[y+(x_size*1)][x+(x_size*1)] = helper(data[y][x], 2)
            new_data[y+(x_size*1)][x+(x_size*2)] = helper(data[y][x], 3)
            new_data[y+(x_size*1)][x+(x_size*3)] = helper(data[y][x], 4)
            new_data[y+(x_size*1)][x+(x_size*4)] = helper(data[y][x], 5)

            new_data[y+(y_size*2)][x+(x_size*0)] = helper(data[y][x], 2)
            new_data[y+(x_size*2)][x+(x_size*1)] = helper(data[y][x], 3)
            new_data[y+(x_size*2)][x+(x_size*2)] = helper(data[y][x], 4)
            new_data[y+(x_size*2)][x+(x_size*3)] = helper(data[y][x], 5)
            new_data[y+(x_size*2)][x+(x_size*4)] = helper(data[y][x], 6)

            new_data[y+(y_size*3)][x+(x_size*0)] = helper(data[y][x], 3)
            new_data[y+(x_size*3)][x+(x_size*1)] = helper(data[y][x], 4)
            new_data[y+(x_size*3)][x+(x_size*2)] = helper(data[y][x], 5)
            new_data[y+(x_size*3)][x+(x_size*3)] = helper(data[y][x], 6)
            new_data[y+(x_size*3)][x+(x_size*4)] = helper(data[y][x], 7)

            new_data[y+(y_size*4)][x+(x_size*0)] = helper(data[y][x], 4)
            new_data[y+(x_size*4)][x+(x_size*1)] = helper(data[y][x], 5)
            new_data[y+(x_size*4)][x+(x_size*2)] = helper(data[y][x], 6)
            new_data[y+(x_size*4)][x+(x_size*3)] = helper(data[y][x], 7)
            new_data[y+(x_size*4)][x+(x_size*4)] = helper(data[y][x], 8)

    data = new_data
    
    # Setup dist matrix
    dist_from_end = list()
    for y in range(len(data)):
        tmp = list()
        for x in range(len(data)):
            tmp.append(float("inf"))
        dist_from_end.append(tmp)
    dist_from_end[-1][-1] = data[-1][-1]

    while True:
        # for line in dist_from_end:print(line)
        # print()

        changes = 0

        for y in range(len(data)):
            for x in range(len(data)):
                this = dist_from_end[y][x]
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if x+dx < 0 or x+dx >= len(data[0]) or y+dy < 0 or y+dy>=len(data):continue
                    if dist_from_end[y+dy][x+dx] + data[y][x] < this:
                        this = dist_from_end[y+dy][x+dx] + data[y][x]
                        changes += 1
                dist_from_end[y][x] = this

        print(changes)
        if changes == 0: break
    
    print(dist_from_end[0][0] - data[0][0])



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    data = [x.strip() for x in tmp]
    data = [[int(q) for q in x] for x in data]


    # print("Part One")
    # part1(data)
    
    print("Part Two")
    part2(data)
