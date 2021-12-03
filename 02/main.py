def part1(data):
    hor = 0
    ver = 0
    for i in range(len(data)):
        x = data[i]
        x = x.split()
        dir = x[0]
        val = x[1]
        if dir == "forward": hor += int(val)
        elif dir == "up": ver -= int(val)
        else: ver += int(val)
    print(hor * ver)

def part2(data):
    hor = 0
    ver = 0
    aim = 0
    for i in range(len(data)):
        x = data[i]
        x = x.split()
        dir = x[0]
        val = x[1]
        if dir == "forward":
            hor += int(val)
            ver += aim*int(val)
        elif dir == "up": aim -= int(val)
        else: aim += int(val)
    print(hor * ver)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    print(data)
    
    print("Part One")
    part1(data)
    
    print("Part Two")
    part2(data)
