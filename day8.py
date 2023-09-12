file = open("day8.txt").read().strip().split("\n")

map = []
acc = 0
pos = 0
while(True):
    if pos in map:
        print(acc)
        break
    else:
        map.append(pos)
    data = file[pos]
    if data[:3] == "acc":
        acc = acc + int(data[3:])
        pos += 1
    elif data[:3] == "jmp":
        pos = pos +int(data[3:])
    else:
        pos += 1
