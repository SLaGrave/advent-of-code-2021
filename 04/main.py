class Board:
    def __init__(self, data):
        self.row1 = [int(x) for x in data[0]]
        self.row2 = [int(x) for x in data[1]]
        self.row3 = [int(x) for x in data[2]]
        self.row4 = [int(x) for x in data[3]]
        self.row5 = [int(x) for x in data[4]]
        self.called = list()

    def check(self, num):
        try:
            self.called.append((1, self.row1.index(num)))
        except: pass
        try:
            self.called.append((2, self.row2.index(num)))
        except: pass
        try:
            self.called.append((3, self.row3.index(num)))
        except: pass
        try:
            self.called.append((4, self.row4.index(num)))
        except: pass
        try:
            self.called.append((5, self.row5.index(num)))
        except: pass


        if len([x for x in self.called if x[0] == 1]) == 5: return self.calc(num)
        if len([x for x in self.called if x[0] == 2]) == 5: return self.calc(num)
        if len([x for x in self.called if x[0] == 3]) == 5: return self.calc(num)
        if len([x for x in self.called if x[0] == 4]) == 5: return self.calc(num)
        if len([x for x in self.called if x[0] == 5]) == 5: return self.calc(num)
        if len([x for x in self.called if x[1] == 1]) == 5: return self.calc(num)
        if len([x for x in self.called if x[1] == 2]) == 5: return self.calc(num)
        if len([x for x in self.called if x[1] == 3]) == 5: return self.calc(num)
        if len([x for x in self.called if x[1] == 4]) == 5: return self.calc(num)
        if len([x for x in self.called if x[1] == 5]) == 5: return self.calc(num)
        return None

    def calc(self, num):
        total = 0

        for i in range(len(self.row1)):
            if (1, i) not in self.called:
                total += self.row1[i]
        for i in range(len(self.row2)):
            if (2, i) not in self.called:
                total += self.row2[i]
        for i in range(len(self.row3)):
            if (3, i) not in self.called:
                total += self.row3[i]
        for i in range(len(self.row4)):
            if (4, i) not in self.called:
                total += self.row4[i]
        for i in range(len(self.row5)):
            if (5, i) not in self.called:
                total += self.row5[i]

        return total * num


def part1(qq, nums):
    boards = list(qq)
    for num in nums:
        for board in boards:
            x = board.check(num)
            if x != None:
                return x

def part2(qq, nums):
    boards = list(qq)
    for num in nums:
        btr = list()
        for board in boards:
            x = board.check(num)
            if x != None:
                print(x)
                btr.append(board)
        for x in btr: boards.remove(x)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    # print(data)

    nums = [int(x) for x in data[0].split(',')]

    boards1 = list()
    boards2 = list()
    
    i = 2
    while i < len(data):
        tmp = data[i:i+5]
        tmp = [q.split() for q in tmp]
        boards1.append(Board(tmp))
        boards2.append(Board(tmp))
        i += 6


    print("Part One")
    print(part1(boards1, nums))
    
    print("Part Two")
    part2(boards2, nums)

