import itertools

# grid[y][x] <- USAGE

def part1(data):
    for _ in range(80):
        for i in range(len(data)):
            if data[i] <= 0:
                data.append(8)
                data[i] = 6
            else:
                data[i] -= 1
    print(len(data))        

def part2(data):
    x = [0]*max((max(data)+1), 9)
    for fish in data:
        x[fish] += 1
    
    for _ in range(256):
        new_x = [0] * len(x)
        new_x[6] += x[0]
        new_x[8] += x[0]
        for i in range(1, len(x)):
            new_x[i-1] += x[i]
        x = new_x
    
    print(sum(x))



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    data1 = [int(x) for x in tmp[0].split(',')]
    data2 = [int(x) for x in tmp[0].split(',')]

    print("Part One")
    part1(data1)
    
    print("Part Two")
    part2(data2)
