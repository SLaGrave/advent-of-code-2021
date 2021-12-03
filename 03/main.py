def part1(data):
    data = [x.strip() for x in data]
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        z = 0
        o = 0
        for j in range(len(data)):
            if data[j][i] == "1": o += 1
            else: z += 1
        if z > o:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(int(gamma, 2) * int(epsilon, 2))

def meta(data):
    data = [x.strip() for x in data]
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        z = 0
        o = 0
        for j in range(len(data)):
            if data[j][i] == "1": o += 1
            else: z += 1
        if z > o:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return(gamma, epsilon)


def part2(data):
    data = [x.strip() for x in data]
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        z = 0
        o = 0
        for j in range(len(data)):
            if data[j][i] == "1": o += 1
            else: z += 1
        if z > o:
            gamma += "0"
            epsilon += "1"
        elif z == o:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "1"
            epsilon += "0"
    
    print(gamma, epsilon)

    # Find oxy
    oxy = None
    data_ox = data
    for i in range(len(data_ox[0])):
        data_ox = [x for x in data_ox if x[i] == gamma[i]]
        gamma, _ = meta(data_ox)
        if len(data_ox) == 1:
            oxy = data_ox[0]
            break
    print(oxy, data_ox)

    co2 = None
    data_co2 = data
    for i in range(len(data_co2[0])):
        data_co2 = [x for x in data_co2 if x[i] == epsilon[i]]
        _, epsilon = meta(data_co2)
        if len(data_co2) == 1:
            co2 = data_co2[0]
            break
    print(co2, data_co2)

    print(int(oxy, 2) * int(co2, 2))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    print(data)
    
    print("Part One")
    part1(data)
    
    print("Part Two")
    part2(data)
