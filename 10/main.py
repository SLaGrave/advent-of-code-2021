mapping = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}

opening=list(mapping.keys())
closing=[x[1] for x in mapping.items()]

corrupted_points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137,
}

incomplete_points = {
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

def part1(data):
    points = 0
    for line in data:
        # print(f"Line {line}")
        chunks = list()
        for c in line:
            if c in opening: chunks.append(c)
            if c in closing:
                x = chunks.pop()
                if mapping[x] != c:
                    # print(f"\tExpected {mapping[x]} but found {c}")
                    points += corrupted_points[c]
                    break
    print(points)


def part2(data):
    data_cleaned = list()
    for line in data:
        flag = True
        # print(f"Line {line}")
        chunks = list()
        for c in line:
            if c in opening: chunks.append(c)
            if c in closing:
                x = chunks.pop()
                if mapping[x] != c:
                    # print(f"\tExpected {mapping[x]} but found {c}")
                    flag = False
                    break
        if flag: data_cleaned.append(line)
    
    # Cleaned the data
    p = list()
    for line in data_cleaned:
        points = 0
        chunks = list()
        for c in line:
            if c in opening: chunks.append(c)
            if c in closing:
                chunks.pop()
        while len(chunks) > 0:
            x = chunks.pop()
            points = (points*5) + incomplete_points[mapping[x]]
        p.append(points)
    p = sorted(p)
    print(p)
    import math
    print(p[math.ceil(len(p)/2) - 1])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip() for x in tmp]

    data1 = [x for x in tmp]
    data2 = [x for x in tmp]

    print("Part One")
    part1(data1)
    
    print("Part Two")
    part2(data2)
