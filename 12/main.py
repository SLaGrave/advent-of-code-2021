# With help from this solution:
# https://topaz.github.io/paste/#XQAAAQCuBQAAAAAAAAA0m0pnuFI8c82uPD0wiI6r5tRSCrme8SokpTv9601K98sOENz1NnI6cB0i/X8PZloQgzFPggpjGXmGlnRinYUHA8R/guIY9NBL5JrxLyZFgXW531sHDfR8pBswAkShQIAcUehLVqULHt2BTtSsbeeAWDLZYdh60XIKg7FkmpQIW2R7zx2NPkIA8QdKx3eYH1sbkZtPIOHIZD8KnI3nfmxqZqIXgtqXxVpdX1PmE894vXKccgodvahjnP6s8AaqvjZ6xdqTUqSvhdfvcalkD9IcOdhHocdb1ITnzO6MCsZbvv3N4EKsjgJoJ9DARVSihxoZHBNPGQTGBkS4NiC5wQwQpRQNzMe6C5uQjmViqRMz9tZvjsx9EBEKeLLyoSR2KR5waE17V4GlHdpn+9LFvMrkuq7+vQgwFFJnbNtlm0ygYqh9DOgOfrmFDY4ub2hWC8h0nHgC9ZVhhlkVULC/rj9/Xzi19HeGuxXf0BxhuKuupZngArN8IcLVlrwqCj35ouldOn1LBvZf+J7YrPhvzRK/vaQt8sUgvNVezQjx1i3bHzlfOV1yGcoPAPwlzFhxudZhRgMo/P/NQP+9NNOP

#TODO: Research exactly how these collections work

import collections

def part1(data):
    processing = list()
    for a, b in data:
        if a!='start': continue
        processing.append([a, b]) # Adds all 'start' edges to processing
    paths = list()
    while len(processing) > 0:
        path = processing.pop()
        current = path[-1]
        if current == 'end':
            paths.append(path)
            continue
        for a, b in data:
            if a!=current:continue
            if b in path and b.islower(): continue
            processing.append([*path, b])
    print(len(paths))



def part2(data):
    processing = list()
    for a, b in data:
        if a!='start': continue
        processing.append([a, b]) # Adds all 'start' edges to processing
    paths = list()
    while len(processing) > 0:
        path = processing.pop()
        current = path[-1]
        if current == 'end':
            paths.append(path)
            continue
        has_visited_small_twice = False
        smalls = collections.defaultdict(int)
        for cave in path:
            if cave.islower(): smalls[cave]+=1
        has_visited_small_twice = any(count == 2 for count in smalls.values())
        for a, b in data:
            if a!=current:continue
            if b in path and b.islower() and has_visited_small_twice: continue
            if b=='start': continue
            processing.append([*path, b])
    print(len(paths))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip() for x in tmp]
    tmp = [x.split('-') for x in tmp]
    for a, b in tmp[:]:
        tmp.append([b,a]) # Add reverse edges

    print("Part One")
    part1(tmp)
    
    print("Part Two")
    part2(tmp)
