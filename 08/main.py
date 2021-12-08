def part1(data):
    total = 0
    for i in data:
        display = i[1]
        for item in display:
            x = len(item)
            if x == 2 or x == 3 or x == 4 or x == 7: total += 1
    print(total)

mapping = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg'
]

# a 8 -
# b 6 -
# c 8 -
# d 7 -
# e 4 - 
# f 9 - 
# g 7 -

def part2(data):
    total = 0
    for i in data: # For each row
        this_mapping = {} # Make the mapping
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            contained = [x for x in i[0] if letter in x]
            if len(contained) == 9: this_mapping[letter] = 'f'
            if len(contained) == 4: this_mapping[letter] = 'e'
            if len(contained) == 6: this_mapping[letter] = 'b'
            if len(contained) == 8:
                # find the shortest one
                tmp = [x for x in i[0] if len(x)==2][0]
                if letter in tmp: this_mapping[letter] = 'c'
                else: this_mapping[letter] = 'a'
            if len(contained) == 7:
                # find the 4
                tmp = [x for x in i[0] if len(x)==4][0]
                if letter in tmp: this_mapping[letter] = 'd'
                else: this_mapping[letter] = 'g'
        
        # Solve the end
        s = ''
        for digit in i[1]:
            s2 = list()
            for c in digit:
                s2 += this_mapping[c]
            s2 = sorted(s2)
            s3 = ''
            for q in s2:
                s3 += q
            s += str(mapping.index(s3))
        s = int(s)
        total += s
    print(total)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    tmp = [x.strip().split("|") for x in tmp]

    data1 = [[x[0].strip().split(), x[1].strip().split()] for x in tmp]
    data2 = [[x[0].strip().split(), x[1].strip().split()] for x in tmp]

    print("Part One")
    part1(data1)
    
    print("Part Two")
    part2(data2)
