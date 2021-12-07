import math
import functools

def part1(data):
    smallest = min(data)
    largest = max(data)

    pos, fuel = 1, math.inf

    for i in range(smallest, largest+1):
        tmp = 0
        for xpos in data:
            tmp += abs(i - xpos)
        if tmp < fuel:
            fuel = tmp
            pos = i
    
    print(pos, fuel)

@functools.lru_cache(maxsize=None)
def util(x):
    if x <= 1: return x
    return sum(range(x, 0, -1))

def part2(data):
    smallest = min(data)
    largest = max(data)

    pos, fuel = 1, math.inf

    for i in range(smallest, largest+1):
        tmp = 0
        for xpos in data:
            tmp += util(abs(i - xpos))
        if tmp < fuel:
            fuel = tmp
            pos = i
    
    print(pos, fuel)



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    data1 = [int(x) for x in tmp[0].split(',')]
    data2 = [int(x) for x in tmp[0].split(',')]

    print("Part One")
    part1(data1)
    
    print("Part Two")
    part2(data2)
