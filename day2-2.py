file = open("day2.txt").read().strip().split("\n")


def test(val):
    rule, v = val.split(": ")
    minmax, letter = rule.split(" ")
    _min, _max = minmax.split("-")
    if(letter == v[int(_min) - 1] and letter != v[int(_max) - 1] or letter != v[int(_min) - 1] and letter == v[int(_max) - 1]):
        return 1
    return 0


c = 0
for f in file:
    c += test(f)
print(c)
