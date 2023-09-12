numbers = list(map(int, open("day9.txt").read().strip().split("\n")))

target = 69316178


def sum(pos, total):
    total += numbers[pos]
    if total == target:
        return pos
    if total > target:
        return -1
    return sum(pos+1, total)


def getMinMax(pos):
    min = None
    max = None
    for n in numbers[pos[0]:pos[1]]:
        if min == None:
            min = max = n
        if n < min:
            min = n
        elif n > max:
            max = n
    return min, max


for n in range(len(numbers)):
    result = sum(n, 0)
    if result != -1:
        min, max = getMinMax([n, result])
        print(min+max, min, max)
        exit(1)
