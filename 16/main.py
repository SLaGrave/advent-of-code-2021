from functools import reduce

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def remove_first(data, n):
    return data[:n], data[n:]

# Part one bit
# def process_packet(bits):
#     print(bits)
#     ver_sum = 0
#     ver, bits = remove_first(bits, 3)
#     ver_sum += int(ver, 2)
#     print(f"Ver: {int(ver, 2)}")
#     type_id, bits = remove_first(bits, 3)
#     print(f"Type: {type_id}")

#     if type_id == "100":  # Literal
#         lit_value = ''
#         while True:
#             tmp, bits = remove_first(bits, 5)
#             lit_value += tmp[1:]
#             if tmp[0] == "0": break
#         print(f"Literal value: {int(lit_value, 2)}")

#     else:  # Operator
#         length_type_id, bits = remove_first(bits, 1)
#         if length_type_id == "0":  # Read 15 bits
#             l, bits = remove_first(bits, 15)
#             l = int(l, 2)
#             print(f"Reading {l} bits")
#             tmp = bits[:l]
#             while len(tmp) > 0:
#                 v, tmp = process_packet(tmp)
#                 ver_sum += v
#             bits = bits[l:]
#         if length_type_id == "1":  # Read 11 bits
#             l, bits = remove_first(bits, 11)
#             l = int(l, 2)
#             print(f"Reading {l} sub-packets")
#             for _ in range(l):
#                 v, bits = process_packet(bits)
#                 ver_sum += v
    
#     return ver_sum, bits

def process_packet(bits):
    print(bits)
    ver, bits = remove_first(bits, 3)
    print(f"Ver: {int(ver, 2)}")
    type_id, bits = remove_first(bits, 3)
    print(f"Type: {type_id}")

    if type_id == "100":  # Literal
        lit_value = ''
        while True:
            tmp, bits = remove_first(bits, 5)
            lit_value += tmp[1:]
            if tmp[0] == "0": break
        print(f"Literal value: {int(lit_value, 2)}")
        return bits, int(lit_value, 2)

    else:  # Operator
        values = list()
        length_type_id, bits = remove_first(bits, 1)
        if length_type_id == "0":  # Read 15 bits
            l, bits = remove_first(bits, 15)
            l = int(l, 2)
            print(f"Reading {l} bits")
            tmp = bits[:l]
            while len(tmp) > 0:
                tmp, x = process_packet(tmp)
                values.append(x)
            bits = bits[l:]
        if length_type_id == "1":  # Read 11 bits
            l, bits = remove_first(bits, 11)
            l = int(l, 2)
            print(f"Reading {l} sub-packets")
            for _ in range(l):
                bits, x = process_packet(bits)
                values.append(x)

        if type_id == "000": return bits, sum(values)
        if type_id == "001": return bits, reduce((lambda x, y: x*y), values)
        if type_id == "010": return bits, min(values)
        if type_id == "011": return bits, max(values)
        if type_id == "101": return bits, 1 if values[0] > values[1] else 0
        if type_id == "110": return bits, 1 if values[0] < values[1] else 0
        if type_id == "111": return bits, 1 if values[0] == values[1] else 0


def part1(data):
    bits = ''
    for c in data:
        bits += hex_to_bin[c]
    
    x = process_packet(bits)
    print(x)
        

def part2(data):
    bits = ''
    for c in data:
        bits += hex_to_bin[c]
    
    x = process_packet(bits)
    print(x)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        tmp = f.readlines()

    data = tmp[0].strip()


    # print("Part One")
    # part1(data)
    
    print("Part Two")
    part2(data)
