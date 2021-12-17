def simulate(x, y, x_range, y_range):
    pos = [0, 0]
    max_y = pos[1]
    flag = False
    while True:
        pos[0] += x
        pos[1] += y

        if pos[1] > max_y: max_y = pos[1]

        y -= 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        
        if pos[0] > x_range[0] and pos[1] < y_range[1]:
            flag = True
        
        if pos[0] > x_range[1] or pos[1] < y_range[0]:
            break
    
    return max_y if flag else 0

def simulate2(x, y, x_range, y_range):
    pos = [0, 0]
    flag = False
    while True:
        pos[0] += x
        pos[1] += y

        y -= 1
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        
        if pos[0] > x_range[0] and pos[1] < y_range[1]:
            flag = True
        
        if pos[0] > x_range[1] or pos[1] < y_range[0]:
            break
    
    return flag
        

def part1(x_range, y_range):
    max_y = 0

    for y in range(-10, 1000):
        for x in range(0, 30):
            tmp = simulate(x, y, x_range, y_range)
            if tmp > max_y: max_y = tmp

    print(max_y)            
        

def part2(x_range, y_range):
    pass


if __name__ == "__main__":
    # with open("input.txt", "r") as f:
    #     tmp = f.readlines()

    # data = tmp[0].strip()

    x_range = (20, 30)
    y_range = (-10, -5)


    print("Part One")
    part1(x_range, y_range)
    
    print("Part Two")
    part2(x_range, y_range)
