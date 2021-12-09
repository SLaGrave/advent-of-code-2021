def check_neighbors(data, x, y):
    if x != 0:
        if data[y][x-1] <= data[y][x]: return False
    if x != len(data[0])-1:
        if data[y][x+1] <= data[y][x]: return False
    if y != 0:
        if data[y-1][x] <= data[y][x]: return False
    if y != len(data)-1:
        if data[y+1][x] <= data[y][x]: return False
    return True

def part1(data):
    low_points = list()
    for y in range(len(data)):
        for x in range(len(data[0])):
            # Check to see if low point
            if check_neighbors(data, x, y): low_points.append((x, y))
    
    low_points = list(set(low_points))
    total = 0
    for x, y in low_points:
        total += data[y][x] + 1
    print(total)
    return low_points



def meta(data, x, y, visited = []):
    total = 1
    if (x, y) in visited: return 0
    visited.append((x, y))
    if x != 0:
        if data[y][x-1] == 1:
            total += meta(data, x-1, y, visited)
    if x != len(data[0])-1:
        if data[y][x+1] == 1:
            total += meta(data, x+1, y, visited)
    if y != 0:
        if data[y-1][x] == 1:
            total += meta(data, x, y-1, visited)
    if y != len(data)-1:
        if data[y+1][x] == 1:
            total += meta(data, x, y+1, visited)
    return total


def part2(data, low_points):
    data = [[int(y != 9) for y in x] for x in data]

    basins = list()

    for low_point in low_points:
        basins.append(meta(data, low_point[0], low_point[1]))

    basins = list(reversed(sorted(basins)))

    print(basins[0] * basins[1] * basins[2])



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip() for x in tmp]

    data1 = [[int(y) for y in x] for x in tmp]
    data2 = [[int(y) for y in x] for x in tmp]

    print("Part One")
    low_points = part1(data1)
    
    print("Part Two")
    part2(data2, low_points)
