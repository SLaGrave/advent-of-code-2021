import collections

def part1(template, insertions):
    polymer = template

    for step in range(10):
        new_polymer = ''
        for i in range(len(polymer)-1):
            first = polymer[i]
            second = polymer[i+1]
            pair = first + second
            x = [x for x in insertions if x[0]==pair][0][1  ]
            new_polymer = new_polymer[:-1] + first + x + second
        polymer = new_polymer
    
    # Solve it
    tmp = collections.defaultdict(int)
    for c in polymer:
        tmp[c] += 1
    print(max(tmp.values()) - min(tmp.values()))


def part2(template, insertions):
    # initial setup
    pairs = collections.defaultdict(int)
    for i in range(len(template)-1):
        pair = template[i] + template[i+1]
        pairs[pair] += 1

    for step in range(40):
        new_pairs = collections.defaultdict(int)
        for key, value in pairs.items():
            inserted = [x for x in insertions if x[0]==key][0][1]
            new_pairs[key[0] + inserted] += value
            new_pairs[inserted + key[1]] += value
        pairs = new_pairs
    
    # Solve it
    tmp = collections.defaultdict(int)
    for pair, value in pairs.items():
        tmp[pair[0]] += value
        tmp[pair[1]] += value
    tmp = [x/2 for x in tmp.values()]
    print(max(tmp) - min(tmp))



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    insertions = [x.strip() for x in tmp]
    insertions = [(x.split(' -> ')[0], x.split(' -> ')[1]) for x in insertions]

    template = "OOBFPNOPBHKCCVHOBCSO"


    print("Part One")
    part1(template, insertions)
    
    print("Part Two")
    part2(template, insertions)
