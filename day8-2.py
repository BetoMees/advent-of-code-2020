file1 = open("day8.txt").read().strip()
# not 1989


def accumulator(pos, acc, data, map) -> bool:
    pos += 1
    acc = acc + int(data[3:])
    return digging(pos, acc, map)


def jump(pos, acc, data, map) -> bool:
    pos = pos + int(data[3:])
    return digging(pos, acc, map)


def next(pos, acc, map) -> bool:
    pos += 1
    return digging(pos, acc, map)


def digging(pos, acc, map) -> bool:
    if len(file) == pos:
        print("fim", pos, acc, len(map))
        exit(1)
    if pos < 0 or pos > len(file) or pos in map:
        return True
    else:
        map.append(pos)
    data = file[pos]
    if data[:3] == "acc":
        return accumulator(pos, acc, data, map)
    elif data[:3] == "jmp":
        return jump(pos, acc, data, map)
        # if result:
        #     return next(pos, acc, map)
    else:
        return next(pos, acc, map)
        # if result:
        #     return jump(pos, acc, data, map)
# file
pos = -3
while(True):
    pos += 3 + file1[pos+3:].index("jmp")
    file = file1[:pos]+"nop"+file1[pos+3:]
    file = file.split("\n")
    digging(0, 0, [])
