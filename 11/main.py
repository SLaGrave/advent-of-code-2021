# Helped step through using
# https://github.com/Goldenlion5648/AdventOfCode2021/blob/master/11.py#L3

size = 10

adjacent = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

grid = list()
for y in range(size):
    for x in range(size):
        grid.append((y, x))

def flash(data, y, x, seen):
    if (y, x) in seen: return
    seen.add((y, x))
    for (dy, dx) in adjacent:
        if (y+dy, x+dx) in grid:
            data[y+dy][x+dx] += 1
            if data[y+dy][x+dx] > 9: flash(data, y+dy, x+dx, seen)
            

def part1(data):
    total_flashes = 0
    for i in range(100):
        seen = set()
        for y, x in grid:
            data[y][x] += 1
        for y, x in grid:
            if data[y][x] > 9: flash(data, y, x, seen)
        total_flashes += len(seen)
        for y, x in seen:
            data[y][x] = 0
    print(total_flashes)


def part2(data):
    total_flashes = 0
    for i in range(10000):
        seen = set()
        for y, x in grid:
            data[y][x] += 1
        for y, x in grid:
            if data[y][x] > 9: flash(data, y, x, seen)
        total_flashes += len(seen)
        for y, x in seen:
            data[y][x] = 0
        if sum([sum(q) for q in data]) == 0:
            print(1+i)
            break


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip() for x in tmp]

    data1 = [[int(q) for q in x] for x in tmp]
    data2 = [[int(q) for q in x] for x in tmp]

    print("Part One")
    part1(data1)
    
    print("Part Two")
    part2(data2)
