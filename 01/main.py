def part1(data):
    inc = 0
    dec = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]: inc+=1
        else: dec+=1
    print(inc)

def part2(data):
    inc = 0
    dec = 0
    for i in range(3, len(data)):
        if data[i] + data[i-1] + data[i-2] > data[i-3] + data[i-1] + data[i-2]: inc+=1
        else: dec+=1
    print(inc)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [int(x) for x in data]
    print(data)
    
    print("Part One")
    part1(data)
    
    print("Part Two")
    part2(data)
