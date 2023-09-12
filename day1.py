n = open("day1.txt").read().strip().split("\n")


def test(val, prox):
    for r2 in prox:
        if int(val)+int(r2) == 2020:
            print(val,r2)
            print(int(val)*int(r2))
            return


for r in range(len(n)):
    test(n[r], n[r:])
