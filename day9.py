numbers = list(map(int, open("day9.txt").read().strip().split("\n")))

ok = []
start = 25


def addOk(n):
    if n not in ok:
        ok.append(n)


def getList(pos, num) -> list:
    n = num.pop(pos)
    return n, num[pos-start:pos]


for n in range(len(numbers)-start):
    n += start
    numPos, lista = getList(n, numbers.copy())
    for n1 in lista:
        n1 = n1
        for n2 in lista:
            n2 = n2
            if numPos == n1 + n2 and numPos != n1 and numPos != n2:
                addOk(numPos)

for n in numbers[start:]:
    if n not in ok:
        print(n)
